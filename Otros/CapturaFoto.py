import SimpleCV

cam = SimpleCV.Camera()

# Initialize the display
display = SimpleCV.Display()

while True:
    img = cam.getImage()
    faces = img.findHaarFeatures('haarcascade_frontalface_alt.xml')
    if faces:
        for face in faces:
            face.draw()
    

counter = 0
img.save("photobooth" + str(counter) + ".jpg")


# Show the image on the display
img.save(display)


