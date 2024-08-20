class Pacientes:
    def __init__ (self):
        self.__nombre= ""
        self.__cedula = 0
        self.__genero= ""
        self.__servicio = ""

    def verNombre(self):
        return self.__nombre
    def verCedula(self):
        return self.__cedula
    def verGenero(self):
        return self.__genero
    def verServicio(self):
        return self.__servicio
    
    def asignaNombre(self,n):
        self.__servicio= n
    def asignaCedula(self,c):
        self.__cedula=c
    def asignaGenero (self,g):
        self.__genero=g
    def asignaServicio (self,s):
        self.__servicio=s



class Sistema (Pacientes):
    def __init__ (self):
        self.__listapacientes= []
        self.__numeropacientes = len(self.__listapacientes)
    def ingresarpaciente(self):  #Métodos
        print('Añada un paciente: ')
        nombre= str(input('Ingrese el nombre del paciente: '))
        while True:
            try:
                cedula= int (input('Ingrese la cédula del paciente: '))
                break
            except ValueError:
                print('El valor ingresado no es válido.\n Intente de nuevo')
            
        genero= str(input('Ingrese el género del paciente: '))
        servicio= str(input ('Ingrese el servicio que requiere: '))

        paciente= Pacientes() #creación del objeto paciente
        paciente.asignaNombre(nombre)
        paciente.asignaCedula(cedula)
        paciente.asignaGenero(genero)
        paciente.asignaServicio(servicio)
            
        self.__listapacientes.append(paciente)
        self.__numeropacientes = len(self.__listapacientes)

    def vernumerospacientes(self):
        print(f'Número de pacientes: {self.__numeropacientes} ') #no funciona?
        

    def verdatospacientes(self):
        print('Los siguientes son los datos del paciente: ')
        cedula= int(input('Ingrese la cédula a buscar '))
        for p in self.__listapacientes:
            if cedula== p.verCedula():
                print (f'Nombre del paciente es {p.verNombre}.')
                print (f'Cedula del paciente es {p.verCedula}. ')
                print (f'Género del paciente es {p.verGenero}. ')
                print (f'El servicio que recibe del paciente es {p.verServicio}. ')

misistema= Sistema()

while True:
    menu =input("""
    1. Ingresar nuevo paciente.
    2. Número de pacientes.
    3. Datos Paciente.
    4. Salir.
    >>>  """)
    if menu== '1':
        misistema.ingresarpaciente()
    elif menu== '2':
        misistema.vernumerospacientes()
    elif menu== '3':
        misistema.verdatospacientes()
    elif menu =='4':
        print('Has cerrado sesión exitosamente. ') 
        break
    else :
        print ('La opción ingresada no es válida. ')


    

    