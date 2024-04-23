from PIL import Image,ImageFilter

imagen = Image.open("josevicente.jpg")
imagen = imagen.resize((512,512))
imagen = imagen.convert("L")
imagen = imagen.filter(ImageFilter.FIND_EDGES)
imagen = imagen.point(lambda x:0 if x < 50 else 255,'1')
pixeles = imagen.load()
print(pixeles[1,1])
