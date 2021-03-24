from libro import Libro
from autor import Autor

def get_list(fichero):
    
    f = open(fichero, mode="rt", encoding="utf-8")
    string = ""
    for linea in f:
        string = string + linea

    f.close()
    if string == "":
        raise ValueError("El archivo está vacio")
    else:
        return generar_diccionario(string)
def generar_diccionario(string):
    string=string.lower().split()
    dic={}
    for word in string:
        if len(word) not in dic:
            dic[len(word)] = set()
        dic[len(word)].add(word)
    return dic


def mas_antiguos(lista, anyo):

    listaux = []

    if anyo < 1900 or anyo > 2021:
        raise ValueError("Año no válido")
    for libro in lista:
        if libro.get_anyo() <= anyo:
            listaux.append(libro.get_titulo()) 
    return listaux
   
        
# --------------------MAIN---------------------
print(get_list("fichero.txt"))
try:
    print(get_list("vacio.txt"))
except ValueError:
    print("ValueError: No se ha detectado ninguna palabra en el fichero")

l1 = Libro(autor = Autor(id_autor = 1, nombre = "Miguel de Cervantes", apellido = "Saavedra"), titulo = "Don Quijote", anyo = 1522)
l2 = Libro(autor = Autor(id_autor = 2, nombre = "Miguel", apellido = "Jose"), titulo = "Doña Quijota", anyo = 1901)
l3 = Libro(autor = Autor(id_autor = 3, nombre = "Miguelito", apellido = "Jose Paco"), titulo = "Don Moderno 2040", anyo = 2040)
l4 = Libro(autor = Autor(id_autor = 4, nombre = "Alejandro", apellido = "Maria"), titulo = "Harry Potter 2020", anyo = 2020) 
lista = [l1, l2, l3, l4]
try:
    print(mas_antiguos(lista, 2022))
except ValueError:
    print("ValueError: Fecha no valida")
print(mas_antiguos(lista, 2019))
    
