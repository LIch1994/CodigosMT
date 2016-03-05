import SimpleCV
from wand.image import Image


cam = SimpleCV.Camera()


count = 1

while count<6:
   img = cam.getImage()
   faces = img.findHaarFeatures('face.xml')
   if faces is not None:
      faces = faces.sortArea()
      bigFace = faces[-1]
      x,y,w,h = bigFace.boundingBox()
      cara = img.crop(x,y,w,h)
      cara = cara.resize(220,233)
      cara.save('cara' + str(count) + '.png')
      with Image(filename='cara' + str(count) + '.png') as OriginalImagen:
		OriginalImagen.format = 'gif'
		OriginalImagen.save(filename='caraGIF' + str(count) + '.gif')
      count = count + 1
   img.show()


