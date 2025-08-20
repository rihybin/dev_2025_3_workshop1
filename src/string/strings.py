import re

class Strings:
    """
    Clase con métodos para manipulación y operaciones con cadenas de texto.
    Incluye funciones para manipular, validar y transformar strings.
    """
    
    def es_palindromo(self, texto):
        """
        Verifica si una cadena es un palíndromo (se lee igual de izquierda a derecha y viceversa).
        
        """
        # Limpia el texto, eliminando espacios y convirtiendo a minúsculas
        texto_limpio = "".join(char.lower() for char in texto if char.isalnum())
        return texto_limpio == texto_limpio[::-1]
    
    def invertir_cadena(self, texto):
        """
        Invierte una cadena de texto sin usar slicing ni reversed().
        
        """
        cadena_invertida = ""
        for caracter in texto:
            cadena_invertida = caracter + cadena_invertida
        return cadena_invertida
    
    def contar_vocales(self, texto):
        """
        Cuenta el número de vocales en una cadena.
        
        """
        vocales = "aeiouAEIOU"
        contador = 0
        for caracter in texto:
            if caracter in vocales:
                contador += 1
        return contador
    
    def contar_consonantes(self, texto):
        """
        Cuenta el número de consonantes en una cadena.
        
        """
        vocales = "aeiouAEIOU"
        consonantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
        contador = 0
        for caracter in texto:
            if caracter in consonantes:
                contador += 1
        return contador
    
    def es_anagrama(self, texto1, texto2):
        """
        Verifica si dos cadenas son anagramas (contienen exactamente los mismos caracteres).
        
        """
        # Elimina espacios y convierte a minúsculas para una comparación justa
        limpio1 = texto1.replace(" ", "").lower()
        limpio2 = texto2.replace(" ", "").lower()
        return sorted(limpio1) == sorted(limpio2)
    
    def contar_palabras(self, texto):
        """
        Cuenta el número de palabras en una cadena.
        
        """
        palabras = texto.split()
        return len(palabras)
    
    def palabras_mayus(self, texto):
        """
        Pon en Mayuscula la primera letra de cada palabra en una cadena.
        
        """
        return texto.title()
    
    def eliminar_espacios_duplicados(self, texto):
        """
        Elimina espacios duplicados en una cadena.
        
        """
        # Usa una expresión regular para reemplazar uno o más espacios por un solo espacio.
        return re.sub(r' +', ' ', texto)
    
    def es_numero_entero(self, texto):
        """
        Verifica si una cadena representa un número entero sin usar isdigit().
        
        """
        if not texto:
            return False
        
        # Manejar signos
        inicio = 0
        if texto[0] in ('-', '+'):
            inicio = 1
        
        # Verificar que el resto de los caracteres sean dígitos
        for i in range(inicio, len(texto)):
            if not '0' <= texto[i] <= '9':
                return False
        
        # Asegurarse de que no sea solo un signo
        return len(texto) > inicio
    
    def cifrar_cesar(self, texto, desplazamiento):
        """
        Aplica el cifrado César a una cadena de texto.
        
        """
        resultado = ""
        for caracter in texto:
            if 'a' <= caracter <= 'z':
                posicion = ord(caracter) - ord('a')
                nueva_posicion = (posicion + desplazamiento) % 26
                nuevo_caracter = chr(nueva_posicion + ord('a'))
                resultado += nuevo_caracter
            elif 'A' <= caracter <= 'Z':
                posicion = ord(caracter) - ord('A')
                nueva_posicion = (posicion + desplazamiento) % 26
                nuevo_caracter = chr(nueva_posicion + ord('A'))
                resultado += nuevo_caracter
            else:
                resultado += caracter
        return resultado
    
    def descifrar_cesar(self, texto, desplazamiento):
        """
        Descifra una cadena cifrada con el método César.
        
        """
        # Descifrar es lo mismo que cifrar con un desplazamiento negativo
        return self.cifrar_cesar(texto, -desplazamiento)
    
    def encontrar_subcadena(self, texto, subcadena):
        """
        Encuentra todas las posiciones de una subcadena en un texto sin usar find() o index().
        
        """
        if not subcadena:
            return []
        
        posiciones = []
        len_texto = len(texto)
        len_sub = len(subcadena)
        
        for i in range(len_texto - len_sub + 1):
            if texto[i:i + len_sub] == subcadena:
                posiciones.append(i)
                
        return posiciones