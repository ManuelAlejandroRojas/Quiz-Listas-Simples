"""El director de un hotel desea implementar una sistema de administración para saber la disponibilidad y asignación de habitaciones. Para asignar, registra el número de cédula y el nombre de cada cliente a medida que llega al hotel, junto con el número de habitación que ocupa (el antiguo libro de entradas).
Igualmente cuando un huésped se retira del hotel se actualiza la disponibilidad de las habitaciones, el libro de entradas y el libro de salida. El director desea en un momento dado contar con la siguiente información: Consultas vigentes por huésped: (1) Individual y (2) total. Las consultas (2) totales pueden ser: (1) Por cédula y (2) por orden de llegada.
Para cualquiera de las consultas entregar toda la información asociada al huésped. Consulta de habitaciones: (1) Lista de habitaciones disponibles y (2) Lista de habitaciones ocupadas."""

# Clase Nodo
class Nodo:
    def __init__(self, data):
        self.data = data
        self.siguiente = None

# CLase Listas enlazada simple
class ListaSE:
    def __init__(self):
        self.cabeza = None

# Agregar al inicio
    def agregarInicio(self, data):
        nuevo_nodo = Nodo(data)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            return
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo

    #Contar cuantos elementos tiene la lista
    def Contar_cuantos_elementos_tiene_la_lista(self):
        CantidadElementos = 0
        NodoActual = self.cabeza
        while NodoActual != None:
            CantidadElementos+=1
            NodoActual = NodoActual.siguiente
        
        print("hay ", CantidadElementos, " elementos en la lista")


    #Encontrar un elemento por su valor
    def Buscar_si_hay_un_elemento(self, valor):
        NodoActual = self.cabeza
        while NodoActual is not None:
            if NodoActual.data == valor:
                print("El elemento si está en la lista")
                return True
            
            else: 
                NodoActual = NodoActual.siguiente	

        
        print("El valor no está en la lista")
        return False
    
    def Cambiar_estado_habitacion(self, NumeroAsignado):
        NodoActual = self.cabeza         #Si está desocupada se asigna
        while NodoActual is not None:
            if NodoActual.data.estado == False and NodoActual.data.numero_habitacion == NumeroAsignado:
                NodoActual.data.estado = True  #Cambia el estado de "no" a "si" (la pregunta)
                print("El estado de la habitación a cambiado correctamente, asignando huesped ingresado...")
                return
            
            elif NodoActual.data.estado == True and NodoActual.data.numero_habitacion == NumeroAsignado: #Si está ocupada, no se asigna.
                print("La habitación ya está ocupada, por favor elija otra habitación")
                return
            
            else:
                NodoActual = NodoActual.siguiente
    
    def Esta_ocupada_la_habitacion(self, NumeroAsignado):
        NodoActual = self.cabeza         #Si está desocupada se asigna
        while NodoActual is not None:
            if NodoActual.data.estado == False and NodoActual.data.numero_habitacion == NumeroAsignado:
                #no cambio el estado, solo verifico que esté desocupada para asignar ya en el programa.
    
                return False #Devuelvo False para ser coherente con la respuesta a la preguinta "Está ocupada la habitación?" False -> no, True -> si           
            
            elif NodoActual.data.estado == True and NodoActual.data.numero_habitacion == NumeroAsignado: #Si está ocupada, no se asigna.
                print("La habitación ya está ocupada, por favor elija otra habitación")
                
                return True #Devuelvo True por que esta funcion ES la pregunta
                            #El return es la RESPUESTA a la pregunta
            
            else:
                NodoActual = NodoActual.siguiente
      
    
    def Buscar_por_numero_de_habitacion(self, NumeroAsignado):
        NodoActual = self.cabeza
        while NodoActual is not None:
            if NodoActual.data.numero_habitacion == NumeroAsignado:
                print("La habitación si está en la lista")
                return True
            
            else: 
                NodoActual = NodoActual.siguiente	

        
        print("El número de habitación no está en la lista, por favor elija otro número de habitación")
        return False
        
                
            
    #Eliminar el último elemento de la lista
    def Eliminar_ultimo_elemento(self):
        NodoActual = self.cabeza

        if NodoActual == None:
            print("La lista está vacía, no se puede eliminar nada")   #Comprobar lista vacía(Por si acaso xd)
            return


        elif NodoActual.siguiente == None:   #Si la lista tiene un solo elemento lo elimino y queda vacía
            self.cabeza = None
            print("Se eliminó el único elemento, la lista quedó vacía")

            return

        while NodoActual.siguiente.siguiente != None: #Busco el siguiente del siguiente pa llegar al penúltimo
            NodoActual = NodoActual.siguiente     #Avanzo uno

        NodoActual.siguiente = None   #Le cambio el apuntador del penúltimo a nada y el último desaparece mujejeje
        print("Se eliminó el último elemento de la lista")

    #Eliminar el primer elemento de la lista ---> Pero sin que se borre toda la lista, claro JAJAJA
    def Eliminar_primer_elemento(self):
        
        if self.cabeza is None:
            print("Lista vacía")
            return
        
        self.cabeza = self.cabeza.siguiente  #Reemplazo lo que hay actualmente en la cabeza por lo que hay en el apuntador de la misma, el primero, desaparece
        print("Se eliminó el primer elemento de la lista")

    #Insertar un elemento después de un elemento random
    def Insertar_despues_de_un_elemento_especifico(self, ValorAgregar, valorX):
        
        Nodo_a_insertar = Nodo(ValorAgregar)

        NodoActual = self.cabeza
        if NodoActual is not None:
            while True:
                if NodoActual is None:
                    print("El valor no se encuentra en la lista")
                    return			

                if NodoActual.data == valorX:
                    Nodo_a_insertar.siguiente = NodoActual.siguiente
                    NodoActual.siguiente = Nodo_a_insertar
                    break
                else:	
                    NodoActual = NodoActual.siguiente
            
            print("Se insertó: '", ValorAgregar, "' después del elemento: ", valorX)
        else:
            print("Lista vacía")
            return
            

    #Insertar antes de un elemento random
    def Insertar_antes_de_un_elemento_especifico(self, ValorAgregar, ValorX):

        if self.cabeza is None: #Comprobar si la lista está vacía
            print("Lista vacía")
            return


        if self.cabeza.data == ValorX:      #En caso de insertar antes del primero
            self.agregarInicio(ValorAgregar)
            print("Se insertó: '", ValorAgregar, "' antes del elemento: ", ValorX)
            return

        NodoActual = self.cabeza

        while NodoActual.siguiente is not None:

            if NodoActual.siguiente.data == ValorX:
                Nodo_a_insertar = Nodo(ValorAgregar)
                Nodo_a_insertar.siguiente = NodoActual.siguiente
                NodoActual.siguiente = Nodo_a_insertar

                print("Se insertó: '", ValorAgregar, "' antes del elemento:", ValorX)
                return
            else:
                NodoActual = NodoActual.siguiente
            
        print("El valor no se encuentra en la lista")


    def Insertar_al_final(self, ValorAgregar):
        Nodo_a_insertar = Nodo(ValorAgregar)
        if self.cabeza is None:
            self.cabeza = Nodo_a_insertar
            print("Se insertó:", ValorAgregar, "al final de la lista")
            return
        
        
        NodoActual = self.cabeza
        while NodoActual.siguiente is not None:
            NodoActual = NodoActual.siguiente

        NodoActual.siguiente = Nodo_a_insertar
        print("Se insertó:", ValorAgregar, "al final de la lista")


    def mostrar_lista(self):
        NodoActual = self.cabeza
        while NodoActual is not None:
            print("--", NodoActual.data)
            NodoActual = NodoActual.siguiente
        print("None")
        


