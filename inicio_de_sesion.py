# Inicio de sesion

# informacion=([])  #La informacion de registro se agrega a informacion.
# print("\n BIENVENIDO A TECHSTORE " )  #Print de bienvenido a la pagina,
# registro= input( "Ya te has registrado en nuestra pagina: ")  #Pregunta si ya esta registrado, si no, pide los datos.

# while registro.lower() == "no":   #NO, el programa pide los datos para ser registrado.
#         nombre_usuario=input("Ingrese su  nombre: ")
#         apellido=input("Ingrese su apellido: ")
#         correo1= input("Por favor ingrese su correo electronico: ")
#         contraseña1= input("Por favor ingrese su contraseña ")
#         edad= int(input("Ingrese su edad: "))
        
#         informacion.append(nombre_usuario)
#         informacion.append(apellido)
#         informacion.append(correo1)   #Se agregan los datos del usuario a la lista
#         informacion.append(contraseña1)
#         informacion.append(edad)

#         if edad >= 18:   #Si es maypr de edad ´puede ingresar, si no, no puede ingresar
#             print(" \n YA ESTAS REGISTRADO!! \n ya puedes mirar nuestros productos")
#         else:
#                print("No puedes registrarte debido a que eres menor de edad")
               
#         break   #Se termina el ciclo
# if registro.lower() == "si":   #SI, ya esta registrado ingresa su correo y contraseña.
#         correo= input("Por favor ingrese su correo electronico: ")
#         contraseña= input("Por favor ingrese su contraseña ")
#         print("Has ingresado a la pagina")  #Puede ingresar correctamente a la pagina

# ---------------------------------------CATALOGO DE PRODUCTOS---------------------------------

productos = [
("Audífonos", 45000),
("Mouse inalámbrico", 38000),
("Teclado gamer", 95000),
("Memoria USB 32GB", 25000),
("Cargador portátil", 67000)
]

# ---------------------------------------CARRITO DE COMPRAS --------------------------------------

carrito = []

print ("\n=== CARRITO ===")
total = 0

for producto in carrito:
    print(f"- {producto[0]}: ${producto[1]}")
    total += producto[1]

iva = 0.19 * total
precio_iva = total + iva

print(f"\nSubtotal: ${total}")
print(f"IVA (19%): ${iva}")
print(f"Total a pagar: ${precio_iva}")



# #-----------------------------------------CARRITO DE COMPRAS-----------------------------------

# while True:
#  opcion = input("\nIngrese el número del producto para agregar al carrito (0 para terminar): ")

#  if opcion == "0":
#   break
#  if opcion == "1":
#   carrito.append(productos[0])
#   print(f" {productos[0][0]} agregado al carrito por ${productos[0][1]}")
#  elif opcion == "2":
#   carrito.append(productos[1])
#   print(f" {productos[1][0]} agregado al carrito por ${productos[1][1]}")
#  elif opcion == "3":
#   carrito.append(productos[2])
#   print(f" {productos[2][0]} agregado al carrito por ${productos[2][1]}")
#  elif opcion == "4":
#   carrito.append(productos[3])
#   print(f" {productos[3][0]} agregado al carrito por ${productos[3][1]}")
#  elif opcion == "5":
#   carrito.append(productos[4])
#   print(f" {productos[4][0]} agregado al carrito por ${productos[4][1]}")
#  else:
#   print(" Opción inválida.")


# print("\n=== CARRITO ===")
# total = 0
# if len(carrito) > 0:
#  if len(carrito) >= 1:
#   print(f"- {carrito[0][0]}: ${carrito[0][1]}")
#  total += carrito[0][1]
# if len(carrito) >= 2:
#  print(f"- {carrito[1][0]}: ${carrito[1][1]}")
#  total += carrito[1][1]
# if len(carrito) >= 3:
#  print(f"- {carrito[2][0]}: ${carrito[2][1]}")
#  total += carrito[2][1]
# if len(carrito) >= 4:
#  print(f"- {carrito[3][0]}: ${carrito[3][1]}")
#  total += carrito[3][1]
# if len(carrito) >= 5:
#  print(f"- {carrito[4][0]}: ${carrito[4][1]}")
#  total += carrito[4][1]
# precio_iva= (0.19 *  total) + total 
# iva=0.19 *  total
# print(f" \n Total original: $ {carrito}")
# print(f" \n IVA: {iva}")
# print(f"\n Total a pagar (+IVA DEL 19%): ${precio_iva}")


#--------------------------------------------------------FACTURA DE COMPRA-----------------------------------------1