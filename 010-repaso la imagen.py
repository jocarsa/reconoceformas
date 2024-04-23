from PIL import Image,ImageFilter

imagen = Image.open("josevicente.jpg")
imagen = imagen.resize((512,512))
imagen = imagen.convert("L")
imagen = imagen.filter(ImageFilter.FIND_EDGES)
imagen = imagen.point(lambda x:0 if x < 50 else 255,'1')
pixeles = imagen.load()
anchurabloque = 2
combinaciones = pow(2,pow(anchurabloque,2))
lista = []
for i in range(0,combinaciones):
    lista.append(None)
for x1 in range(0,512-anchurabloque):
    for y1 in range(0,512-anchurabloque):
        cadena = ""
        for x in range(0,anchurabloque):
            for y in range(0,anchurabloque):
                if pixeles[x1+x,y1+y] == 255:
                    cadena += "1"
                else:
                    cadena += "0"
        print(cadena)
                
