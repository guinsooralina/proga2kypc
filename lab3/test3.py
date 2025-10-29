import unittest
from your_module_name import create_tree_node, make_lambda_from_expr  # замените your_module_name на имя вашего файла


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

    def test_invalid_lambda_expression(self):
        """Недопустимое имя в выражении вызывает ValueError."""
        with self.assertRaises(ValueError):
            make_lambda_from_expr("x + y")  # 'y' не разрешено


if __name__ == "__main__":
    unittest.main()
