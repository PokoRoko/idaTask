from PIL import Image as ImgPil


with ImgPil.open('test.jpeg') as img:
    width, height = img.size
    print(width, height)