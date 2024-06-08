from morse.utils import load_config
morse_mapping_json = load_config('morse_mapping.json')


class Morse(object):
    def __init__(self):
        self.character_mapping = {**morse_mapping_json['morse_mapping'], **{k.lower(): v for k, v in \
                                morse_mapping_json['morse_mapping'].items()}}
        self.reverse_character_mapping = {v: k for k, v in self.character_mapping.items()}
        self.binary_mapping = morse_mapping_json['binary_mapping']
        self.reverse_binary_mapping = {v: k for k, v in self.binary_mapping.items()}

    def binary_to_morse(self, binary):
        binary_string = str(binary)
        return "".join([self.binary_mapping[char] for char in binary_string])

    def morse_to_binary(self, morse_code):
        return "".join([self.reverse_binary_mapping[char] for char in morse_code])

    def encode_morse(self, text):
        return ' '.join([self.character_mapping[char] if char in self.character_mapping \
                         else char for char in text])

    def decode_morse(self, morse_code):
        return ''.join([self.reverse_character_mapping[char].lower() if char in self.reverse_character_mapping \
                        else char for char in morse_code.split()])
