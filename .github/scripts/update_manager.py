import json
import os

def update_bunker():
    # 1. Obtener datos del entorno
    payload_raw = os.getenv('PAYLOAD', '').strip()
    
    print(f"DEBUG: Payload recibido: {payload_raw}")

    # 2. Validación de seguridad mejorada
    if not payload_raw or payload_raw in ['null', '{}', 'None', '']:
        print("⚠️ Aviso: Ejecución sin datos (posible inicio manual). Saliendo sin cambios.")
        return

    try:
        payload = json.loads(payload_raw)
        if payload is None:
            print("⚠️ Aviso: El Payload es nulo después de parsear.")
            return
    except json.JSONDecodeError as e:
        print(f"❌ Error: El JSON recibido está mal formado: {e}")
        return

    # 3. Extraer variables y Mapeo de Rutas
    module = payload.get('module')
    action = payload.get('action')
    new_data = payload.get('data')
    nested_key = payload.get('nested')
    index = payload.get('index')

    files_map = {
        "desarrollo": "data/projects.json",
        "estudios": "data/education.json",
        "experiencia": "data/experience.json"
    }

    file_path = files_map.get(module)
    
    if not file_path:
        print(f"❌ Error: El módulo '{module}' no tiene un archivo mapeado.")
        return

    if not os.path.exists(file_path):
        print(f"❌ Error: El archivo {file_path} no existe.")
        return

    # 4. LECTURA
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = json.load(f)
    except Exception as e:
        print(f"❌ Error crítico leyendo el archivo: {e}")
        return

    # 5. DETERMINAR LISTA OBJETIVO
    if nested_key:
        target_list = content.get(nested_key, [])
    else:
        target_list = content

    # 6. LÓGICA DE ACTUALIZACIÓN (Ahora con DELETE)
    if action == 'add':
        target_list.append(new_data)
        print(f"✅ Registro añadido a {file_path}.")

    elif action == 'edit' or action == 'delete':
        if index is None:
            print(f"❌ Error: La acción '{action}' requiere un índice.")
            return
        
        try:
            idx = int(index)
            if 0 <= idx < len(target_list):
                if action == 'edit':
                    target_list[idx] = new_data
                    print(f"✅ Registro en índice {idx} actualizado.")
                else: # action == 'delete'
                    eliminado = target_list.pop(idx)
                    print(f"✅ Registro eliminado en índice {idx}.")
            else:
                print(f"❌ Error: Índice {idx} fuera de rango.")
                return
        except (ValueError, TypeError):
            print(f"❌ Error: El índice '{index}' no es válido.")
            return
    else:
        print(f"⚠️ Aviso: Acción '{action}' no reconocida.")
        return

    # 7. ESCRITURA FINAL
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(content, f, indent=2, ensure_ascii=False)
        print(f"🚀 Éxito: {file_path} actualizado correctamente vía GitOps.")
    except Exception as e:
        print(f"❌ Error al guardar: {e}")

if __name__ == "__main__":
    update_bunker()
