import PIL      
from PIL import Image

basewidth = 640
count = 1

#while count<4:
img = Image.open('cara' + str(count) + '.png')
wpercent = (basewidth/float(img.size[0]))
hsize = int((float(img.size[1]*float(wpercent)))
img = img.resize((basewidth,hsize))
img2.save('caraRedime' + str(count) + '.png')
      #count = count + 1
