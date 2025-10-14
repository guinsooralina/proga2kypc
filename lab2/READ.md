# Отчёт по лабораторной работе 1
## 1. Задача
Дан массив целых чисел `nums` и целочисленное значение переменной `target` , верните индексы двух чисел таким образом, чтобы они в сумме давали `target`.
## 2. Решение
##  Код `pr1.py`

```
def two_sum(nums, target):
    num_x = {}
    for index, num in enumerate(nums):
        complement = target - num
        if complement in num_x:
            return [num_x[complement], index]
        num_x[num] = index
    print("нет подходящих слагаемых для заданной суммы.")
    return None
```
**Код содержит:**

• массив целых чисел `nums` и целевую сумму `target`
 
• содержит функцию `twoSum`

## Код `test1.py`

```
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

```
**Код содержит:** 

• импортирует модуль `unittest`

• `test_add_positive` — проверяет сложение положительных чисел.
`test_add_negative` — проверяет сложение отрицательных чисел.
`test_add_zero` — проверяет сложение с нулём.

## 3. Вывод 
Код тестирует функцию. 
