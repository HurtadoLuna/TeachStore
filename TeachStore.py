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
  print("   \n ¡Has ingresado a la pagina! :)")  #Puede ingresar correctamente a la pagina.

#--------------------------------------- CATALOGO DE PRODUCTOS -----------------------------------
  productos = [   #Se crea una lista con los productos disponibles.
       ("Audífonos", 45000),
       ("Mouse inalámbrico", 38000),
       ("Teclado gamer", 95000),
       ("Memoria USB 32GB", 25000),
       ( "Cargador portátil", 67000) ]
  print (" \n ESTOS SON NUESTROS PRODUCTOS DISPONIBLES")  #Mostrar los productos disponibles.

# Recorrer la lista de productos con enumerate() para obtener
# tanto el índice (posición) como el contenido (nombre y precio).
# Se inicia en 1 para numerar los productos desde el 1 en lugar de 0.
  for i, producto in enumerate(productos, start=1):
        print(f"{i}. {producto[0]} - ${producto[1]}")

#---------------------------------------CARRITO DE COMPRAS --------------------------------------
        carrito = []  #Se crea una lista vacia donde se agregaran los productos seleccionados por el usuario.

  while True:
       opcion = int(input("\n Ingrese el número del producto para agregar al carrito (0 para terminar): "))  #Se solicita al usuario ingresar el numero de los productos que desea agregar. Se usa el cero para terminar la seleccion.

       if opcion == 0:   #Si el usuario ingresa 0, ropmpe el ciclo y deja de pedir productos.
      
          break
      
       if 1 <= opcion <= len(productos):   #Revisa si la opcion esta dentro del rango de productos disponibles.
          producto= productos[opcion - 1]  #Se resta uno por que las listas en pyton inician en indice 0.
          carrito.append(producto)  #Se agrega el producto seleccionado a la lista.
          print(f"El producto '{producto[0]}' ha sido agregado al carrito") #Se le muestra un mensaje de confirmacion al usuario.
          
       else:  #Si la opcion no es valida le pide al usuario que intente de nuevo.
          print("Opcion invalida, intentalo de nuevo")
  print(f" \n Este es su carrito de compras \n {carrito}") #Muestra el contenido del varito al usuario.
  


#-----------------------------------------CARRITO PAGAR-----------------------------------

  print ("\n=== CARRITO ===") 
  total = 0  #Se inicia en cero para ir acumulando el total de la compra.

  for producto in carrito:  #Recorre todos los productos que el usuario seleciono en el carrito.
   print(f"- {producto[0]}: ${producto[1]}")  #Muestra el nombre y precio de cada producto.
  
#------------------------------------------------METODOS DE PAGO-------------------------------------------------

print("\n ===METODOS DE PAGO===")

#Diccionario con los metodos de pago disponibles
pago={
    "1":"BANCOLOMBIA",
    "2":"NEQUI",
    "3":"DAVIPLATA",
    "4":"PAYPAL",
    "5":"APPLE PAY",
    "6":"SALIR"
   }

# Se crea un bucle para solicitar el método de pago hasta que el usuario elija uno válido
while True: 
    #Mostrar los metodos de pago dispponibles.
    for clave,valor in pago.items():
        print(f"[{clave}] {valor}")

    metodos_de_pago=input("\n Ingrese un metodo de pago: ")  #Solicitar al usuario que seleccione un metodo de pago.

    if metodos_de_pago in pago:  #Valida si la opcion esta dentro del diccionario.
        if metodos_de_pago == 6:  #Si selecciona la opcion 6 sale del ciclo.
            break
        else:
            #Confirma el metodo de pago elegido
            print(f"Has elegido {pago[metodos_de_pago]}\n")
            break
    else: 
        #Si la opcion no existe, pedirle al usuario que intente de nuevo.
        print("Opción o valida, intenta de nuevo")

#------------------------------------------------FACTURA DE COMPRA-------------------------------------------------
print ("\n=== FACTURA ===")

#Librerias
from datetime import datetime  # Para obtener fecha y hora actual
import random   # Para generar números aleatorios (factura y pedido)

#Datos de la factura 
fecha_factura = datetime.now().strftime("%d/%m/%Y %H:%M:%S")  # Fecha y hora actual
no_factura = random.randint(1000, 9999)   # Número de factura generado aleatoriamente
no_pedido = random.randint(5000, 9999)    # Número de pedido generado aleatoriamente

# Solicitar datos de envío al usuario
print("\n--- Datos de Envío ---")
enviar_a = {
    "nombre": input("Nombre del destinatario: "),
    "direccion": input("Dirección de envío: "),
    "ciudad": input("Ciudad: "),
    "telefono": input("Teléfono: ")
}

# Solicitar datos de facturación al usuario
print("\n--- Datos de Facturación ---")
facturar_a = {
    "nombre": input("Nombre del comprador: "),
    "telefono": input("Teléfono: "),
    "direccion": input("Dirección: ")
}

total = 0  #Se inicia en cero para ir acumulando el total de los productos.

for producto in carrito:   #Recorre todos los productos que el usuario seleciono en el carrito.
   print(f"- {producto[0]}: ${producto[1]}")  #Muestra el nombre y precio de cada producto.
total += producto[1]  # Sumar el precio al total

iva = 0.19 * total  #Se calcula el IVA (19% en este caso).
precio_iva = total + iva   #Precio final con IVA incluido.

# Mostrar los detalles principales de la factura
print("\n--- Detalles de Factura ---")
print(f"No. Factura: {no_factura}")
print(f"Fecha: {fecha_factura}")
print(f"No. Pedido: {no_pedido}")

#Se muestra detalles de la factura
print(f"\nSubtotal: ${total}")  
print(f"IVA (19%): ${iva}")
print(f"Total a pagar: ${precio_iva}")

# Mostrar información de envío
print("\n--- ENVIAR A ---")
print(f"Nombre: {enviar_a['nombre']}")
print(f"Dirección: {enviar_a['direccion']}")
print(f"Ciudad: {enviar_a['ciudad']}")
print(f"Teléfono: {enviar_a['telefono']}")

# Mostrar información de facturación
print("\n--- FACTURAR A ---")
print(f"Nombre: {facturar_a['nombre']}")
print(f"Teléfono: {facturar_a['telefono']}")
print(f"Dirección: {facturar_a['direccion']}")

#Mostrar el metodo de pago selecionado
print(f"pago por: {pago[metodos_de_pago]}\n")

print("Gracias por su compra")
