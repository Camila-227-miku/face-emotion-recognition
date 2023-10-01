from flask import Flask, render_template, json, request, Response
import Capture
import Training
import Recognition
import cv2
import os

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/showFormNewPerson')
def showFormNewPerson():
    return render_template('registerPerson.html')


@app.route('/registerPerson',methods=['POST'])
def registerPerson():
    try:
        _name = request.form['inputName']
        Capture.captureImages(_name)
        Training.training()     
        return json.dumps({'message': 'Persona creada exitosamente', 'code': 'success'})   
    except Exception as e:
        return json.dumps({'error':str(e), 'code': 'success'})
    
@app.route('/recognitionPerson')
def recognitionPerson():
    return render_template('recognition.html')

@app.route('/recognitionPersonVideo')
def recognitionPersonVideo():
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    return Response(Recognition.recognizer(),
          mimetype = "multipart/x-mixed-replace; boundary=frame")

if __name__ == "__main__":
    app.run(port=5002)
