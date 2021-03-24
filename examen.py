
def get_list(fichero):
    
    f = open(fichero, mode="rt", encoding="utf-8")
    string = ""
    for linea in f:
        string = string + linea

    f.close()
    return generar_diccionario(string)
def generar_diccionario(string):
    string=string.lower().split()
    dic={}
    for word in string:
        if len(word) not in dic:
            dic[len(word)] = set()
        dic[len(word)].add(word)
    return dic    
print(get_list("fichero.txt"))
print(get_list("vacio.txt"))
