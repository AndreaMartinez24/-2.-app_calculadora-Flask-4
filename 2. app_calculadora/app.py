# Importamos las clases y métodos

from flask import Flask, render_template, redirect, request
from flask_bootstrap import Bootstrap

app=Flask(__name__)
Bootstrap(app)

@app.route('/', methods=['GET', 'POST'])
def aritmetica():
    if request.method == "POST":
        # Valores que recibo del form n1, n2 son pasados
        num1 = float(request.form.get('n1'))
        num2 = float(request.form.get('n2'))

        # Realizamos opreaciones aritmeticas
        suma = num1 + num2
        resta= num1 - num2
        multiplicacion = num1 * num2
        division= num1 / num2
        return render_template('index.html', suma_total=suma,
                                             resta_total=resta,
                                             multiplicacion_total=multiplicacion,
                                             division_total=division )
    
    return render_template('index.html')

@app.route('/divisas',methods=['GET', "POST"])
def divisas():
    if request.method == "POST":
        # Valores que recibo del form dolar, pesos son pasados
        dolar = int(request.form.get('dolar'))
        pesos = 4200


        # Realizamos opreaciones aritmeticas
        total_pesos = dolar * pesos
        return render_template('divisas.html', total_pesos_colombianos=total_pesos)
    return render_template('divisas.html')


if __name__ == "__main__":
    app.run(debug=True)