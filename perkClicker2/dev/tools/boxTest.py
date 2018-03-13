#!/usr/bin/python
import Image
import pytesseract

#crop image
#photo = Image.open('stillWatching.png')
photo = Image.open('e69a57a3-screen.png')
w , h = photo.size

	
photo.crop((0 , 1600 , w , h)).save("e69a57a3-croped.png")
quit()
screenContents = pytesseract.image_to_string(Image.open('croped.png'))
for line in screenContents.splitlines():
	if line == 'Are you still watching?':
		print line
		execfile('pin-test.py')
