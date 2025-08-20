class Conversion:
    def celsius_a_fahrenheit(self, celsius):
        """
        Convierte temperatura de Celsius a Fahrenheit.
        
        """
        fahrenheit = (celsius * 9/5) + 32
        return fahrenheit
    
    def fahrenheit_a_celsius(self, fahrenheit):
        """
        Convierte temperatura de Fahrenheit a Celsius.
        
        """
        celsius = (fahrenheit-32) * 5/9
        return celsius
    
    def metros_a_pies(self, metros):
        """
        Convierte distancia de metros a pies.
        
        """
        pies=(metros*3.28084)
        return pies
    
    def pies_a_metros(self, pies):
        """
        Convierte distancia de pies a metros.
        
        """
        metros=(pies/3.28084)
        return metros
    
    def decimal_a_binario(self, decimal):
        """
        Convierte un número decimal a su representación binaria.
        
        """
        if decimal == 0:
            return "0"
        return bin(decimal)[2:]
    
    def binario_a_decimal(self, binario):
        """
        Convierte un número binario a decimal.
        
        """
        return int(binario, 2)
    
    def decimal_a_romano(self, numero):
        """
        Convierte un número decimal a numeración romana.

        """
        valores = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        simbolos = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        romano = ""
        i = 0
        while numero > 0:
            for _ in range(numero // valores[i]):
                romano += simbolos[i]
                numero -= valores[i]
            i += 1
        return romano
    
    def romano_a_decimal(self, romano):
        """
        Convierte un número romano a decimal.
        
        """
        valores = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        decimal = 0
        i = 0
        while i < len(romano):
            if i + 1 < len(romano) and valores[romano[i]] < valores[romano[i+1]]:
                decimal += valores[romano[i+1]] - valores[romano[i]]
                i += 2
            else:
                decimal += valores[romano[i]]
                i += 1
        return decimal
    
    def texto_a_morse(self, texto):
        """
        Convierte texto a código Morse.
        
        """
        morse_code = {
            'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
            'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
            'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
            'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
            'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
            '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
            '9': '----.', '0': '-----', ' ': ' '
        }
        texto_morse = ""
        for char in texto.upper():
            if char in morse_code:
                texto_morse += morse_code[char] + " "
        return texto_morse.strip()
    
    def morse_a_texto(self, morse):
        """
        Convierte código Morse a texto.
        ...
        """
        morse_code = {
            '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F',
            '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
            '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R',
            '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
            '-.--': 'Y', '--..': 'Z', '.----': '1', '..---': '2', '...--': '3',
            '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8',
            '----.': '9', '-----': '0', ' ': ' '
        }
        texto = ""
        codigos_morse = morse.strip().split(' ')
        for codigo in codigos_morse:
            if codigo in morse_code:
                texto += morse_code[codigo]
        return texto