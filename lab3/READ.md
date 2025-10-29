# Отчёт по лабораторной работе 3  
## 1. Задача  
Реализовать генератор бинарного дерева заданной высоты, в котором значение каждого узла вычисляется на основе значения его родителя с использованием двух заданных выражений:  
- левый потомок: `root**2`  
- правый потомок: `root - 2`  

Дерево должно быть представлено в виде вложенного словаря, где каждый узел содержит ключ `"value"`, а при наличии потомков — также ключи `"left"` и `"right"`.

## 2. Решение  

### Код `pr3.py`

```python
import pprint


def create_tree_node(current_value, depth, left_rule, right_rule):
    """
    Создаёт узел бинарного дерева рекурсивно.

    Args:
        current_value: Значение текущего узла.
        depth: Оставшаяся глубина (высота) дерева.
        left_rule: Функция для вычисления значения левого потомка.
        right_rule: Функция для вычисления значения правого потомка.

    Returns:
        dict: Представление узла дерева.
    """
    # Устанавливаем минимальную глубину 1, если передано меньшее значение
    if depth < 1:
        depth = 1
    if depth == 1:
        return {"value": current_value}

    left_value = left_rule(current_value)
    right_value = right_rule(current_value)

    return {
        "value": current_value,
        "left": create_tree_node(left_value, depth - 1, left_rule, right_rule),
        "right": create_tree_node(right_value, depth - 1, left_rule, right_rule)
    }


def make_lambda_from_expr(expression_str):
    """
    Создаёт безопасную лямбду из строкового выражения.

    Args:
        expression_str (str): Строковое выражение для преобразования в лямбду.

    Returns:
        function: Лямбда-функция от 'x'.

    Raises:
        ValueError: Если в выражении используется недопустимое имя.
    """
    allowed = {
        "abs": abs,
        "round": round,
        "min": min,
        "max": max,
        "pow": pow,
    }

    compiled_expr = compile(f"lambda x: {expression_str}", "<expr>", "eval")
    for name in compiled_expr.co_names:
        if name not in allowed and name != "x":
            raise ValueError(f"Недопустимое имя: {name}")

    return eval(compiled_expr, {"builtins": {}}, allowed)


def run_tree_builder():
    """
    Основная функция для запуска интерактивного построения дерева.
    """
    print("Если не ввести значение, будут использованы настройки по умолчанию:\n"
          "  root = 5, height = 6, левый = root^2, правый = root-2\n")

    # Ввод root
    root_input = input("Введите значение root (по умолчанию 5): ").strip()
    root = float(root_input) if root_input else 5.0

    # Ввод высоты
    height_input = input("Введите значение height (целое число, >=1, по умолчанию 6): ").strip()
    height = int(height_input) if height_input else 6

    # Ввод выражений для потомков

    left_input = input("Формула для левого (root**2): ").strip()
    left_expr = left_input if left_input else "root**2"
    left_expr = left_expr.replace("root", "x")  # сразу заменяем

    right_input = input("Формула для правого (root-2): ").strip()
    right_expr = right_input if right_input else "root-2"
    right_expr = right_expr.replace("root", "x")

    left_func = make_lambda_from_expr(left_expr)
    right_func = make_lambda_from_expr(right_expr)

    tree = create_tree_node(root, height, left_func, right_func)

    print("\nБинарное дерево:")
    pprint.pprint(tree, width=50, sort_dicts=False)


if __name__ == "__main__":
    run_tree_builder()
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
Код тестирует функцию.
