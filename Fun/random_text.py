from time import sleep as z
from colorama import Fore as q, Style as p
import numpy as np
import random

def add_noise():
    return random.choice(["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", ";", ":", "'", "\"", "<", ">", ",", ".", "/", "?", "|", "\\"])

def reverse_string(text):
    return text[::-1]

def shuffle_string(text):
    text_list = list(text)
    random.shuffle(text_list)
    return ''.join(text_list)

def capitalize_text(text):
    return text.upper()

def generate_random_string(length):
    return ''.join(random.choices("abcdefghijklmnopqrstuvwxyz", k=length))

class TextManipulator:
    def __init__(self, text):
        self.text = text
        self.alphabet = Alphabet().generate()

    def process_text(self):
        accumulator = Accumulator()
        accumulator.set_text(self.text)
        accumulator.set_alphabet(self.alphabet)

        while not accumulator.is_complete():
            accumulator.process_next()

class Accumulator:
    def __init__(self):
        self.text = ""
        self.alphabet = np.array([])
        self.current_text_index = 0
        self.current_alpha_index = 0

    def set_text(self, text):
        self.text = text

    def set_alphabet(self, alphabet):
        self.alphabet = alphabet

    def is_complete(self):
        return self.current_text_index >= len(self.text)

    def process_next(self):
        current_char = self.text[self.current_text_index]
        current_alpha = self.alphabet[self.current_alpha_index]

        self.add_sleep()
        self.print_alpha(current_alpha)
        
        if self.check_condition(current_alpha, current_char):
            self.current_text_index += 1
            self.current_alpha_index = 0
        else:
            if self.current_alpha_index == len(self.alphabet) - 1:
                self.current_alpha_index = 0
                self.current_text_index += 1
            else:
                self.current_alpha_index += 1

    def add_sleep(self):
        z(1 / 10)

    def print_alpha(self, alpha):
        if self.current_text_index < len(self.text) - 1:
            formatted_string = q.GREEN + p.BRIGHT + self.text[:self.current_text_index] + alpha + add_noise() + p.RESET_ALL
        else:
            formatted_string = q.GREEN + p.BRIGHT + self.text[:self.current_text_index] + alpha + p.RESET_ALL
        print(formatted_string, end="\r")

    def check_condition(self, alpha, char):
        return alpha == char

class Alphabet:
    def generate(self):
        return np.array([chr(x) for x in range(97, 123)])

class Text:
    def __init__(self, ascii_values):
        self.content = ''.join([chr(x) for x in ascii_values])

text_obj = Text([104, 101, 108, 108, 111, 32, 119, 111, 114, 108, 100])
manipulator = TextManipulator(text_obj.content)
manipulator.process_text()
