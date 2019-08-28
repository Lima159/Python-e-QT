import numpy as np
import cv2
from matplotlib import pyplot as plt

imagemOriginal = cv2.imread('dft.png', cv2.IMREAD_GRAYSCALE)

transformadaDeFourier = cv2.dft(np.float32(imagemOriginal), flags = cv2.DFT_COMPLEX_OUTPUT)
# Shift the zero-frequency component to the center of the spectrum.
transformadaDeFourierModificada = np.fft.fftshift(transformadaDeFourier)
imagemNoDominioDaFrequencia = 20 * np.log(cv2.magnitude(transformadaDeFourierModificada[:,:,0],transformadaDeFourierModificada[:,:,1]))

plt.title('Imagem no Espaco da Frequencia')
plt.xticks([])
plt.yticks([])

cv2.imshow('Imagem Original', imagemOriginal)
plt.imshow(imagemNoDominioDaFrequencia, cmap='gray')
plt.show()

altura, largura = imagemOriginal.shape
alturaMedia, larguraMedia = int(altura/2), int(largura/2)

mascara = np.zeros((altura, largura, 2), np.uint8)
mascara[alturaMedia-30:alturaMedia+30, larguraMedia-30:larguraMedia+30] = 1
transformadaDeFourierModificada *= mascara
imagemNoDominioDaFrequencia = 20 * np.log(cv2.magnitude(transformadaDeFourierModificada[:,:,0],transformadaDeFourierModificada[:,:,1]))

transformadaDeFourierInversa = np.fft.ifftshift(transformadaDeFourierModificada)
imagemFiltrada = cv2.idft(transformadaDeFourierInversa)
imagemFiltrada = cv2.magnitude(imagemFiltrada[:,:,0],imagemFiltrada[:,:,1])

plt.title('Imagem Filtrada')
plt.xticks([])
plt.yticks([])

plt.imshow(imagemNoDominioDaFrequencia, cmap='gray')
plt.show()

cv2.imshow('Imagem Original', imagemOriginal)
plt.imshow(imagemFiltrada, cmap='gray')
plt.show()