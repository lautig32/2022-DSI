
from Clases import Clases
from Functions.Determine_age import *
from datetime import date
import os
import time

def menuPrincipal():
    desc = 0
    while desc > 10 or desc <= 0:
        print ("\nBienvenido al sistema de Circulo de Sangre para Socios.")
        print ("1- Ingresar un nuevo socio...")
        print ("2- Mostrar socios...")
        print ("3- Registrar pago de los socios...")
        print ("4- Socios que se encuentran en condicion de deuda...")
        print ("5- Registrar socio que se presento a donar...")
        print ("6- Socios disponibles para presentarse a donar...")
        print ("7- Solicitar donadores...")
        print ("8- Socios que ya han cumplido con su donacion...")
        print ("9- Mostrar historial de donadores...")
        print ("10- Mostrar el historial de peticones del banco de sangre...")
        print ("0- Finalizar sistema.")
        desc = int(input ("\nSeleccione la opcion que desea llevar a cabo: "))
        os.system('cls')
    return desc


def cargarSocio(): # 1
    # -- Ingreso de DNI identificador de cada socio.
    documento_identificador = Clases.Socio.ingreso_documento(socio_generico,socio_generico,socios_totales)
    Clases.Socio.dni.append(documento_identificador)
    # -- Registro de relacion entre la donacion y el socio que dono, y pre-ingreso de el estado de este.
    Clases.Donaciones.dni.append(documento_identificador)
    Clases.Donaciones.estado_para_donar.append("Esperando")
    Clases.Donaciones.fecha_ultima_donacion.append("No registrada")
    # -- Ingreso del nombre de cada Socio.
    Clases.Socio.nombre_apellido.append(input("Ingresar nombre y apellido: "))
    # -- Determinacion de la fecha de nacimiento y la edad de el usuario estimado.
    fecha_nacimiento = validate_age()
    Clases.Socio.fecha_nacimiento.append(fecha_nacimiento)
    # -- Ingreso de domiciolio.
    Clases.Socio.domicilio.append(input("Ingresar domicilio: "))
    # -- Numero de domicilio.
    Clases.Socio.numero_domicilio.append(input("Ingresar numero de domicilio: "))
    # -- Ingreso de localidad.
    Clases.Socio.localidad.append(input("Ingresar la Localidad: "))
    # -- Ingreso de provincia.
    Clases.Socio.provincia.append(input("Ingresar la Provincia: "))
    # -- Ingreso de pais.
    Clases.Socio.pais.append(input("Ingresar el Pais de origen: "))
    # -- Ingreso de numero de telefono con validacion.
    Clases.Socio.telefono.append(input("Ingresar numero de telefono: "))
    # -- Ingreso de correo / email.
    Clases.Socio.email.append(input("Ingresar e-mail: "))
    # -- Ingreso de grupo Sanguineo.
    Clases.Socio.grupo_sanguineo.append(socio_generico.seleccionar_grupo_sanguineo(socio_generico,Clases.Socio.Grupo_Sanguineo))
    # -- Ingreso de factor Sanguineo.
    Clases.Socio.factor.append(Clases.Socio.factor_sanguineo())
    # -- Ingreso de padencia de enfermedad.
    posee_enfermedad = Clases.Socio.posee_alguna_enfermedad()
    Clases.Socio.enfermedad.append(posee_enfermedad)
    # -- Determinacion de consumo de medicamentos en base a la enfermedad.
    if posee_enfermedad == 1:
        Clases.Socio.medicamento.append(input("Ingresar si consume algun tipo de medicamento: "))
    else:
        Clases.Socio.medicamento.append("No consume medicamento.")
    # -- Determinacion de la categoria en base a si posee enfermedad y los requisitos de edad.
    Clases.Socio.categoria.append(Clases.Socio.definir_cat_socio(socio_generico,fecha_nacimiento,posee_enfermedad))
    # -- Definir condicion de registro de cada socio.
    Clases.Socio.condicion_deuda.append("No pagado")
    return 0


