from flask import Flask, render_template, json, request, Response
#import capture
#import training
#import recognition

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
        #capture.captureImages(_name)
        #training.training()     
        return json.dumps({'message': 'Persona creada exitosamente', 'code': 'success'})   
    except Exception as e:
        return json.dumps({'error':str(e), 'code': 'success'})
    
@app.route('/recognitionPerson')
def recognitionPerson():
    return render_template('recognition.html')

if __name__ == "__main__":
    app.run()
