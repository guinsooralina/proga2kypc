# Отчёт по лабораторной работе 1
## 1. Задача
Дан массив целых чисел `nums` и целочисленное значение переменной `target` , верните индексы двух чисел таким образом, чтобы они в сумме давали `target`.
## 2. Решение
##  Код `pr1.py`

```
def twoSum(nums, target):
    nums_map = {}
    for index, num in enumerate(nums):
        complement = target - num
        if complement in nums_map:
            return [nums_map[complement], index]
        nums_map[num] = index

    return None  

nums1 = [2, 7, 11, 15]
target1 = 9
print(twoSum(nums1, target1)) 

nums2 = [3, 2, 4]
target2 = 6
print(twoSum(nums2, target2))  

nums3 = [3, 3]
target3 = 6
print(twoSum(nums3, target3))

```
**Код содержит:**

• массив целых чисел `nums` и целевую сумму `target`
 
• содержит функцию `twoSum`

## Код `test1.py`

```
import unittest

# Функция, которую будем тестировать
def add(a, b):
    return a + b

# Тесты
class TestMath(unittest.TestCase):
    def test_add_positive(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative(self):
        self.assertEqual(add(-1, -3), -4)

    def test_add_zero(self):
        self.assertEqual(add(0, 5), 5)

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
