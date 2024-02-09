import unittest

# Función para calcular el factorial de un número
def factorial(n):
    if n == 0:
        return 1
    elif n < 0:
        return None
    else:
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        return fact

# Clase de pruebas para la función factorial
class TestFactorial(unittest.TestCase):
    
    # Prueba para el factorial de 0
    def test_factorial_cero(self):
        self.assertEqual(factorial(0), 1)
        
    # Prueba para el factorial de un número positivo
    def test_factorial_positivo(self):
        self.assertEqual(factorial(5), 120)
        
    # Prueba para el factorial de un número negativo
    def test_factorial_negativo(self):
        self.assertIsNone(factorial(-3))

# Si se ejecuta este script directamente, ejecutar las pruebas
if __name__ == '__main__':
    unittest.main()