#Defino un objeto habitación para saber si número y estado.
class habitacion:
    def __init__(self, NumeroAsignado, huesped):
        self.numero_habitacion = NumeroAsignado  #Mientras no haya numero asignado, será 0 al crear las habitaciones
        self.estado = False           #True es ocupado, responde a la pregunta "Está ocupada la habitación?" True-> si --- False --> no
        self.huesped = huesped        #Mientras no haya un huésped asignado, será None al crear las habitaciones
        
        
#Ahora definiré un objeto huésped para saber su nombre, cédula, fecha de ingreso(o salida) y habitación asignada
class persona:
    def __init__(self, nombre, cedula, fecha_ingreso):
        self.nombre = nombre
        self.cedula = cedula
        self.fecha_ingreso = fecha_ingreso
        
        


#########################
#CREACIÓN DE LISTA DE HABITACIONES
#########################

ListaHabitaciones = ListaSE()



def Crear_Habitaciones():
    try:
        print("\t===CONFIGURACIÓN DEL SISTEMA DE ASIGNACIÓN DE HABITACIONES===")
        Numero_pisos = int(input("Ingrese cuantos pisos tiene el hotel"\
            "\nTome en cuenta que 1 es considerada la planta más baja: "))
        Habitaciones_por_piso = int(input("\nIngrese cuantas habitaciones hay por cada piso: "))
    
    except ValueError:
        print("Por favor, ingrese un número válido")
        #Ahora se vuelve a llamar a la función para que el usuario pueda ingresar los datos correctamente
        Crear_Habitaciones()
        return    
    
    if Numero_pisos <= 0 or Habitaciones_por_piso <= 0:
        print("Por favor, ingrese un número mayor a 0")
        Crear_Habitaciones()
        return
        
    for i in range(1, Numero_pisos+1):
        for j in range(1, Habitaciones_por_piso+1):
            Habitacion = habitacion(0, None) #Creo la habitación con número 0 y sin huésped asignado
            Habitacion.numero_habitacion = (i*100) + j #Aqui se asigna el numero de habitación
            
            ListaHabitaciones.agregarInicio(Habitacion)
            
    print("Se han creado las habitaciones correctamente")
    
