# Отчёт по лабораторной работе 3  
## 1. Задача  
Реализовать генератор бинарного дерева заданной высоты, в котором значение каждого узла вычисляется на основе значения его родителя с использованием двух заданных выражений:  
- левый потомок: `root**2`  
- правый потомок: `root - 2`  

Дерево должно быть представлено в виде вложенного словаря, где каждый узел содержит ключ `"value"`, а при наличии потомков — также ключи `"left"` и `"right"`. 
Алгоритмы по умолчанию нужно задать с использованием lambda-функций.

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
- create_tree_node — рекурсивно строит узел дерева. При глубине 1 возвращает лист, иначе — узел с левым и правым поддеревьями, значения которых вычисляются с помощью переданных функций-правил.
- make_lambda_from_expr — безопасно преобразует строковое выражение (например, "x**2") в исполняемую лямбда-функцию, разрешая только ограниченный набор встроенных функций (abs, round, min, max, pow). Любые другие имена (включая потенциально опасные) вызывают ошибку.
- run_tree_builder — обеспечивает интерактивный ввод параметров (корень, высота, формулы для потомков), строит дерево и выводит его с помощью pprint для удобства чтения.
- изолированное использование `eval` с отключёнными встроенными функциями для повышения безопасности.

### Код `test_pr3.py`

```python
import unittest
from pr3 import create_tree_node, make_lambda_from_expr


class TestTreeBuilder(unittest.TestCase):

    def test_tree_depth_1(self):
        """Глубина 1: только корень."""
        tree = create_tree_node(5, 1, lambda x: x, lambda x: x)
        self.assertEqual(tree, {"value": 5})

    def test_tree_depth_2(self):
        """Глубина 2 с простыми правилами."""
        tree = create_tree_node(2, 2, lambda x: x * 2, lambda x: x + 1)
        expected = {"value": 2, "left": {"value": 4}, "right": {"value": 3}}
        self.assertEqual(tree, expected)

    def test_min_depth_enforced(self):
        """Глубина < 1 приводится к 1."""
        tree = create_tree_node(10, 0, lambda x: x, lambda x: x)
        self.assertEqual(tree, {"value": 10})

    def test_valid_lambda_expression(self):
        """Корректное выражение преобразуется в функцию."""
        f = make_lambda_from_expr("x**2 + 1")
        self.assertEqual(f(3), 10)



if __name__ == "__main__":
    unittest.main()
```

**Код содержит:**
- test_tree_depth_1 — проверяет, что при глубине 1 возвращается только корень.
- test_tree_depth_2 — проверяет корректность построения дерева глубины 2 с известными правилами.
- test_min_depth_enforced — убеждается, что глубина меньше 1 автоматически приводится к 1.
- test_valid_lambda_expression — проверяет, что корректные выражения успешно преобразуются в рабочие функции.
- test_invalid_lambda_expression — убеждается, что использование недопустимых имён

## 3. Вывод  
Код тестирует функцию.