def mostrarSocio(): # 2
    for i in range(socios_totales):
        print(f"\nSocio numero {i+1}... --------------------")
        print(f"\nSocio {socio_generico.nombre_apellido[i]}, DNI: {socio_generico.dni[i]}," +
        f"Nacido el: {socio_generico.fecha_nacimiento[i]}, y su edad es: {calculate_age(socio_generico.fecha_nacimiento[i])} años" +
        f"\nDomicilio en: {socio_generico.domicilio[i]}, numero: {socio_generico.numero_domicilio[i]}" +
        f"\nSe ubica en: {Clases.Socio.print_info(socio_generico,socio_generico,i)}" +
        f"\nN° telefono: {socio_generico.telefono[i]}, Correo electronico: {socio_generico.email[i]}" +
        f"\nGrupo sanguineo: {socio_generico.grupo_sanguineo[i].name} y su factor es: {socio_generico.factor[i]}" +
        f"\nEnfermedad: {Clases.Socio.mostrar_estado_enfermedad(socio_generico,socio_generico.enfermedad[i])}, Medicamentos: {socio_generico.medicamento[i]}" +
        f"\nSu categoria es: {socio_generico.mostrar_categoria(socio_generico,socio_generico.categoria[i])}\nSu condicion de deuda es: {socio_generico.condicion_deuda[i]}" +
        f"\nSu estado de donacion es: {donacion_generico.estado_para_donar[i]}")
    return 0


def registraremos_el_pago(): # 3
    band = 0
    dniSocioVerificar = int(input("Ingrese el dni del socio que quiere registrar el pago: "))
    for i in range(socios_totales):
        if dniSocioVerificar == socio_generico.dni[i]:
            if socio_generico.categoria[i] == 1:
                saldo = cuota_socio_activo.monto
            else:
                saldo = cuota_socio_inactivo.monto
            print(f"\nUsted registrara el pago de: {socio_generico.nombre_apellido[i]}"+
                    f"\nque se encuentra | {socio_generico.condicion_deuda[i]} |"+
                    f"\nY su saldo es de | {saldo} |")
            variableTemporal = int(input("Ingrese | 1 | para registrar pago." + 
                                        "\nIngrese | 0 | para omitir registro: "))
            if variableTemporal == 1:
                socio_generico.condicion_deuda[i] = "Pagado"
        else:
            band = band + 1
    if band == socios_totales:
        print("\nEl dni ingresado es incorrecto, no se encontro compatibilidad.")
    return 0
    

def sociosEnCondicionDeuda(): # 4
    band = 0
    for i in range(socios_totales):
        if socio_generico.condicion_deuda[i] == "No pagado":
            print(f"\nSocio {socio_generico.nombre_apellido[i]} de DNI: {socio_generico.dni[i]} se encuentra en | {socio_generico.condicion_deuda[i]} |")
            band = band + 1
    if band == 0:
        print("Ningun socio presenta deuda.")
    return 0


def socioPresentadoDonar(): # 5
    dniPresentado = int(input("Dni del socio que se presento a donar: "))
    for i in range(socios_totales):
        if donacion_generico.dni[i] == dniPresentado and socio_generico.categoria[i] != 0:
            donacion_generico.estado_para_donar[i] = "Dono"
            donacion_generico.fecha_ultima_donacion[i] = today
            histoial_generico.dni.append(dniPresentado)
            histoial_generico.fecha_de_donacion.append(today)
    return 0


def sociosDisponiblesParaDonar(): # 6
    for i in range(socios_totales):
        if donacion_generico.estado_para_donar[i] == "Esperando":
            for u in range(socios_totales):
                if socio_generico.dni[u] == donacion_generico.dni[i]:
                    print(f"El socio: {socio_generico.nombre_apellido[i]} esta en condicion de: {donacion_generico.estado_para_donar[i]}.")
    return 0


