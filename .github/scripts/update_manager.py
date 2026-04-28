import json
import os
import sys

def update_bunker():
    # Obtener el payload y limpiar posibles espacios o comillas extra
    payload_raw = os.getenv('PAYLOAD', '').strip()
    
    print(f"DEBUG: Payload recibido: {payload_raw}")

    # VALIDACIÓN INICIAL: Si no hay nada, terminar en paz
    if not payload_raw or payload_raw in ['null', '{}', 'None']:
        print("⚠️ Aviso: Ejecución sin datos (posiblemente manual). Nada que actualizar.")
        return

    try:
        payload = json.loads(payload_raw)
    except json.JSONDecodeError as e:
        print(f"❌ Error: El payload no es un JSON válido: {e}")
        return

    # Usar .get() con calma
    module = payload.get('module')
    action = payload.get('action')
    new_data = payload.get('data')
    nested_key = payload.get('nested')

    if not module:
        print("❌ Error: No se especificó el archivo (module) a modificar.")
        return

    file_path = f"{module}.json"
    
    if not os.path.exists(file_path):
        print(f"❌ Error: El archivo {file_path} no existe en la raíz.")
        return

    # Leer el archivo actual
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = json.load(f)
    except Exception as e:
        print(f"❌ Error al leer {file_path}: {e}")
        return

    # Lógica de actualización (Ejemplo: Añadir)
    if action == 'add':
        if nested_key:
            if nested_key in content:
                content[nested_key].append(new_data)
            else:
                content[nested_key] = [new_data]
        else:
            if isinstance(content, list):
                content.append(new_data)
            else:
                print("❌ Error: El archivo no es una lista y no se especificó 'nested'.")
                return

    # Guardar cambios
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(content, f, indent=4, ensure_ascii=False)
    
    print(f"✅ Éxito: {file_path} actualizado correctamente.")

if __name__ == "__main__":
    update_bunker()
