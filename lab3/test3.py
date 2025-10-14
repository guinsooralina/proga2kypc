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