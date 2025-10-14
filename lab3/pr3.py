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
