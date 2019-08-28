import numpy as np
import cv2

#imagemOriginal = cv2.imread('biel.png', cv2.IMREAD_GRAYSCALE)
imagemOriginal = cv2.imread('figurasgeometricas.png')

imagemContornos = imagemOriginal.copy()
imagemFiltrada = cv2.Canny(imagemOriginal, 75, 75)

(_, contours, _) = cv2.findContours(imagemFiltrada, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(imagemContornos, contours, -1, (255,255,0), 2)

cv2.imshow('Imagem Original', imagemOriginal)
cv2.imshow('Imagem Filtrada', imagemFiltrada)
cv2.imshow('Imagem Contornos', imagemContornos)

cv2.waitKey(0)
cv2.waitKey(1)