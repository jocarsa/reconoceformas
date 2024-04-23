from PIL import Image,ImageFilter

imagen = Image.open("josevicente.jpg")
imagen = imagen.resize((512,512))
imagen = imagen.convert("L")
imagen = imagen.filter(ImageFilter.FIND_EDGES)
imagen.show()
