import re

class Utilidad:
    def __innit__(self):
        pass

    def minusculas_sin_espacios(self, cadena):
        # Usamos re.sub para reemplazar todos los caracteres no alfanuméricos con una cadena vacía
        resultado = re.sub(r'[^a-zA-Z0-9]', '', cadena)
        return resultado.lower()

    def string_to_int(self, cadena):
        try:
            return int(cadena)
        except ValueError:
            raise ValueError(f"'{cadena}' no se puede convertir a int")