#Para testeo de habitaciones creadas...
"""Crear_Habitaciones()           
#Compruebo que se crean las habitaciones correctamente mostrando la lista de habitaciones
NodoActual = ListaHabitaciones.cabeza
while NodoActual is not None:
    print("Número de habitación: ", NodoActual.data.numero_habitacion, "Estado: ", NodoActual.data.estado)
    NodoActual = NodoActual.siguiente
    """
    
#Recuerda que el plan ahora es asignarle a la habitacion un self.huesped y no a la persona una habitación.
#De hecho creo que solo necesito una lista para las habitaciones y ya.

"""Inicio del programa"""
Crear_Habitaciones()


while True:
    print("\t===SISTEMA DE ASIGNACIÓN DE HABITACIONES===\n")
    print("1. Asignar habitación a huésped")
    print("2. Retirar huésped y actualizar disponibilidad")
    print("3. Consultar individual de huesped por cédula")
    print("4. Consultar huéspedes por orden de llegada")
    print("5. Consultar habitaciones disponibles")
    print("6. Consultar habitaciones ocupadas")
    print("7. Salir")

    opcion = input("Seleccione una opción: ")

    match opcion:
        case "1":
            print("\t===ASIGNAR HABITACIÓN A HUÉSPED===\n")
            nombre = input("Ingrese el nombre del huésped: ")
                
            try:
                cedula = int(input("Ingrese la cédula del huésped: "))
            
            except ValueError:
                print("Ingrese un número entero")
                continue
            
            if cedula <= 0:
                print("Ingrese un número mayor a 0")
                continue    
                
                
            fecha_ingreso = input("Ingrese la fecha de ingreso del huésped (dd/mm/yyyy): ")
            Nuevo_huesped = persona(nombre, cedula, fecha_ingreso)
            
            try:
                Numero_asignado = int(input("Ingrese el número de habitación que desea asignarle: "))
            
            except ValueError:
                print("Ingrese un número entero")
                continue
            
            if Numero_asignado <= 0:
                print("Ingrese un número mayor a 0")
                continue
            
            
            
            
            #Si el numero de habitacion existe en la lista, se verifica su estado, si no existe, se devuelve al while y se muestra el menú de nuevo.
            #Si existe y está ocupada, se muestra un mensaje y se devuelve al menu de nuevo.
            if ListaHabitaciones.Buscar_por_numero_de_habitacion(Numero_asignado) == True:
                print("Verificando estado...")
                if ListaHabitaciones.Esta_ocupada_la_habitacion(Numero_asignado) == False: #Si la habitacion no está ocupada (Osea False)
                    ListaHabitaciones.Cambiar_estado_habitacion(Numero_asignado) #Cambio el estado de la habitación a ocupada

                    
                    #ahora recorro la lista para llegar a la habitacion a asignar
                    NodoActual = ListaHabitaciones.cabeza
                    while NodoActual is not None:
                        if NodoActual.data.numero_habitacion == Numero_asignado:
                            NodoActual.data.huesped = Nuevo_huesped #Asigno el huesped a la habitacion
                            break
                        else:
                            NodoActual = NodoActual.siguiente
                    print("Habitación asignada correctamente")
                    
                else:
                    print("Volviendo al menú principal...")
                    #continue para volver al menú principal
                    continue
            else:
                print("Volviendo al menú principal...")
                continue
            
            #La opcion 1 ya está completa, ahora se muestra el menú de nuevo
            print("Volviendo al menú principal...")
            continue
        
        
        case "2":
            print("\t===RETIRAR HUÉSPED Y ACTUALIZAR DISPONIBILIDAD===\n")
            try:
                Numero_asignado = int(input("Ingrese el número de habitación que desea liberar: "))
            
            except ValueError:
                print("Ingrese un número entero")
                continue
            
            if Numero_asignado <= 0:
                print("Ingrese un número mayor a 0")
                continue
            
            if ListaHabitaciones.Buscar_por_numero_de_habitacion(Numero_asignado) == True:    #Verofico que exista la habitacion
                if ListaHabitaciones.Esta_ocupada_la_habitacion(Numero_asignado) == True:  #Verifico que esté ocupada (True -> si)
                    
                    #Recorro la lista para llegar a la habitacion a liberar
                    NodoActual = ListaHabitaciones.cabeza
                    
                    while NodoActual is not None:
                        if NodoActual.data.numero_habitacion == Numero_asignado:
                            NodoActual.data.estado = False #Cambio el estado a desocupada
                            NodoActual.data.huesped = None #Elimino el huesped asignado a la habitacion
                            print("Habitación liberada correctamente")
                            break
                        else:
                            NodoActual = NodoActual.siguiente
                else:
                    print("La habitación ya está desocupada, no se puede liberar")
                    print("Volviendo al menú principal...")
                    continue
            else:
                print("La habitación no existe, por favor ingrese un número de habitación válido")
                print("Volviendo al menú principal...")
                continue
            print("Volviendo al menú principal...")
            continue
        
        
        case "3":
            print("\t===CONSULTAR INDIVIDUAL DE HUÉSPED POR CÉDULA===\n")
            try:
                cedula = int(input("Ingrese la cédula del huésped que desea consultar: "))
            except ValueError:
                print("Ingrese un número entero")
                continue
            if cedula <= 0:
                print("Ingrese un número mayor a 0")
                continue
            
            NodoActual = ListaHabitaciones.cabeza
            while NodoActual is not None:
                if NodoActual.data.huesped is not None and NodoActual.data.huesped.cedula == cedula: #Si el huesped existe y su cédula coincide con la ingresada
                    print("Huésped encontrado:")
                    print("Nombre: ", NodoActual.data.huesped.nombre)
                    print("Cédula: ", NodoActual.data.huesped.cedula)
                    print("Fecha de ingreso: ", NodoActual.data.huesped.fecha_ingreso)
                    print("Número de habitación asignada: ", NodoActual.data.numero_habitacion)
                    break
                else:
                    NodoActual = NodoActual.siguiente
            #Si el while encuentra huesped, se rompe el ciclo.
            #Si el while termina sin encontrar el huesped, se muestra el mensaje de que no se encontró ningún huésped con esa cédula.
            if NodoActual is None:
                print("No se encontró ningún huésped con esa cédula")
                print("Volviendo al menú principal...")
                continue
            
            print("Volviendo al menú principal...")
            continue
        
        case "4":
            print("\t===CONSULTAR HUÉSPEDES POR ORDEN DE LLEGADA===\n")
            NodoActual = ListaHabitaciones.cabeza
            while NodoActual is not None:
                if NodoActual.data.estado == True: #Si hay un huesped asignado a la habitacion
                    print("Huésped encontrado:")
                    print("Nombre: ", NodoActual.data.huesped.nombre)
                    print("Cédula: ", NodoActual.data.huesped.cedula)
                    print("Fecha de ingreso: ", NodoActual.data.huesped.fecha_ingreso)
                    print("Número de habitación asignada: ", NodoActual.data.numero_habitacion) #Entonces muestra todo
                    print("\n") #Un saltico de linea para que se vea más bonito
                NodoActual = NodoActual.siguiente
            print("Volviendo al menú principal...")
            continue
        
        case "5":
            print("\t===CONSULTAR HABITACIONES DISPONIBLES===\n")
            NodoActual = ListaHabitaciones.cabeza
            Hubo_disponibles = False
            while NodoActual is not None:
                if NodoActual.data.estado == False: #Si la habitación está desocupada (False -> no)
                    print("Número de habitación disponible: --> [", NodoActual.data.numero_habitacion, "]") #Entonces muestra el número de habitación
                    Hubo_disponibles = True
                    
                NodoActual = NodoActual.siguiente
            if NodoActual is None and Hubo_disponibles == True: 
                print("No hay más habitaciones disponibles") #Si hubo disponibles pero ya se mostraron todas
            
            elif NodoActual is None and Hubo_disponibles == False:
                print("No hay habitaciones disponibles") #Si el while termina sin encontrar ninguna habitación disponible, se muestra este mensaje
            
                
            print("Volviendo al menú principal...")
            continue
        
        case "6":
            print("\t===CONSULTAR HABITACIONES OCUPADAS===\n")
            NodoActual = ListaHabitaciones.cabeza
            hay_ocupadas = False
            
            while NodoActual is not None:
                if NodoActual.data.estado == True: #Si la habitación está ocupada (True -> sí)
                    print("Número de habitación ocupada: --> [", NodoActual.data.numero_habitacion, "]") #Entonces muestra el número de habitación
                    hay_ocupadas = True
                NodoActual = NodoActual.siguiente
                
            if NodoActual is None and hay_ocupadas == False:
                print("No hay habitaciones ocupadas")
                
            print("Volviendo al menú principal...")
            continue
 
        case "7":
            print("Saliendo del programa...")
            break
        
        case _:
            print("Opción no válida, por favor seleccione una opción del 1 al 7")
            print("Volviendo al menú principal...")
            continue
        #El programa se ejecutará hasta que el usuario seleccione la opción 7 para salir.
        
        #Aqui el match termina, por lo que ya ese es todo el programa, se muestra el menú de nuevo y se espera la siguiente opción del usuario.
        #El programa ha terminado
        #Procuré que el programa maneje errores importantes y que fuera estético al usarlo, espero haberlo logrado jajaja. 
        
        #Si lees esto sin haber probado el programa, no sigas esta linea, ve a probarlo y luego vuelve a leer esto, si ya lo probaste, entonces gracias por leerlo, espero que te haya gustado y que no hayas encontrado ningún error D:. Mi mensaje secreto final essss: No te rindas, sonríele a la vida aunque hayan problemas o momentos difíciles. Yo me he tardado un montón en hacer este programa, y aunque a veces me sentí frustrada por no saber cómo hacer algo o por no entender algo, seguí intentando y al final lo logré, así que tú también puedes lograr lo que te propongas, solo tienes que seguir intentándolo o buscar ayuda si es necesario, pero no te rindas, porque al final todo el esfuerzo valdrá la pena. ¡Ánimo! ;3 Att: ShiningStar47 
            
    


    
