from morseify.utils import load_config
morse_mapping_json = load_config('morse_mapping.json')


class Morseify(object):
    """ Morseify class to convert text to morse code and vice versa 
    
    Attributes:

        character_mapping (dict): A dictionary mapping characters to morse code
        reverse_character_mapping (dict): A dictionary mapping morse code to characters
        binary_mapping (dict): A dictionary mapping binary to morse code
        reverse_binary_mapping (dict): A dictionary mapping morse code to binary

    Methods:
    
        binary_to_morse(binary): A method to convert binary to morse code
        morse_to_binary(morse_code): A method to convert morse code to binary
        encode_morse(text): A method to convert text to morse code
        decode_morse(morse_code): A method to convert morse code to text

    """
    def __init__(self):
        self.character_mapping = {**morse_mapping_json['morse_mapping'], **{k.lower(): v for k, v in \
                                morse_mapping_json['morse_mapping'].items()}}
        self.reverse_character_mapping = {v: k for k, v in self.character_mapping.items()}
        self.binary_mapping = morse_mapping_json['binary_mapping']
        self.reverse_binary_mapping = {v: k for k, v in self.binary_mapping.items()}

    def binary_to_morse(self, binary):
        binary_string = str(binary)
        return "".join([self.binary_mapping[char] for char in binary_string \
                        if char in self.binary_mapping])

    def morse_to_binary(self, morse_code):
        return "".join([self.reverse_binary_mapping[char] for char in morse_code \
                        if char in self.reverse_binary_mapping])

    def encode_morse(self, text):
        return ' '.join([self.character_mapping[char] if char in self.character_mapping \
                         else char for char in text])

    def decode_morse(self, morse_code):
        return ''.join([self.reverse_character_mapping[char].lower() if char in self.reverse_character_mapping \
                        else char for char in morse_code.split()])

    def __version__(self):
        return '1.0.0'
