from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_roots(a, b, c):
    discriminant = b * b - 4 * a * c
    if discriminant > 0:
        x1 = (-b + (discriminant ** 0.5)) / (2 * a)
        x2 = (-b - (discriminant ** 0.5)) / (2 * a)
        return f'У уравнения два корня: x₁ = {x1}, x₂ = {x2}'
    elif discriminant == 0:
        x = -b / (2 * a)
        return f'У уравнения один корень: x = {x}'
    else:
        return 'У уравнения нет действительных корней'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    a = float(request.form['a'])
    b = float(request.form['b'])
    c = float(request.form['c'])
    result = calculate_roots(a, b, c)
    return render_template('result.html', result=result, a=a, b=b, c=c)

if __name__ == '__main__':
    app.run(debug=True)
