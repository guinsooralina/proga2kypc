import unittest
from pr2 import twoSum
# Функция, которую будем тестировать
def add(a, b):
    return a + b

# Тесты
class TestMath(unittest.TestCase):
    def test_add_positive(self):
        self.assertEqual(sorted(twoSum([2,7,6], 9)), [0,1])

    def test_add_negative(self):
        self.assertEqual(sorted(twoSum([5, 4, 11, 8], 13)), [0, 3])

    def test_add_zero(self):
        self.assertEqual(sorted(twoSum([1, 10, 12, 9, 13], 14)), [0, 4])

# Запуск тестов
unittest.main(argv=[''], verbosity=2, exit=False)
