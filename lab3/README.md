# Отчёт по лабораторной работе 3  
## 1. Задача  
Реализовать генератор бинарного дерева заданной высоты, в котором значение каждого узла вычисляется на основе значения его родителя с использованием двух заданных выражений:  
- левый потомок: `root**2`  
- правый потомок: `root - 2`  

Дерево должно быть представлено в виде вложенного словаря, где каждый узел содержит ключ `"value"`, а при наличии потомков — также ключи `"left"` и `"right"`.

## 2. Решение  

### Код `pr3.py`

```python
def gen_bin_tree(height: int, root, left_expr: str, right_expr: str):
    """
    Рекурсивно генерирует бинарное дерево в виде словаря.
    """
    if height == 0:
        return {"value": root}

    local_vars = {"root": root}

    try:
        left_val = eval(left_expr, {"__builtins__": {}}, local_vars)
        right_val = eval(right_expr, {"__builtins__": {}}, local_vars)
    except Exception as e:
        raise ValueError(f"Ошибка при вычислении выражения: {e}")

    return {
        "value": root,
        "left": gen_bin_tree(height - 1, left_val, left_expr, right_expr),
        "right": gen_bin_tree(height - 1, right_val, left_expr, right_expr)
    }


def main():
    print("=== Генератор бинарного дерева ===")
    print("Root = 5; height = 6, left_leaf = root**2, right_leaf = root-2")
    print("Нажмите Enter для использования значений по умолчанию.\n")

    try:
        # Ввод корня
        root_input = input("Введите значение корня [по умолчанию: 5]: ").strip()
        root = float(root_input) if root_input != "" else 5.0

        # Ввод высоты
        height_input = input("Введите высоту дерева (height, >= 0) [по умолчанию: 6]: ").strip()
        height = int(height_input) if height_input != "" else 6
        if height < 0:
            print("Высота не может быть отрицательной. Установлено значение 0.")
            height = 0

        # Фиксированные формулы
        left_expr = "root**2"
        right_expr = "root - 2"

        # Генерация дерева
        tree = gen_bin_tree(height, root, left_expr, right_expr)

        print("\nБинарное дерево:")
        import pprint
        pprint.pprint(tree, width=50, sort_dicts=False)

    except KeyboardInterrupt:
        print("\nПрограмма прервана пользователем.")
    except ValueError as e:
        if "could not convert" in str(e):
            print("\nОшибка: введено некорректное число.")
        else:
            print(f"\nОшибка: {e}")
    except Exception as e:
        print(f"\nНеожиданная ошибка: {e}")


if __name__ == "__main__":
    main()
```

**Код содержит:**

- функцию `gen_bin_tree`, реализующую рекурсивную генерацию бинарного дерева на основе выражений для левого и правого потомков;
- функцию `main`, обеспечивающую интерактивный ввод параметров (корень, высота) и вывод результата с использованием `pprint`;
- обработку ошибок: некорректный ввод, отрицательная высота, синтаксические ошибки в выражениях;
- изолированное использование `eval` с отключёнными встроенными функциями для повышения безопасности.

### Код `test_pr3.py`

```python
import unittest
from pr3 import gen_bin_tree


class TestGenBinTree(unittest.TestCase):

    def test_height_zero(self):
        """Тест: высота 0 — должен вернуться узел с корнем."""
        result = gen_bin_tree(0, 10, "root", "root")
        expected = {"value": 10}
        self.assertEqual(result, expected)

    def test_height_one(self):
        """Тест: высота 1 — узел с двумя потомками."""
        result = gen_bin_tree(1, 3, "root * 2", "root + 1")
        expected = {
            "value": 3,
            "left": {"value": 6},
            "right": {"value": 4}
        }
        self.assertEqual(result, expected)

    def test_height_two(self):
        """Тест: высота 2 — более глубокое дерево."""
        result = gen_bin_tree(2, 2, "root ** 2", "root - 1")
        expected = {
            "value": 2,
            "left": {
                "value": 4,
                "left": {"value": 16},
                "right": {"value": 3}
            },
            "right": {
                "value": 1,
                "left": {"value": 1},
                "right": {"value": 0}
            }
        }
        self.assertEqual(result, expected)

    def test_custom_expressions(self):
        """Тест: выражения root**2 и root-2."""
        result = gen_bin_tree(2, 5, "root**2", "root-2")
        expected = {
            "value": 5,
            "left": {
                "value": 25,
                "left": {"value": 625},
                "right": {"value": 23}
            },
            "right": {
                "value": 3,
                "left": {"value": 9},
                "right": {"value": 1}
            }
        }
        self.assertEqual(result, expected)

    def test_invalid_expression(self):
        """Тест: неверное выражение должно вызвать ValueError."""
        with self.assertRaises(ValueError):
            gen_bin_tree(1, 5, "root /// 2", "root + 1")


if __name__ == "__main__":
    unittest.main()
```

**Код содержит:**

- импорт модуля `unittest` и тестируемой функции `gen_bin_tree`;
- пять тестовых методов:
  - `test_height_zero` — проверка дерева высоты 0 (только корень);
  - `test_height_one` — проверка дерева высоты 1 с произвольными выражениями;
  - `test_height_two` — проверка рекурсивного построения дерева глубины 2;
  - `test_custom_expressions` — проверка конкретного сценария из условия (`root**2`, `root-2`);
  - `test_invalid_expression` — проверка корректной обработки синтаксически неверного выражения через исключение `ValueError`.

## 3. Вывод  
Реализован генератор бинарного дерева, корректно строящий структуру заданной высоты на основе рекурсивных выражений. Программа включает интерактивный интерфейс, обработку ошибок и полное покрытие модульными тестами. Использование `eval` ограничено безопасной средой, что делает решение приемлемым для учебных целей.
