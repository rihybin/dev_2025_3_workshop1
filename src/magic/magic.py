import math

class Magic:
    """
    Clase con métodos para juegos matemáticos, secuencias especiales y algoritmos numéricos.
    Incluye implementaciones de Fibonacci, números perfectos, triangulo de pascal etc.
    """
    
    def fibonacci(self, n):
        """
        Calcula el n-ésimo número de la secuencia de Fibonacci.
        
        """
        if n < 0:
            return None
        if n <= 1:
            return n
        
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
    
    def secuencia_fibonacci(self, n):
        """
        Genera los primeros n números de la secuencia de Fibonacci.
        
        """
        if n <= 0:
            return []
        if n == 1:
            return [0]
        
        secuencia = [0, 1]
        while len(secuencia) < n:
            siguiente = secuencia[-1] + secuencia[-2]
            secuencia.append(siguiente)
        return secuencia
    
    def es_primo(self, n):
        """
        Verifica si un número es primo.
        
        """
        if n <= 1:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    
    def generar_primos(self, n):
        """
        Genera una lista de números primos hasta n.
        
        """
        primos = []
        for numero in range(2, n + 1):
            if self.es_primo(numero):
                primos.append(numero)
        return primos
    
    def es_numero_perfecto(self, n):
        """
        Verifica si un número es perfecto (igual a la suma de sus divisores propios).
        
        """
        if n <= 1:
            return False
        
        suma_divisores = 1
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                suma_divisores += i
                if i * i != n:
                    suma_divisores += n // i
        
        return suma_divisores == n
    
    def triangulo_pascal(self, filas):
        """
        Genera las primeras n filas del triángulo de Pascal.
        
        """
        if filas <= 0:
            return []
        
        triangulo = [[1]]
        for i in range(1, filas):
            fila_anterior = triangulo[-1]
            nueva_fila = [1]
            for j in range(1, i):
                nueva_fila.append(fila_anterior[j - 1] + fila_anterior[j])
            nueva_fila.append(1)
            triangulo.append(nueva_fila)
        return triangulo
    
    def factorial(self, n):
        """
        Calcula el factorial de un número.
     
        """
        if n < 0:
            return None
        if n == 0:
            return 1
        
        resultado = 1
        for i in range(1, n + 1):
            resultado *= i
        return resultado
    
    def mcd(self, a, b):
        """
        Calcula el máximo común divisor de dos números.
        
        """
        while b:
            a, b = b, a % b
        return abs(a)
    
    def mcm(self, a, b):
        """
        Calcula el mínimo común múltiplo de dos números.
        
        """
        if a == 0 or b == 0:
            return 0
        return abs(a * b) // self.mcd(a, b)
    
    def suma_digitos(self, n):
        """
        Calcula la suma de los dígitos de un número.
        
        """
        suma = 0
        num_str = str(abs(n))
        for digito in num_str:
            suma += int(digito)
        return suma
    
    def es_numero_armstrong(self, n):
        """
        Verifica si un número es de Armstrong (igual a la suma de sus dígitos elevados a la potencia del número de dígitos).
        
        """
        if n < 0:
            return False
            
        num_str = str(n)
        potencia = len(num_str)
        suma_de_potencias = sum(int(digito) ** potencia for digito in num_str)
        return suma_de_potencias == n
    
    def es_cuadrado_magico(self, matriz):
        """
        Verifica si una matriz es un cuadrado mágico (suma igual en filas, columnas y diagonales).
        
        """
        n = len(matriz)
        if not all(len(fila) == n for fila in matriz):
            return False
            
        suma_magica = sum(matriz[0])
        
        # Verificar filas y columnas
        for i in range(n):
            if sum(matriz[i]) != suma_magica:
                return False
            if sum(matriz[j][i] for j in range(n)) != suma_magica:
                return False
        
        # Verificar diagonales
        suma_diag1 = sum(matriz[i][i] for i in range(n))
        if suma_diag1 != suma_magica:
            return False
            
        suma_diag2 = sum(matriz[i][n - i - 1] for i in range(n))
        if suma_diag2 != suma_magica:
            return False
            
        return True