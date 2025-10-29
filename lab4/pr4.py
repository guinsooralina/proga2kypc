import pprint

def build_tree_iterative(current_root, depth, left_rule, right_rule):
    """
    Генерирует бинарное дерево заданной высоты без рекурсии.

    Args:
        current_root: Значение корневого узла.
        depth (int): Высота дерева (должна быть >= 1).
        left_rule: Функция для вычисления левого потомка.
        right_rule: Функция для вычисления правого потомка.

    Returns:
        dict: Представление бинарного дерева.

    Raises:
        ValueError: Если высота < 1 или при ошибке вычисления функций.
    """
    if depth < 1:
        depth = 1  # Устанавливаем минимальную глубину 1, если передано меньшее значение
    if depth == 1:
        return {"value": current_root}

    root_node = {"value": current_root}

    # Используем стек для обхода дерева и построения узлов
    stack = [(root_node, depth)]

    while stack:
        node, level = stack.pop()

        if level <= 1:
            continue

        try:
            left_val = left_rule(node["value"])
            right_val = right_rule(node["value"])
        except Exception as e:
            raise ValueError(f"Ошибка при вычислении функции: {e}")

        left_node = {"value": left_val}
        right_node = {"value": right_val}

        node["left"] = left_node
        node["right"] = right_node

        # Добавляем в стек узлы следующего уровня, если они не конечные
        if level > 2:
            stack.append((right_node, level - 1))
            stack.append((left_node, level - 1))

    return root_node


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
          "  root = 5, height = 6, левый потомок = root^2, правый = root-2\n")

    # Ввод root
    root_input = input("Введите значение root (по умолчанию 5): ").strip()
    root = float(root_input) if root_input else 5.0

    # Ввод высоты
    height_input = input("Введите значение height (целое число, >=1, по умолчанию 6): ").strip()
    height = int(height_input) if height_input else 6


    left_input = input("Формула для левого (root**2): ").strip()
    left_expr = left_input if left_input else "root**2"
    left_expr = left_expr.replace("root", "x")  # сразу заменяем

    right_input = input("Формула для правого (root-2): ").strip()
    right_expr = right_input if right_input else "root-2"
    right_expr = right_expr.replace("root", "x")

    left_func = make_lambda_from_expr(left_expr)
    right_func = make_lambda_from_expr(right_expr)

    tree = build_tree_iterative(root, height, left_func, right_func)

    print("\nБинарное дерево:")
    pprint.pprint(tree, width=50, sort_dicts=False)


if __name__ == "__main__":
    run_tree_builder()