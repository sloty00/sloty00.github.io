import json
import os

def update_bunker():
    # 1. Obtener datos del entorno (GitHub Actions)
    payload_raw = os.getenv('PAYLOAD', '').strip()
    
    print(f"DEBUG: Payload recibido: {payload_raw}")

    # 2. Validación de seguridad para no romper el script si no hay datos
    if not payload_raw or payload_raw in ['null', '{}', 'None']:
        print("⚠️ Aviso: Ejecución manual o sin datos. Saliendo sin cambios.")
        return

    try:
        payload = json.loads(payload_raw)
    except json.JSONDecodeError as e:
        print(f"❌ Error: El JSON recibido está mal formado: {e}")
        return

    # 3. Extraer variables del JSON enviado desde tu web
    module = payload.get('module')      # Ej: "estudios"
    action = payload.get('action')      # Ej: "add"
    new_data = payload.get('data')      # El nuevo registro
    nested_key = payload.get('nested')  # Ej: "certificaciones"

    if not module:
        print("❌ Error: No se especificó el módulo.")
        return

    file_path = f"{module}.json"
    
    # 4. Verificar si el archivo existe antes de intentar leerlo
    if not os.path.exists(file_path):
        print(f"❌ Error: El archivo {file_path} no existe en la raíz.")
        return

    # 5. LECTURA: Abrimos el archivo para traer los datos actuales a la memoria
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = json.load(f)
    except Exception as e:
        print(f"❌ Error crítico leyendo el archivo actual: {e}")
        return

    # 6. LÓGICA DE ACTUALIZACIÓN: Aquí es donde protegemos tus datos
    if action == 'add':
        if nested_key:
            # CASO A: El JSON es un objeto { "clave": [] } (como estudios.json)
            if isinstance(content, dict):
                # Si la clave no existe (ej: "certificaciones"), la creamos como lista
                if nested_key not in content:
                    content[nested_key] = []
                
                # IMPORTANTE: Verificamos que sea una lista antes de agregar
                if isinstance(content[nested_key], list):
                    content[nested_key].append(new_data)
                else:
                    print(f"❌ Error: {nested_key} existe pero no es una lista.")
                    return
            else:
                print(f"❌ Error: El archivo {file_path} debería ser un objeto {{}}.")
                return
        else:
            # CASO B: El JSON es una lista pura [] (como desarrollo.json)
            if isinstance(content, list):
                content.append(new_data)
            else:
                print(f"❌ Error: El archivo {file_path} debería ser una lista [].")
                return

    # 7. ESCRITURA FINAL: Guardamos todo (lo viejo + lo nuevo)
    # Usamos 'w' para sobrescribir el archivo completo con la versión actualizada en memoria
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            # indent=4 lo hace legible, ensure_ascii=False respeta tildes y ñ
            json.dump(content, f, indent=4, ensure_ascii=False)
        print(f"✅ Éxito: {file_path} actualizado. Registro añadido correctamente.")
    except Exception as e:
        print(f"❌ Error al guardar los cambios: {e}")

if __name__ == "__main__":
    update_bunker()
