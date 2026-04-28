# UBICACIÓN: .github/scripts/update_manager.py

import json
import os

def update_bunker():
    payload_str = os.getenv('PAYLOAD')
    if not payload_str:
        return

    payload = json.loads(payload_str)
    module = payload.get('module')
    action = payload.get('action')
    new_data = payload.get('data')
    nested_key = payload.get('nested')

    # CAMBIO AQUÍ: Ahora apunta a la raíz del repositorio
    file_path = f"{module}.json" 
    
    if not os.path.exists(file_path):
        print(f"Error: El archivo {file_path} no se encontró en la raíz.")
        return

    with open(file_path, 'r', encoding='utf-8') as f:
        content = json.load(f)

    if action == 'add':
        if nested_key:
            if nested_key in content:
                content[nested_key].append(new_data)
            else:
                content[nested_key] = [new_data]
        else:
            content.append(new_data)

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(content, f, indent=4, ensure_ascii=False)
    
    print(f"Éxito: {module}.json actualizado en la raíz.")

if __name__ == "__main__":
    update_bunker()
