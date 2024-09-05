import time
import sys

class History:
    def __init__(self, dialog, sounds, options):
        self.dialog = dialog
        self.sounds = sounds
        self.options = options
        
    def get_text(self):
        text = self.dialog
        for option in self.options:
            text = f'\n{option}. '.join([text, self.options[option]['text']])
        return text
    
    def get_next_history_part(self, key_option):
        return self.options[key_option]["siguiente"]
    
    def print_story(self):
        for char in self.get_text():
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.03)
        print()