def solicitarDonadores(): # 7
    listaDonadoresEnEspera = []
    for u in range(solicitud.dadores_necesarios):
        band = 0
        for i in range(socios_totales):
            if solicitud.factor_sanguineo == socio_generico.factor[i] and solicitud.grupo_sanguineo == socio_generico.grupo_sanguineo[i]:
                if donacion_generico.estado_para_donar[i] == "Esperando" and band == 0:
                    print(f"Se solicita al socio: {socio_generico.nombre_apellido[i]} que se presente a donar.")
                    donacion_generico.estado_para_donar[i] = "Dono"
                    donacion_generico.fecha_ultima_donacion[i] = solicitud.fecha
                    listaDonadoresEnEspera.append(donacion_generico.dni[i])
                    histoial_generico.dni.append(donacion_generico.dni)
                    histoial_generico.fecha_de_donacion.append(solicitud.fecha)
                    band = band + 1
    return listaDonadoresEnEspera


def sociosQueYaCumplieron(): # 8
    for i in range(socios_totales):
        if donacion_generico.estado_para_donar[i] == "Dono":
            for u in range(socios_totales):
                if socio_generico.dni[u] == donacion_generico.dni[i]:
                    print(f"El socio: {socio_generico.nombre_apellido[i]} ya dono.")
    return 0


def mostrarHistorialDeDonadores(): # 9
    for i in range(len(histoial_generico.dni)):
        for u in range(len(socio_generico.dni)):
            if histoial_generico.dni[i] == socio_generico.dni[u]:
                print(f"El socio: {socio_generico.nombre_apellido[u]} se presento a donar\n el dia {histoial_generico.fecha_de_donacion[i]}.")
    return 0

def mostrar_historial_peticiones(): # 10 -- mostrar el historial de peticones del banco de sangre.
    for i in range (len(historial_peticiones)):
        print(f"La peticion {i+1} tiene como socios participantes: {historial_peticiones[i]}")
    return 0

def auto_actualizacion_socios(): # 10 -- actualiza la condicion de donacion del socio
    for i in range(socios_totales):
        socio_generico.definir_cat_socio(socio_generico,socio_generico.fecha_nacimiento[i],socio_generico.enfermedad[i])
    return 0

socios_totales : int = 0
decision : int = 1
today = date.today()
historial_peticiones = []
socio_generico = Clases.Socio
donacion_generico = Clases.Donaciones
histoial_generico = Clases.Historiales
cuota_socio_activo = Clases.Cuotas(300,f"10/{today.month+1}/{today.year}")
cuota_socio_inactivo = Clases.Cuotas(500,f"10/{today.month+1}/{today.year}")
while decision != 0:
    auto_actualizacion_socios()
    decision = menuPrincipal()
    if decision == 1:
        cargarSocio()
        socios_totales = socios_totales + 1
        time.sleep(2)
    if decision == 2:
        mostrarSocio()
        time.sleep(5)
    if decision == 3:
        registraremos_el_pago()
        time.sleep(2)
    if decision == 4:
        sociosEnCondicionDeuda()
        time.sleep(2)
    if decision == 5:
        socioPresentadoDonar()
        time.sleep(2)
    if decision == 6:
        sociosDisponiblesParaDonar()
        time.sleep(2)
    if decision == 7:
        socios_necesarios = int(input("Ingresar la cantidad de socios necesarios para la donacion: "))
        grupo_sanguineo = Clases.Socio.seleccionar_grupo_sanguineo(socio_generico,Clases.Socio.Grupo_Sanguineo)
        factor_sanguineo = Clases.Socio.factor_sanguineo()
        solicitud = Clases.Peticiones(socios_necesarios,today,grupo_sanguineo,factor_sanguineo)
        historial_peticiones.append(solicitarDonadores())
        time.sleep(2)
    if decision == 8:
        sociosQueYaCumplieron()
        time.sleep(2)
    if decision == 9:
        mostrarHistorialDeDonadores()
        time.sleep(3)
    if decision == 10:
        mostrar_historial_peticiones()