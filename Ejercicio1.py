import csv

def ejercicio1():
    nombre = input("Ingrese su nombre: ")
    correo = input("Ingrese su correo: ")
    unMail.crearCuenta(correo)
    print(f"Estimado {nombre} te enviaremos tus mensajes a la direccion {correo}")

def ejercicio2():
    cont = input("Ingrese contraseña actual: ")
    unMail.cambiarContraseña(cont)

def ejercicio3():
    correo2 = input("Ingrese correo: ")
    otroMail.crearCuenta(correo2)

def ejercicio4():
    pass

class Email:
    __idCuenta = ""
    __dominio = ""
    __tipoDominio = ""
    __contraseña = ""

    def __init__(self, idCuenta = "", dominio = "", tipoDominio = "", contraseña = ""):
        __idCuenta = idCuenta
        __dominio = dominio
        __tipoDominio = tipoDominio
        __contraseña = contraseña
        
    def retornaEmail(self):
        mailComp = self.__idCuenta + "@" + self.__dominio + "." + self.__tipoDominio
        return mailComp
    
    def getDominio(self):
        return self.__dominio
    
    def crearCuenta(self, correo):
        divideId = correo.split("@")
        self.__idCuenta = divideId[0]
        DomYTip = divideId[1]
        divideDom = DomYTip.split(".")
        self.__dominio = divideDom[0]
        self.__tipoDominio = divideDom[1]
        self.__contraseña = input("Ingrese Contraseña: ")

    def cambiarContraseña(self, cont):
        if cont == self.__contraseña:
            self.__contraseña = input("Contraseña correcta, ingrese nueva contraseña: ")
        else: print(f"Contraseña Incorrecta")
        

    
if __name__ == "__main__":
    unMail = Email(idCuenta="", dominio="", tipoDominio="", contraseña="")
    ejercicio1()
    print(unMail.retornaEmail())
    ejercicio2()
    otroMail = Email(idCuenta="", dominio="", tipoDominio="", contraseña="")
    ejercicio3()
    archivo = open("inciso4.csv")
    lista = []
    cuentas = []
    reader = csv.reader(archivo,delimiter=';')
    next(reader, None)
    for fila in reader:
        lista.append(fila[0])
    archivo.close
    for i in range(len(lista)):
        cuentas[i].append = Email(idCuenta="", dominio="", tipoDominio="", contraseña="")
        cuentas[i].crearCuenta(lista[i])
    ejercicio4()