def adivinar_numero(n):
  inicio = 1
  fin = float('inf')

  while True:
      numero_propuesto = (inicio + fin) // 2
      respuesta = input(f"¿Tu número es {numero_propuesto} ? Responde 'mayor', 'menor' o 'igual': ").lower()

      if respuesta in {'mayor', 'menor', 'igual'}:
          if respuesta == 'mayor':
              fin = numero_propuesto - 1
          elif respuesta == 'menor':
              inicio = numero_propuesto + 1
          else:
              print(f"Tu número es {numero_propuesto}.")
              break
      else:
          print("Respuesta invalida. Por favor, responde 'mayor', 'menor' o 'igual'.")

# Ejemplo de uso
try:
  numero_pensado = int(input("Piensa en un número natural: "))
  adivinar_numero(numero_pensado)
except ValueError:
  print("Ingresa un número válido.")
