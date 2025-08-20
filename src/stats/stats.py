import math
from collections import Counter

class Stats:
    def promedio(self, numeros):
        """
        Calcula la media aritmética de una lista de números.
        
        """
        if not numeros:
            return 0.0
        return sum(numeros) / len(numeros)

    def mediana(self, numeros):
        """
        Encuentra el valor mediano de una lista de números.
        Para listas con número par de elementos, retorna el promedio de los dos valores centrales.
        
        """
        if not numeros:
            return 0.0
            
        numeros_ordenados = sorted(numeros)
        n = len(numeros_ordenados)
        indice_medio = n // 2
        
        if n % 2 == 1:
            # Si la lista tiene un número impar de elementos, retorna el valor del medio.
            return float(numeros_ordenados[indice_medio])
        else:
            # Si la lista tiene un número par de elementos, retorna el promedio de los dos valores centrales.
            return (numeros_ordenados[indice_medio - 1] + numeros_ordenados[indice_medio]) / 2.0

    def moda(self, numeros):
        """
        Encuentra el valor que aparece con mayor frecuencia en la lista.
        Si hay empate, retorna el primer valor encontrado.
        
        """
        if not numeros:
            return None
            
        conteo = Counter(numeros)
        moda_valor = None
        max_frecuencia = 0
    
        for valor, frecuencia in conteo.items():
            if frecuencia > max_frecuencia:
                max_frecuencia = frecuencia
                moda_valor = valor
        
        return moda_valor

    def desviacion_estandar(self, numeros):
        """
        Calcula la desviación estándar de una lista de números.
        Usa la fórmula de desviación estándar poblacional.
        
        """
        if len(numeros) < 2:
            return 0.0
            
        media = self.promedio(numeros)
        varianza = sum([(x - media) ** 2 for x in numeros]) / len(numeros)
        return math.sqrt(varianza)

    def varianza(self, numeros):
        """
        Calcula la varianza de una lista de números.
        La varianza es el cuadrado de la desviación estándar.
        
        """
        if len(numeros) < 2:
            return 0.0
            
        media = self.promedio(numeros)
        return sum([(x - media) ** 2 for x in numeros]) / len(numeros)

    def rango(self, numeros):
        """
        Calcula el rango (diferencia entre el valor máximo y mínimo).
        
        """
        if not numeros:
            return 0
        
        return max(numeros) - min(numeros)