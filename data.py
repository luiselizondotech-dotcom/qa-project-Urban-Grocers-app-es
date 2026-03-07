# data.py
import copy

# --- Datos para crear usuario ---
user_body = {
    "firstName": "Max",
    "phone": "+10005553535",
    "address": "8042 Lancaster Ave.Hamburg, NY"
}

# --- Kit base ---
kit_base_body = {
    "name": "NombreDePrueba"
}

# --- Valores límite generados programáticamente (siempre exactos) ---
kit_name_511_chars = "a" * 511
kit_name_512_chars = "a" * 512

# --- Validación automática al importar ---
assert len(kit_name_511_chars) == 511, f"Error: kit_name_511_chars tiene {len(kit_name_511_chars)} caracteres"
assert len(kit_name_512_chars) == 512, f"Error: kit_name_512_chars tiene {len(kit_name_512_chars)} caracteres"

# --- Factory function ---
def get_kit_body(name):
    current_body = copy.deepcopy(kit_base_body)
    current_body["name"] = name
    return current_body