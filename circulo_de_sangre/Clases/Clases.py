from enum import *
from Functions.Determine_age import *

class Cuotas:
    monto = []
    fecha_vencimiento = []
    def __init__(self,monto,fecha_vencimiento):
        self.monto = monto
        self.fecha_vencimiento = fecha_vencimiento

class Donaciones():
   dni = []
   fecha_ultima_donacion = []
   estado_para_donar = []

class Historiales:
    dni = []
    fecha_de_donacion = []

class Peticiones:
    def __init__(self,dadores_necesarios,fecha,grupo_sanguineo,factor_sanguineo):
        self.dadores_necesarios = dadores_necesarios
        self.fecha = fecha
        self.grupo_sanguineo = grupo_sanguineo
        self.factor_sanguineo = factor_sanguineo


class Pais:
    pass
    pais = []


class Provincia(Pais):
    pass
    provincia = []


class Localidad(Provincia):
    pass
    localidad = []


class Socio(Localidad):
    dni = []
    nombre_apellido = []
    fecha_nacimiento = []
    domicilio = []
    numero_domicilio = []
    telefono = []
    email = []
    grupo_sanguineo = []
    factor = []
    enfermedad  = []
    medicamento = []
    categoria = []
    condicion_deuda = []


    class Grupo_Sanguineo(Enum):
            A = 0
            B = 1
            AB = 2
            O = 3


    def ingreso_documento(self, socio_generico, socios_totales):
        while True:
            try:
                bandera = 0
                documento_identificador = int(input("Ingresar documento: "))
                while bandera == 0:
                    bandera = 1
                    for u in range(socios_totales):
                        if documento_identificador == socio_generico.dni[u]:
                            bandera = 0
                            documento_identificador = int(input("Ese documento ya se encuentra registrado, reingrese otro numero: "))
            except ValueError:
                print("Debes ingresar un numero de DNI.")
                continue
            else:
                break
        return documento_identificador
    

    def definir_cat_socio(self,fecha_nacimiento,posee_enfermedad):
        edad_calculada = calculate_age(fecha_nacimiento)
        if posee_enfermedad != 1:
            if edad_calculada >= 18:
                cate = 1
            else:
                cate = 0
        else:
            cate = 0
        return cate


    def mostrar_categoria(self, categoria_num):
        if categoria_num == 1:
            return "Activo"
        elif categoria_num == 0:
            return "Inactivo"



    def seleccionar_grupo_sanguineo(self, valores_enum_Grupo_Sanguineo):
        cont = 0
        seleccion = 0
        print("Grupos sanguineos posibles...")
        for grupo in valores_enum_Grupo_Sanguineo:
            cont = cont + 1
            print(f"Grupo: {cont} es: {grupo.name}")
        while seleccion > 4 or seleccion <= 0:
            seleccion = int(input("Seleccione un grupo sanguineo: "))
            if seleccion > 4 or seleccion <= 0:
                seleccion = int(input("Reingresar grupo sanguineo por un dato valido del 1 al 4: "))
        grupo_sanguineo = valores_enum_Grupo_Sanguineo(seleccion-1)
        return grupo_sanguineo
    

    def factor_sanguineo():
        factor = 0
        while factor != '+' and factor != '-':
            factor = input("Ingresar factor Sanguineo | + | o | - | : ")
            if factor != '+' and factor != '-':
                factor = input("Se solicita ingresar un factor sanguineo correcto.\nDebe ser | + | o | - | : ")
        return factor

    def posee_alguna_enfermedad():
        var = False
        while var != True:
            posee_enfermedad = int(input("Ingresar | 1 | si posee alguna en fermedad\nIngresar | 0 | si no posee ninguna enfermedad: "))
            var = True
            if posee_enfermedad != 0 and posee_enfermedad != 1:
                print("Debes ingresar un numero correcto.")
                var = False
        return posee_enfermedad


    def mostrar_estado_enfermedad(self, i):
        if i == 0:
            return "No posee enfermedad"
        elif i == 1:
            return "Posee enfermedad"

    def print_info(self, socio_generico, i):
        return f"Reside en: {socio_generico.pais[i]}, su provincia es: {socio_generico.provincia[i]}, y la localidad es: {socio_generico.localidad[i]}"
            