# Inicio de sesion

informacion=([])  #La informacion de registro se agrega a informacion.
print("\n BIENVENIDO A TECHSTORE " )  #Print de bienvenido a la pagina,
registro= input( "¿Ya te has registrado en nuestra pagina? \n -")  #Pregunta si ya esta registrado, si no, pide los datos.

while registro.lower() == "no":   #NO, el programa pide los datos para ser registrado.
        print("REGISTRATE AQUI:")
        nombre=input("Ingrese su  nombre: ")
        apellido=input("Ingrese su apellido: ")
        correo1= input("Por favor ingrese su correo electronico: ")
        nombre_usuario=input("Ingrese su  nombre de usuario: ")
        contraseña1= input("Por favor ingrese su contraseña: ")
        edad= int(input("Ingrese su edad: "))

        
        informacion.append(nombre)
        informacion.append(apellido)
        informacion.append(correo1)   #Se agregan los datos del usuario a la lista
        informacion.append(contraseña1)
        informacion.append(edad)
        informacion.append(nombre_usuario)

        if edad >= 18:   #Si es maypr de edad ´puede ingresar, si no, no puede ingresar
            print(" \n YA ESTAS REGISTRADO!! \n ya puedes mirar nuestros productos")
        else:
               print("No puedes registrarte debido a que eres menor de edad")

               break   #Se termina el ciclo
        
if registro.lower() == "si":   #SI, ya esta registrado ingresa su correo y contraseña.
  correo= input("Por favor ingrese su correo electronico: ")
  contraseña= input("Por favor ingrese su contraseña: ")
  print("   \n ¡Has ingresado a la pagina! :)")  #Puede ingresar correctamente a la pagina

#--------------------------------------- CATALOGO DE PRODUCTOS -----------------------------------
  productos = [
       ("Audífonos", 45000),
       ("Mouse inalámbrico", 38000),
       ("Teclado gamer", 95000),
       ("Memoria USB 32GB", 25000),
       ( "Cargador portátil", 67000) ]
  print (" \n ESTOS SON NUESTROS PRODUCTOS DISPONIBLES")
  for i, producto in enumerate(productos, start=1):
        print(f"{i}. {producto[0]} - ${producto[1]}")

#---------------------------------------CARRITO DE COMPRAS --------------------------------------
        carrito = []

  while True:
       opcion = int(input("\n Ingrese el número del producto para agregar al carrito (0 para terminar): "))

       if opcion == 0:
      
          break
      
       if 1 <= opcion <= len(productos):
          producto= productos[opcion - 1]
          carrito.append(producto)
          print(f"El producto '{producto[0]}' ha sido agregado al carrito")
          
       else:
          print("Opcion invalida, intentalo de nuevo")
  print(f" \n Este es su carrito de compras \n {carrito}")
  dirección=input("\n Ingrese la dirección donde llegara su pedido: ")


#-----------------------------------------CARRITO PAGAR-----------------------------------

  print ("\n=== CARRITO ===")
  total = 0

  for producto in carrito:
   print(f"- {producto[0]}: ${producto[1]}")
  

#------------------------------------------------FACTURA DE COMPRA-------------------------------------------------
  print ("\n=== FACTURA ===")
  total = 0

  for producto in carrito:
   print(f"- {producto[0]}: ${producto[1]}")
  total += producto[1]

  iva = 0.19 * total
  precio_iva = total + iva

  print(f"\nSubtotal: ${total}")
  print(f"IVA (19%): ${iva}")
  print(f"Total a pagar: ${precio_iva}")

  print(f"\nla direccion donde llegara su pedido es: {dirección}")


#------------------------------------------------METODOS DE PAGO-------------------------------------------------

  print("\n ===METODOS DE PAGO===")

  pago={
    "1":"BANCOLOMBIA",
    "2":"NEQUI",
    "3":"DAVIPLATA",
    "4":"PAYPAL",
    "5":"APPLE PAY",
    "6":"SALIR"
   }

  while True: 
    for clave,valor in pago.items():
        print(f"[{clave}] {valor}")
    metodos_de_pago=input("\n Ingrese un metodo de pago: ")
    if metodos_de_pago in pago:
        if metodos_de_pago == 6:
            break
        else:
            print(f"Has elegido {pago[metodos_de_pago]}\n")
            break
    else: 
        print("Opción o valida, intenta de nuevo")



