import re

class Utilidad:
    def __init__(self):
        pass

    def minusculas_sin_espacios(self, cadena):
        # Usamos re.sub para reemplazar todos los caracteres no alfanuméricos con una cadena vacía
        resultado_n = re.sub(r'[^a-zA-Z0-9]', '', cadena)
        return resultado_n.lower()

    def string_to_int(self, cadena):
        try:
            return int(cadena)
        except ValueError:
            raise ValueError(f"'{cadena}' no se puede convertir a int")