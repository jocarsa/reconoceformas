from PIL import Image,ImageFilter
import os


imagen = Image.open("prueba/mirectangulo1.png")
imagen = imagen.resize((512,512))
imagen = imagen.convert("L")
imagen = imagen.filter(ImageFilter.FIND_EDGES)
imagen = imagen.point(lambda x:0 if x < 50 else 255,'1')
pixeles = imagen.load()
anchurabloque = 2
combinaciones = pow(2,pow(anchurabloque,2))
lista = []
for i in range(0,combinaciones):
    lista.append(0)
for x1 in range(0,512-anchurabloque):
    for y1 in range(0,512-anchurabloque):
        cadena = ""
        for x in range(0,anchurabloque):
            for y in range(0,anchurabloque):
                if pixeles[x1+x,y1+y] == 255:
                    cadena += "1"
                else:
                    cadena += "0"
        lista[int(cadena,2)] += 1
print(lista)
mejortipo = None
mejorsuma = 10000000000
archivo = open("memoria.txt")
for linea in archivo:
    tipo = linea.split("|")[0]
    valores = linea.split("|")[1]
    valores = valores.split(",")
    valores = [int(num_str) for num_str in valores]
    suma = 0
    for i in range(0,len(valores)):
        suma += abs(lista[i] - valores[i])
    print(tipo+": "+str(suma))
archivo.close()
