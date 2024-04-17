from PIL import Image,ImageFilter


img  = Image.open('./images/pikachu.jpg')
filter_img = img.filter(ImageFilter.BLUR)
filter_img.save('blur.png', 'png')
filter_img.show()

# print(dir(img))