import cv2 
from PIL import Image 
try: 
  img = Image.open('am.png') 
  x=500 
  y = 600 
  width, height = img.size 
  if x < width and y < height: 
    pixel_value = img.getpixel((x,y)) 
    img.show() 
    print({pixel_value}) 
  else: 
    print("Error: Coordinates out of range") 
except FileNotFoundError: 
  print("error:The image not found.")