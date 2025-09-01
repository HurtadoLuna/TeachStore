# Inicio de sesion

informacion=([])  #La informacion de registro se agrega a informacion.
print("\n BIENVENIDO A STECHSTORE " )  #Print de bienvenido a la pagina,
registro= input( "Ya te has registrado en nuestra pagina: ")  #Pregunta si ya esta registrado, si no, pide los datos.

while registro.lower() == "no":   #NO, el programa pide los datos para ser registrado.
        nombre=input("Ingrese su  nombre")
        apellido=input("Ingrese su apellido")
        correo1= input("Por favor ingrese su correo electronico: ")
        contraseña1= input("Por favor ingrese su contraseña ")
        edad= int(input("Ingrese su edad: "))
        
        informacion.append(nombre)
        informacion.append(apellido)
        informacion.append(correo1)   #Se agregan los datos del usuario a la lista
        informacion.append(contraseña1)
        informacion.append(edad)

        if edad >= 18:   #Si es maypr de edad ´puede ingresar, si no, no puede ingresar
            print(" \n YA ESTAS REGISTRADO!! \n ya puedes mirar nuestros productos")
        else:
               print("No puedes registrarte debido a que eres menor de edad")
               
        break   #Se termina el ciclo
if registro.lower() == "si":   #SI, ya esta registrado ingresa su correo y contraseña.
        correo= input("Por favor ingrese su correo electronico: ")
        contraseña= input("Por favor ingrese su contraseña ")
        print("Has ingresado a la pagina")  #Puede ingresar conrrectamente a al pagina
        



        
       


   


