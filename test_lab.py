import unittest
from lab import app

class TestApp(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_index_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Калькулятор корней квадратных уравнений', response.data.decode('utf-8'))

    def test_valid_input(self):
        response = self.app.post('/calculate', data=dict(a=1, b=-3, c=2), follow_redirects=True)
        self.assertIn('У уравнения два корня', response.data.decode('utf-8'))

    def test_one_root(self):
        response = self.app.post('/calculate', data=dict(a=1, b=-4, c=4), follow_redirects=True)
        self.assertIn('У уравнения один корень', response.data.decode('utf-8'))

    def test_no_real_roots(self):
        response = self.app.post('/calculate', data=dict(a=1, b=2, c=3), follow_redirects=True)
        self.assertIn('У уравнения нет действительных корней', response.data.decode('utf-8'))

    def test_invalid_input(self):
        response = self.app.post('/calculate', data=dict(a='a', b='b', c='c'), follow_redirects=True)
        self.assertIn('Введите числовое значение для всех коэффициентов', response.data.decode('utf-8'))

    def test_dict_input(self):
        response = self.app.post('/calculate', data=dict(a={'a': 1}, b={'b': -3}, c={'c': 2}), follow_redirects=True)
        self.assertIn('Введите числовое значение для всех коэффициентов', response.data.decode('utf-8'))

    def test_space_input(self):
        response = self.app.post('/calculate', data=dict(a=' ', b=' ', c=' '), follow_redirects=True)
        self.assertIn('Введите числовое значение для всех коэффициентов', response.data.decode('utf-8'))

    def test_symbol_input(self):
        response = self.app.post('/calculate', data=dict(a='@', b='#', c='$'), follow_redirects=True)
        self.assertIn('Введите числовое значение для всех коэффициентов', response.data.decode('utf-8'))

    def test_complex_number_input(self):
        response = self.app.post('/calculate', data=dict(a='1+2j', b='3+4j', c='5+6j'), follow_redirects=True)
        self.assertIn('Введите числовое значение для всех коэффициентов', response.data.decode('utf-8'))

    def test_space_string_input(self):
        response = self.app.post('/calculate', data=dict(a=' ', b=' ', c=' '), follow_redirects=True)
        self.assertIn('Введите числовое значение для всех коэффициентов', response.data.decode('utf-8'))

    def test_empty_string_input(self):
        response = self.app.post('/calculate', data=dict(a='', b='', c=''), follow_redirects=True)
        self.assertIn('Введите числовое значение для всех коэффициентов', response.data.decode('utf-8'))

    def test_number_string_input(self):
        response = self.app.post('/calculate', data=dict(a='123', b='456', c='789'), follow_redirects=True)
        self.assertIn('У уравнения нет действительных корней', response.data.decode('utf-8'))

    def test_mixed_string_input(self):
        response = self.app.post('/calculate', data=dict(a='1a2b3c', b='4d5e6f', c='7g8h9i'), follow_redirects=True)
        self.assertIn('Введите числовое значение для всех коэффициентов', response.data.decode('utf-8'))

    def test_special_characters_input(self):
        response = self.app.post('/calculate', data=dict(a='!@#', b='$%^', c='&*('), follow_redirects=True)
        self.assertIn('Введите числовое значение для всех коэффициентов', response.data.decode('utf-8'))

    def test_zero_coefficients(self):
        response = self.app.post('/calculate', data=dict(a=0, b=0, c=0), follow_redirects=True)
        self.assertIn('Уравнение имеет бесконечное множество корней', response.data.decode('utf-8'))

    def test_zero_minus_coefficients(self):
        response = self.app.post('/calculate', data=dict(a=-0, b=-0, c=-0), follow_redirects=True)
        self.assertIn('Уравнение имеет бесконечное множество корней', response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
