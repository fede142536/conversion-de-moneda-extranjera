# Creacion del menu de compra venta de moneda extranjera
class main():
  while True:
    print("\nMenu de compra/venta de mondeda extranjera.")
    print("1. Compra/Venta - Ingrese la operacion a realizar")
    print("2. Salir")

    # seleccionar en el menú la opción de compra o venta
    operacion = input("Ingrese la operacion a realizar: Compra/Venta/Salir ")

    if operacion == "compra":
      #Ingresar la cotizacion del dolar para la compra
      usd_compra = float(input("Ingrese la cotizacion actual del USD en pesos ARS: $"))
      #Ingresar los pesos o usd a convertir
      peso_compra = float(input("Ingrese la cantidad ARS que quiere convertir a USD: $"))
      conversion_compra = peso_compra / usd_compra
      print("Usted a convertido $", peso, "a ", conversion_compra, "usd")
    elif  operacion == "venta":
      #Ingresar la cotizacion del dolar para la venta
      usd_venta = float(input("Ingrese la cotizacion actual del USD en pesos ARS: $"))
      peso_venta = float(input("Ingrese la cantidad de dólares a vender: Usd"))
      conversion_venta = usd_venta * peso_venta
      print("Usted a convertido ", usd_venta, "a $", conversion_venta)
    elif operacion == "salir":
      print("Gracias por usar nuestro programa")
      break
    else:
      print("Opcion no valida")
if __name__ == "__main__":
    main()