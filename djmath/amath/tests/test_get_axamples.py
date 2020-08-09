from django.test import SimpleTestCase
from amath.get_examples import generate_k_examples


class TestExamples(SimpleTestCase):

    def test_get_examples_len(self):
        self.assertEqual(len(list(generate_k_examples(10))), 10)

    def test_get_examples_result_types(self):
        l = list(generate_k_examples(1))
        tup = l[0]
        self.assertTrue(isinstance(tup, tuple))
        self.assertTrue(isinstance(tup[0], str))
        self.assertTrue(isinstance(tup[1], int))

    def test_get_examples_k_neg(self):
        self.assertEqual(len(list(generate_k_examples(-20))), 1)

    def test_get_examples_k_eq_0(self):
        self.assertEqual(len(list(generate_k_examples(0))), 1)

    def test_get_examples_k_too_big(self):
        self.assertEqual(len(list(generate_k_examples(2000))), 121)

    def test_get_examples_k_true(self):
        self.assertEqual(len(list(generate_k_examples(True))), 1)

    def test_get_examples_k_false(self):
        self.assertEqual(len(list(generate_k_examples(False))), 1)

    def test_get_examples_k_is_str(self):
        with self.assertRaises(TypeError):
            list(generate_k_examples("str"))
