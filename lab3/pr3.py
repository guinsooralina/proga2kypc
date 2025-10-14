from pprint import pprint

def gen_bin_tree(height=6, root=5, left_func=None, right_func=None):
    if left_func is None:
        left_func = lambda x: x ** 2
    if right_func is None:
        right_func = lambda x: x - 2

    if height <= 0:
        return None

    left_child = gen_bin_tree(height - 1, left_func(root), left_func, right_func)
    right_child = gen_bin_tree(height - 1, right_func(root), left_func, right_func)

    return {
        'root': root,
        'left': left_child,
        'right': right_child
    }


def print_tree_structure(tree, level=0, prefix="Root: "):
    if tree is None:
        return

    indent = "    " * level
    print(f"{indent}{prefix}{tree['root']}")

    if tree['left'] is not None:
        print_tree_structure(tree['left'], level + 1, "L--- ")
    if tree['right'] is not None:
        print_tree_structure(tree['right'], level + 1, "R--- ")


def calculate_tree_stats(tree):
    if tree is None:
        return 0, 0

    left_count, left_height = calculate_tree_stats(tree['left'])
    right_count, right_height = calculate_tree_stats(tree['right'])

    total_nodes = 1 + left_count + right_count
    height = 1 + max(left_height, right_height)

    return total_nodes, height


if __name__ == "__main__":
    print("=" * 50)
    print("Генерация бинарного дерева (в виде словаря)")
    print("=" * 50)

    print("\n1. Дерево с параметрами по умолчанию (height=6, root=5):")
    tree1 = gen_bin_tree()
    pprint(tree1, width=40, sort_dicts=False)

    print("\n2. Дерево с height=3, root=5:")
    tree2 = gen_bin_tree(height=3, root=5)
    pprint(tree2, width=40, sort_dicts=False)

    print("\n3. Дерево с кастомными функциями (height=3, root=10):")
    tree3 = gen_bin_tree(
        height=3,
        root=10,
        left_func=lambda x: x + 5,
        right_func=lambda x: x * 3
    )
    pprint(tree3, width=40, sort_dicts=False)

    print("\n4. Статистика по деревьям:")
    for i, tree in enumerate([tree1, tree2, tree3], 1):
        nodes, height = calculate_tree_stats(tree)
        print(f"Дерево {i}: узлов = {nodes}, высота = {height}")

    print("\n" + "=" * 50)
    print("Конец программы")
    print("=" * 50)
