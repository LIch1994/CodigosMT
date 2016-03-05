#!/usr/bin/python

print __doc__
import time
from SimpleCV import *
display = Display()
cam= Camera()

haarcascade = HaarCascade('face.xml')

while display.isNotDone():
	image = cam.getImage().flipHorizontal().scale(0.5)
	faces = image.findHaarFeatures(haarcascade)
	if faces:
		face = faces[-1]
	 	face.draw(Color.RED, 1)
	image.show()

