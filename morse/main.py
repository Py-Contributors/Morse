import sys
sys.path.append('.')
from morse.utils import load_config

morse_mapping = load_config('morse_mapping.json')

alpha_to_morse_mapping = morse_mapping['alpha_to_morse_mapping']
number_to_morse_mapping = morse_mapping['number_to_morse_mapping']
morse_to_alpha_mapping = {v: k for k, v in alpha_to_morse_mapping.items()}
morse_to_number_mapping = {v: k for k, v in number_to_morse_mapping.items()}

class Morse(object):
    def __init__(self):
        pass
    
    def binary_to_morse(self, binary):
        morse_code = []
        for char in binary:
            if char == '1':
                morse_code.append('-')
            elif char == '0':
                morse_code.append('.')
        return ''.join(morse_code)
    
    def morse_to_binary(self, morse_code):
        binary = []
        for char in morse_code:
            if char == '-':
                binary.append('1')
            elif char == '.':
                binary.append('0')
        return ''.join(binary)

    def encode_morse(self, text):
        morse_code = []
        for char in text:
            if char.isalpha():
                morse_code.append(alpha_to_morse_mapping[char.upper()])
            elif char.isdigit():
                morse_code.append(number_to_morse_mapping[char])
            else:
                morse_code.append(char)
        return ' '.join(morse_code)
    
    def decode_morse(self, morse_code):
        text = []
        for char in morse_code.split(' '):
            if char in morse_to_alpha_mapping:
                text.append(morse_to_alpha_mapping[char])
            elif char in morse_to_number_mapping:
                text.append(morse_to_number_mapping[char])
            else:
                text.append(char)
        return ''.join(text)

            
    def encode_morse_to_audio(self, text, output_file_path):
        morse_code = self.encode_morse(text)
        # for char in morse_code:
        #     if char == '.':
        #         playsound('src/sounds/dit.wav')
        #     elif char == '-':
        #         playsound('src/sounds/dah.wav')
        #     elif char == ' ':
        #         playsound('src/sounds/short_pause.wav')
        #     else:
        #         playsound('src/sounds/long_pause.wav')
        
