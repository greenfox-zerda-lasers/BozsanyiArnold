import unittest
import extend

class TestExtend(unittest.TestCase):
    def setUp(self):
        pass

    def test_add_2_and_3_is_5(self):
        self.assertEqual(extend.add(2, 3), 5)
    def test_add_any_number(self):
        self.assertEqual(extend.add(4,6), 10)
        self.assertEqual(extend.add(10,20), 30)
    def test_add_check_input(self):
        self.assertRaises(TypeError, extend.add, 'k', [])
        self.assertRaises(TypeError, extend.add, {}, ' ')

    def test_max_of_three_first(self):
        self.assertEqual(extend.max_of_three(5, 4, 3), 5)
    def test_max_of_three_third(self):
        self.assertEqual(extend.max_of_three(3, 4, 5), 5)
    def test_max_of_three_second(self):
        self.assertEqual(extend.max_of_three(3, 5, 4), 5)
    def test_max_of_three_input_type(self):
        self.assertRaises(TypeError, extend.max_of_three, [], {}, '')

    def test_median_four(self):
        self.assertEqual(extend.median([7,5,3,5]), 5)
    def test_median_five(self):
        self.assertEqual(extend.median([1,2,3,4,5]), 3)
    def test_median_even(self):
        self.assertEqual(extend.median([5,4,2,3]), 3.5)
    def test_median_odd(self):
        self.assertEqual(extend.median([5,6,9,8,10]), 8)
    def test_median_single(self):
        self.assertEqual(extend.median([5]), 5)
    def test_median_input_type(self):
        self.assertRaises(TypeError, extend.median, {})
        self.assertRaises(TypeError, extend.median, '')
        self.assertRaises(TypeError, extend.median, 15)
    def test_median_if_empty(self):
        self.assertRaises(ValueError, extend.median, [])
    def test_median_if_duo(self):
        self.assertEqual(extend.median([2,5]), 3.5)

    def test_is_vovel_a(self):
        self.assertTrue(extend.is_vovel('a'))
    def test_is_vovel_u(self):
        self.assertTrue(extend.is_vovel('u'))
    def test_is_vovel_many(self):
        self.assertRaises(ValueError, extend.is_vovel, 'au')
    def test_is_vovel_empty(self):
        self.assertRaises(ValueError, extend.is_vovel, '')
    def test_is_vovel_not_vovel(self):
        self.assertEqual(extend.is_vovel('b'), False)
    def test_is_vovel_input_type(self):
        self.assertRaises(TypeError, extend.is_vovel, [])

    def test_translate_bemutatkozik(self):
        self.assertEqual(extend.translate('bemutatkozik'), 'bevemuvutavatkovozivik')
    def test_translate_kolbice(self):
        self.assertEqual(extend.translate('kolbice'), 'kovolbiviceve')
    def test_translate_input_type(self):
        self.assertRaises(TypeError, extend.translate, [])
    def test_translate_input_multipliedvovels(self):
        self.assertEqual(extend.translate('alma'), 'avalmava')
if __name__ == '__main__':
    unittest.main()
