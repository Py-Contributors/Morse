import sys
import unittest

sys.path.append('.')
from morse.main import Morse
m = Morse()


class MorseTest(unittest.TestCase):
    
    def test_encode_morse(self):
        self.assertEqual(m.encode_morse('HELLO'), '.... . .-.. .-.. ---')
        self.assertEqual(m.encode_morse('HELLO123'), '.... . .-.. .-.. --- .---- ..--- ...--')
        self.assertEqual(m.encode_morse('HELLO123!'), '.... . .-.. .-.. --- .---- ..--- ...-- !')
    
    def test_decode_morse(self):
        self.assertEqual(m.decode_morse('.... . .-.. .-.. ---'), 'hello')
        self.assertEqual(m.decode_morse('.... . .-.. .-.. --- .---- ..--- ...--'), 'hello123')
        self.assertEqual(m.decode_morse('.... . .-.. .-.. --- .---- ..--- ...-- !'), 'hello123!')

    def test_binary_to_morse(self):
        self.assertEqual(m.binary_to_morse('101010'), '-.-.-.')
        self.assertEqual(m.binary_to_morse('010101'), '.-.-.-')
        self.assertEqual(m.binary_to_morse('1010101010'), '-.-.-.-.-.')
        self.assertEqual(m.binary_to_morse(101010101), '-.-.-.-.-')

    def test_morse_to_binary(self):
        self.assertEqual(m.morse_to_binary('-.-.-.'), '101010')
        self.assertEqual(m.morse_to_binary('.-.-.-'), '010101')
        self.assertEqual(m.morse_to_binary('-.-.-.-.-.'), '1010101010')


if __name__ == '__main__':
    unittest.main()
