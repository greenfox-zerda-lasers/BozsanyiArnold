import unittest
from Arnold_Bozsanyi import *



class Bozsanyi_Arnold_Test(unittest.TestCase):
    def test_anagramm_if_anagramm(self):
        self.assertTrue(anagramm('alma','lama'))
        self.assertFalse(anagramm('korte','alma'))
        self.assertTrue(anagramm('korte','korte'))
    def test_anagramm_if_space(self):
        self.assertTrue(anagramm('al ma', 'lama'))
    def test_anagramm_if_string(self):
        self.assertRaises(TypeError, anagramm,[],[])
        self.assertRaises(TypeError, anagramm, 1,2)
        self.assertRaises(TypeError, anagramm, {}, {})

    def test_count_letters_if_string(self):
        self.assertEqual(count_letters('kutule'), {'k':1,'u':2,'t':1,'l':1,'e':1})
        self.assertEqual(count_letters(' ?.,;!'), {})
    def test_count_letters_input_type(self):
        self.assertRaises(TypeError, count_letters, [])
        self.assertRaises(TypeError, count_letters, {})
        self.assertRaises(TypeError, count_letters, 12)
if __name__ == '__main__':
    unittest.main()
