import SimpleCV 
from wand.image import Image
import time

#Initialize the camera
cam = SimpleCV.Camera()

# Initialize the display
display = SimpleCV.Display()

#take an initial picture
img = cam.getImage()

# Write a message on the image
img.drawText("Click izquierdo para guardar la foto.", color=SimpleCV.Color().getRandom())

# Show the image on the display
img.save(display)


counter = 0
while not display.isDone():
	# Update the display with the latest image
	img = cam.getImage()
	
	img.save(display)
        	
	if display.mouseLeft:
		faces = img.findHaarFeatures('face.xml')
		faces = faces.sortArea()
		bigFace = faces[-1]
		x,y,w,h = bigFace.boundingBox()
		cara = img.crop(x,y,w,h)
		cara = cara.resize(220,233)
		
		#Save image to the current directory
		cara.save('CaraProfe' + str(counter) + '.png')
		with Image(filename='CaraProfe' + str(counter) + '.png') as OriginalImagen:
			OriginalImagen.format = 'gif'
			OriginalImagen.save(filename='caraProfeGIF' + str(counter) + '.gif')
		cara.save(display)
		counter = counter + 1
	img.drawText("guardar la foto.", color=SimpleCV.Color().getRandom())