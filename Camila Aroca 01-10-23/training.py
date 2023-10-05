import cv2
import os
import numpy as np
import time

def obtenerModelo(method,facesData,labels):

	if method == 'LBPH': emotion_recognizer = cv2.face.LBPHFaceRecognizer_create()

	# Entrenamiento
	print("Entrenando ( "+method+" )...")
	inicio = time.time()
	emotion_recognizer.train(facesData, np.array(labels))
	tiempoEntrenamiento = time.time()-inicio
	print("Tiempo de entrenamiento ( "+method+" ): ", tiempoEntrenamiento)

	# Almacenando modelo
	emotion_recognizer.write("modelo"+method+".xml")

def training():
	dataPath = 'data' #Ruta de Data
	emotionsList = os.listdir(dataPath)
	print('Lista de personas: ', emotionsList)

	labels = []
	facesData = []
	label = 0

	for nameDir in emotionsList:
		emotionsPath = dataPath + '/' + nameDir

		for fileName in os.listdir(emotionsPath):

			labels.append(label)
			facesData.append(cv2.imread(emotionsPath+'/'+fileName,0))

		label = label + 1

	obtenerModelo('LBPH',facesData,labels)
