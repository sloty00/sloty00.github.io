import json
import os

def update_bunker():
    payload_str = os.getenv('PAYLOAD')
    
    # 1. Validación de seguridad para evitar el AttributeError
    if not payload_str or payload_str == 'null' or payload_str == '{}':
        print("⚠️ Ejecución detectada sin datos (posiblemente manual).")
        print("Finalizando proceso sin cambios para evitar errores.")
        return

    try:
        # 2. Intentar parsear el JSON de forma segura
        payload = json.loads(payload_str)
    except Exception as e:
        print(f"❌ Error al decodificar el JSON: {e}")
        return

    # 3. Extraer datos con valores por defecto para evitar errores de tipo None
    module = payload.get('module')
    action = payload.get('action')
    new_data = payload.get('data')
    nested_key = payload.get('nested')

    # Si falta el módulo, no podemos seguir
    if not module:
        print("❌ Error: No se especificó el módulo en el payload.")
        return

    file_path = f"{module}.json" 
    
    if not os.path.exists(file_path):
        print(f"❌ Error: El archivo {file_path} no se encontró en la raíz.")
        return

    # 4. Carga y actualización con manejo de archivos vacíos
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = json.load(f)
    except json.JSONDecodeError:
        print(f"⚠️ El archivo {file_path} estaba vacío o corrupto. Inicializando...")
        content = {} if nested_key else []

    if action == 'add':
        if nested_key:
            if isinstance(content, dict):
                if nested_key in content:
                    content[nested_key].append(new_data)
                else:
                    content[nested_key] = [new_data]
            else:
                print(f"❌ Error: Se esperaba un objeto en {file_path} para la clave {nested_key}")
                return
        else:
            if isinstance(content, list):
                content.append(new_data)
            else:
                print(f"❌ Error: Se esperaba una lista en {file_path}")
                return

    # 5. Guardado final
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(content, f, indent=4, ensure_ascii=False)
    
    print(f"✅ Éxito: {module}.json actualizado correctamente.")

if __name__ == "__main__":
    update_bunker()
