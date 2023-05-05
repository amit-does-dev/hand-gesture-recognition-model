from PIL import Image

# path="Dataset/One/"
# path="Dataset/Two/"
# path="Dataset/Three/"
path="Dataset/Four/"

def resizeImage(imageName):
    basewidth = 100
    img = Image.open(imageName)
    wpercent = (basewidth/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((basewidth,hsize), Image.ANTIALIAS)
    img.save(imageName)

for i in range(0, 201):
    # Mention the directory in which you wanna resize the images followed by the image name
    resizeImage(path + str(i) + '.png')


