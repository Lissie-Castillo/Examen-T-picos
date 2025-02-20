from flask import Flask,render_template, request
import math
import cmath
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

#creamos una ruta que solo es accesible por post (si la escribimos directamente en el navegador nos dara error)
@app.route('/calcular', methods=['POST'])
def calculo():
    data = {
        
        "a": int(request.form.get("a", 0)),  # Convertir a entero
        "b": int(request.form.get("b", 0)),  # Convertir a entero
        "c": int(request.form.get("c", 0))   # Convertir a entero
    }

    D = data["b"]**2 - 4*data["a"]*data["c"]

    den= 2*data["a"]
    resp = None


    if den == 0:
        resp = "Error: No se puede dividir por 0."
    else:
        if D > 0:
            x1 = (-data["b"] + math.sqrt(D)) / den
            x2 = (-data["b"] - math.sqrt(D)) / den
            resp = f"Las soluciones reales son x1 = {x1} y x2 = {x2}"
        elif D == 0:
            x3 = -data["b"] / den
            resp = f"Hay una única solución real: x = {x3}"
        else:  # D < 0
            x1 = (-data["b"] + cmath.sqrt(D)) / den
            x2 = (-data["b"] - cmath.sqrt(D)) / den
            resp = f"Las soluciones son complejas: x1 = {x1} y x2 = {x2}"

    return render_template('calculo.html', resp=resp)