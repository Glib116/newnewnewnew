from PIL import Image
from PIL import ImageFilter

with Image.open("дуже неслухняний та жирний мопс!!!! Поганий!!!.png") as pic_original:
    pic_original.show()
    
    pic_gray = pic_oroginal.convert("L")
    pic_gray.save("дуже неслухняний та жирний мопс!!!! Поганий!!!1.png")
    pic_gray.show
    
    pic_up = pic_gray.transpose(Image.ROTATE_90)
    pic_up.save("дуже неслухняний та жирний мопс!!!! Поганий!!!2.png")
    pic_up.show()
    
    print("розмір:"+ pic_original.size)
    print("формат:"+ pic_original.format )
    print("тип:"+ pic_original.mode)