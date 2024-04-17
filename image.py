from PIL import Image,ImageFilter


img  = Image.open('./images/pikachu.jpg')

#blur the image
filter_img = img.filter(ImageFilter.BLUR)
filter_img.save('blur.png', 'png')

#convert the image
filter_img_l = img.convert('L')
filter_img_l.save('grey.png', 'png')

#rorate the image and resize the image
image_rotate = filter_img_l.rotate(90)
image_resize = image_rotate.resize((300,300))
image_resize.save('grey.png', 'png')


# filter_img.show()

# print(dir(img))