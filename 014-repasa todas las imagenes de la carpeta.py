from PIL import Image,ImageFilter
import os

memoria = open("memoria.txt",'a')
archivos = os.listdir("entrenamiento")
for archivo in archivos:
    imagen = Image.open("entrenamiento/"+archivo)
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
    valores = [str(num) for num in lista]
    cadena = ','.join(valores)
    memoria.write(archivo.split("-")[1].split(".")[0]+"|"+cadena+"\n")
memoria.close()
                
