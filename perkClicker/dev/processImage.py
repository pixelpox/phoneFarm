#!/usr/bin/python
import Image
import pytesseract

device = 'vod'

if device == 'vod':
	#crop image
	#photo = Image.open('stillWatching.png')
	photo = Image.open('screen.png')
	w , h = photo.size

	
	photo.crop((0 , 370 , w , h)).save("croped.png")

screenContents = pytesseract.image_to_string(Image.open('croped.png'))
for line in screenContents.splitlines():
	if line == 'Are you still watching?':
		print line
		execfile('pin-test.py')
