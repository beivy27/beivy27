def calcular_descuento(monto_total, porcentaje_descuento=10):
  """
  Calcula el descuento sobre un monto total dado un porcentaje de descuento.

  Args:
    monto_total: El monto total de la compra.
    porcentaje_descuento: El porcentaje de descuento a aplicar. Por defecto es 10%.

  Returns:
    El monto del descuento.
  """

  # Convertir el porcentaje a un decimal
  descuento_decimal = porcentaje_descuento / 100

  # Calcular el descuento
  descuento = monto_total * descuento_decimal

  return descuento

# Llamadas a la función

# Primera llamada: Usando el valor por defecto del descuento (10%)
monto_compra1 = 100
descuento1 = calcular_descuento(monto_compra1)
monto_final1 = monto_compra1 - descuento1
print("Descuento 1: ", descuento1)
print("Monto final 1: ", monto_final1)

# Segunda llamada: Especificando un porcentaje de descuento diferente
monto_compra2 = 200
descuento2 = calcular_descuento(monto_compra2, 15)
monto_final2 = monto_compra2 - descuento2
print("Descuento 2: ", descuento2)
print("Monto final 2: ", monto_final2)