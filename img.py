import numpy as np
import cv2
from matplotlib import pyplot as plt

imagemOriginal = cv2.imread('clouds.jpg', cv2.IMREAD_GRAYSCALE)

transformadaDeFourier = cv2.dft(np.float32(imagemOriginal), flags=cv2.DFT_COMPLEX_OUTPUT)
# Shift the zero-frequency component to the center of the spectrum.
transformadaDeFourierModificada = np.fft.fftshift(transformadaDeFourier)
imagemNoDominioDaFrequencia =  np.log(cv2.magnitude(transformadaDeFourierModificada[:,:,0],transformadaDeFourierModificada[:,:,1]))

plt.title('Imagem no Espaco da Frequencia')
plt.xticks([])
plt.yticks([])

cv2.imshow('Imagem Original', imagemOriginal)
plt.imshow(imagemNoDominioDaFrequencia, cmap='gray')
plt.show()