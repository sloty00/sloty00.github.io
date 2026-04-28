import json
import os

def update_bunker():
    # 1. Recuperar los datos enviados desde el JS
    payload_str = os.getenv('PAYLOAD')
    if not payload_str:
        print("No se recibió payload.")
        return

    payload = json.loads(payload_str)
    module = payload.get('module')
    action = payload.get('action')
    new_data = payload.get('data')
    nested_key = payload.get('nested')

    # 2. Definir la ruta del archivo (ajusta según tu estructura)
    # Si tus JSON están en la raíz, deja solo f"{module}.json"
    file_path = f"data/{module}.json" 
    
    if not os.path.exists(file_path):
        print(f"Error: El archivo {file_path} no existe.")
        return

    # 3. Leer el JSON actual
    with open(file_path, 'r', encoding='utf-8') as f:
        content = json.load(f)

    # 4. Aplicar la lógica de actualización
    if action == 'add':
        if nested_key:
            # Caso de estudios.json que tiene { "certificaciones": [...] }
            if nested_key in content:
                content[nested_key].append(new_data)
            else:
                content[nested_key] = [new_data]
        else:
            # Caso de desarrollo o experiencia que son [ {}, {} ]
            content.append(new_data)

    # 5. Guardar los cambios
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(content, f, indent=4, ensure_ascii=False)
    
    print(f"Éxito: Registro añadido a {module}.json")

if __name__ == "__main__":
    update_bunker()
