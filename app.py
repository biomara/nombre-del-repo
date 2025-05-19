from flask import Flask

app = Flask(__name__)

@app.route('/')
def inicio():
    return """
    <h1>¡Hola desde Azure 5.3!</h1>
    <p>Nombre completo: "Biomara Valenzuela Godina"</p>
    <p>Carrera: "mi carrera es ingenieria informatica"</p>
    <p>Semestre: "estoy en octavo semestre"</p>
    <p>No. de Control: 21550748 </p>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
