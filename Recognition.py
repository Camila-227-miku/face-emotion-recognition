import cv2
import os

def recognizer():
	imagePaths = os.listdir('data')
	print('imagePaths=',imagePaths)

	face_recognizer = cv2.face.LBPHFaceRecognizer_create()

	face_recognizer.read('modeloLBPH.xml') # Lectura de modelo 

	cap = cv2.VideoCapture(0,cv2.CAP_DSHOW) #Para usar camara en directo
	#cap = cv2.VideoCapture('picture.jpg') #Para usar una imagen del equipo

	faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')

	while True:
          ret, frame = cap.read()
          if ret:
               gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
               auxFrame = gray.copy()
               faces = faces = faceClassif.detectMultiScale(gray,1.3,5)
               for (x,y,w,h) in faces:
                rostro = auxFrame[y:y+h,x:x+w]
                rostro = cv2.resize(rostro,(150,150),interpolation= cv2.INTER_CUBIC)
                result = face_recognizer.predict(rostro)

                if result[1] < 70:
                    cv2.putText(frame,'{}'.format(imagePaths[result[0]]),(x,y-25),2,1.1,(0,255,0),2,cv2.LINE_AA)
                    cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
                else:
                    cv2.putText(frame,'Desconocido',(x,y-20),2,0.8,(0,0,255),1,cv2.LINE_AA)
                    cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),2)
                    
               (flag, encodedImage) = cv2.imencode(".jpg", frame)
               if not flag:
                    continue
               yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' +
                    bytearray(encodedImage) + b'\r\n')