import json
import os

def update_bunker():
    # 1. Obtener datos del entorno (GitHub Actions)
    payload_raw = os.getenv('PAYLOAD', '').strip()
    
    print(f"DEBUG: Payload recibido: {payload_raw}")

    # 2. Validación de seguridad
    if not payload_raw or payload_raw in ['null', '{}', 'None']:
        print("⚠️ Aviso: Ejecución manual o sin datos. Saliendo sin cambios.")
        return

    try:
        payload = json.loads(payload_raw)
    except json.JSONDecodeError as e:
        print(f"❌ Error: El JSON recibido está mal formado: {e}")
        return

    # 3. Extraer variables (Incluyendo el nuevo 'index')
    module = payload.get('module')      # Ej: "estudios"
    action = payload.get('action')      # Ej: "add" o "edit"
    new_data = payload.get('data')      # El registro (nuevo o editado)
    nested_key = payload.get('nested')  # Ej: "certificaciones"
    index = payload.get('index')        # Posición en la lista (para editar)

    if not module:
        print("❌ Error: No se especificó el módulo.")
        return

    file_path = f"{module}.json"
    
    if not os.path.exists(file_path):
        print(f"❌ Error: El archivo {file_path} no existe en la raíz.")
        return

    # 4. LECTURA
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = json.load(f)
    except Exception as e:
        print(f"❌ Error crítico leyendo el archivo actual: {e}")
        return

    # 5. LÓGICA DE ACTUALIZACIÓN (Protección de datos)
    
    # Determinar la lista objetivo (si es anidada como estudios.json o plana como desarrollo.json)
    if nested_key:
        if not isinstance(content, dict) or nested_key not in content:
            print(f"❌ Error: Estructura de {file_path} inválida para llave '{nested_key}'")
            return
        target_list = content[nested_key]
    else:
        if not isinstance(content, list):
            print(f"❌ Error: El archivo {file_path} debería ser una lista [].")
            return
        target_list = content

    # --- ACCIÓN: AÑADIR ---
    if action == 'add':
        target_list.append(new_data)
        print(f"✅ Registro añadido a {file_path}.")

    # --- ACCIÓN: EDITAR ---
    elif action == 'edit':
        if index is None:
            print("❌ Error: Acción 'edit' requiere un índice.")
            return
        
        try:
            index = int(index)
            if 0 <= index < len(target_list):
                target_list[index] = new_data
                print(f"✅ Registro en índice {index} actualizado correctamente.")
            else:
                print(f"❌ Error: Índice {index} fuera de rango (Largo: {len(target_list)}).")
                return
        except ValueError:
            print(f"❌ Error: El índice '{index}' no es un número válido.")
            return

    else:
        print(f"⚠️ Aviso: Acción '{action}' no reconocida.")
        return

    # 6. ESCRITURA FINAL
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            # indent=4 para legibilidad, ensure_ascii=False para tildes/ñ
            json.dump(content, f, indent=4, ensure_ascii=False)
        print(f"🚀 Éxito: {file_path} sincronizado con los nuevos cambios.")
    except Exception as e:
        print(f"❌ Error al guardar los cambios: {e}")

if __name__ == "__main__":
    update_bunker()
