from flask import Flask, render_template, request

app = Flask(__name__)


def calculate_roots(a, b, c):
    try:
        a = float(a)
        b = float(b)
        c = float(c)
    except ValueError:
        return 'Введите числовое значение для всех коэффициентов'

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
    a = request.form['a']
    b = request.form['b']
    c = request.form['c']

    if a == '' or b == '' or c == '':
        return 'Введите числовое значение для всех коэффициентов'

    try:
        a = float(a)
        b = float(b)
        c = float(c)
    except ValueError:
        return 'Введите числовое значение для всех коэффициентов'

    result = calculate_roots(a, b, c)
    return render_template('result.html', result=result, a=a, b=b, c=c)


if __name__ == '__main__':
    app.run(debug=True)
