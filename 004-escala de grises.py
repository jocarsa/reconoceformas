from PIL import Image

imagen = Image.open("josevicente.jpg")
imagen = imagen.resize((512,512))
imagen = imagen.convert("L")
imagen.show()
