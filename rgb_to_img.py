import numpy as np
from PIL import Image
import cv2
import os, sys
from colory.color import Color


im = Image.open("Lena.jpg")

#pixel que será verificado
x = 100
y = 120

pix = im.load()

#tamanho da imagem
width = 150
height = 180

array = np.zeros([height, width, 3], dtype=np.uint8)

ar = pix[x, y] #RGB do pixel

hex = '#%02x%02x%02x' % ( ar[0],ar[1],ar[2] ) #transforma RGB para Hex

cor = Color( hex, 'xkcd') #pega cor a partir do hex e da lista de cores

#print(a.name) #printa nome da cor

array[:,:] = [ar[0], ar[1], ar[2]]

img = Image.fromarray(array)
img.save('myimg.jpg') #salva nova imagem com a cor do pixel

color_img = cv2.imread('myimg.jpg', cv2.IMREAD_COLOR) 
cv2.imshow(cor.name, color_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
