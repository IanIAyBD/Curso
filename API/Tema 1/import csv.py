import csv
import re
 
 
class Contacto:
    def __init__(self,nombre,apellido,movil):
        self.nombre=nombre
        self.apellido=apellido
        self.movil=movil
class Agenda:
    def __init__(self):
        self.contactos=[]
    def añadir(self,nombre,apellido,movil):
        contacto=Contacto(nombre,apellido,movil)
        self.contactos.append(contacto)
    def mostrarTodos(self):
        for contacto in self.contactos:
            self.imprimeContacto(contacto)
    def buscar(self,textoBuscar):
        encontrado=0
        for contacto in self.contactos:
            if (re.findall(textoBuscar,contacto.nombre)) or (re.findall(textoBuscar,contacto.apellido)):
                self.imprimeContacto(contacto)
                encontrado=encontrado+1
        if encontrado==0:
            self.noEncontrado()
    def borrar(self,codigo):
        for contacto in self.contactos:
            if contacto.codigo==codigo:
                print('-----------------------------------')
                print('¿Borar el contacto? (si/no) ')
                print('-----------------------------------')
                opcion=str(input(""))
                if opcion=='si':
                    print('Contacto borrado')
                    del self.contactos[codigo]
                elif opcion=='no':
                    break
    def grabar(self):
        with open('agenda.csv','w') as fichero:
            escribir=csv.writer(fichero)
            escribir.writerow(('codigo', 'nombre', 'apellido', 'movil'))
            for contacto in self.contactos:
                escribir.writerow((contacto.codigo,contacto.nombre,contacto.apellido,contacto.movil))
    def imprimeContacto(self,contacto):
        print()
        print('-----------------------------------')
        print('Codigo: {}'.format(contacto.codigo))
        print('Nombre:{}'.format(contacto.nombre))
        print('Apellido:{}'.format(contacto.apellido))
        print('Movil:{}'.format(contacto.movil))
        print('-----------------------------------')
    def noEncontrado(self):
        print()
        print('-----------------------------------')
        print('Contacto no encontrado')
        print('-----------------------------------')
def ejecutar():
    global movil
    agenda=Agenda()
    try:
        with open('agenda.csv','r') as fichero:
            lector=csv.DictReader(fichero,delimiter=',')
            for fila in lector:
                agenda.añadir(fila['nombre'],fila['apellido'],fila['movil'])
    except:
        print('Error al abrir fichero o no existe fichero aun')
    while True:
        Menu=str(input("""
        1. Mostrar lista de contactos \n
        2. Buscar contacto \n
        3. Añadir contacto \n
        4. Eliminar contacto \n
        5. Salir \n
        Elija una opción escribiendo el número:
        """))
        if Menu=='1':
            agenda.mostrarTodos()
        elif Menu=='2':
            texto=str(input('Escribe el nombre o apellido del contacto: '))
            agenda.buscar(texto.capitalize())
        elif Menu=='3':
            nombre=str(input('Escribe el nombre: '))
            apellido=str(input('Escribe el apellido: '))
            movil=str(input('Escribe el movil: '))
            agenda.añadir(nombre,apellido,movil)
            agenda.grabar()
        elif Menu=='4':
            pass
        elif Menu=='5':
            print('Ha finalizado')
            agenda.grabar()
            break
        else:
            print('Debe marcar una opcion del Menu')
if __name__=='__main__':
    ejecutar()