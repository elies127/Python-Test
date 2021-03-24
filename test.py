import unittest
from libro import Libro
from autor import Autor
from examen import *
class Pruebas(unittest.TestCase):

    def test_1(self):
        l1 = Libro(autor = Autor(id_autor = 1, nombre = "Miguel de Cervantes", apellido = "Saavedra"), titulo = "Don Quijote", anyo = 1522)
        l2 = Libro(autor = Autor(id_autor = 2, nombre = "Miguel", apellido = "Jose"), titulo = "Doña Quijota", anyo = 1901)
        l3 = Libro(autor = Autor(id_autor = 3, nombre = "Miguelito", apellido = "Jose Paco"), titulo = "Don Moderno 2040", anyo = 2040)
        l4 = Libro(autor = Autor(id_autor = 4, nombre = "Alejandro", apellido = "Maria"), titulo = "Harry Potter 2020", anyo = 2020) 
        lista = [l1, l2, l3, l4]
        self.assertRaises(examen.mas_antiguo(lista, 1800))
        
    
    def test_2(self):
        l1 = Libro(autor = Autor(id_autor = 1, nombre = "Miguel de Cervantes", apellido = "Saavedra"), titulo = "Don Quijote", anyo = 1522)
        l2 = Libro(autor = Autor(id_autor = 2, nombre = "Miguel", apellido = "Jose"), titulo = "Doña Quijota", anyo = 1901)
        l3 = Libro(autor = Autor(id_autor = 3, nombre = "Miguelito", apellido = "Jose Paco"), titulo = "Don Moderno 2040", anyo = 2040)
        l4 = Libro(autor = Autor(id_autor = 4, nombre = "Alejandro", apellido = "Maria"), titulo = "Harry Potter 2020", anyo = 2020) 
        lista = [l1, l2, l3, l4]
        self.assertRaises(mas_antiguo(lista, 2050))
    def test_3(self):
        l1 = Libro(autor = Autor(id_autor = 1, nombre = "Miguel de Cervantes", apellido = "Saavedra"), titulo = "Don Quijote", anyo = 1522)
        l2 = Libro(autor = Autor(id_autor = 2, nombre = "Miguel", apellido = "Jose"), titulo = "Doña Quijota", anyo = 1901)
        l3 = Libro(autor = Autor(id_autor = 3, nombre = "Miguelito", apellido = "Jose Paco"), titulo = "Don Moderno 2040", anyo = 2040)
        l4 = Libro(autor = Autor(id_autor = 4, nombre = "Alejandro", apellido = "Maria"), titulo = "Harry Potter 2020", anyo = 2020) 
        lista = [l1, l2, l3, l4]
        self.assertRaises(mas_antiguo(lista, -1.6))
    def test_4(self): #--------------- Qué ocurre si el título es none
        l1 = Libro(autor = Autor(id_autor = 1, nombre = "Miguel de Cervantes", apellido = "Saavedra"), titulo = None, anyo = 1522)
        l2 = Libro(autor = Autor(id_autor = 2, nombre = "Miguel", apellido = "Jose"), titulo = "Doña Quijota", anyo = 1901)
        l3 = Libro(autor = Autor(id_autor = 3, nombre = "Miguelito", apellido = "Jose Paco"), titulo = "Don Moderno 2040", anyo = 2040)
        l4 = Libro(autor = Autor(id_autor = 4, nombre = "Alejandro", apellido = "Maria"), titulo = "Harry Potter 2020", anyo = 2020) 
        lista = [l1, l2, l3, l4]
        self.assertRaises(mas_antiguo(lista, 2020))
    def test_5(self): #--------------- Qué ocurre si el título es none Pero nunca llega a ser mostrado por mas_antiguos (cambiamos año)
        l1 = Libro(autor = Autor(id_autor = 1, nombre = "Miguel de Cervantes", apellido = "Saavedra"), titulo = None, anyo = 1990)
        l2 = Libro(autor = Autor(id_autor = 2, nombre = "Miguel", apellido = "Jose"), titulo = "Doña Quijota", anyo = 1901)
        l3 = Libro(autor = Autor(id_autor = 3, nombre = "Miguelito", apellido = "Jose Paco"), titulo = "Don Moderno 2040", anyo = 2040)
        l4 = Libro(autor = Autor(id_autor = 4, nombre = "Alejandro", apellido = "Maria"), titulo = "Harry Potter 2020", anyo = 2020) 
        lista = [l1, l2, l3, l4]
        self.assertRaises(mas_antiguo(lista, 1989))     
class Suite(unittest.TestSuite):

    def __init__(self):
        super(Suite, self).__init__()        
        self.addTest(Pruebas('test_1'))
        self.addTest(Pruebas('test_2'))
        self.addTest(Pruebas('test_3'))
        self.addTest(Pruebas('test_4'))
        self.addTest(Pruebas('test_5'))

if __name__ == "__main__":    
    runner = unittest.TextTestRunner()
    my_suite = Suite()
    runner.run(my_suite)
