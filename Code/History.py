import time
import sys

class History:
    def __init__(self, dialogo, sonido, opciones):
        self.dialogo = dialogo
        self.sonido = sonido
        self.opciones = opciones
        
    def get_text(self):
        text = self.dialogo
        for opcion in self.opciones:
            text = f'\n{opcion}. '.join([text, self.opciones[opcion]['text']])
        return text
    
    def get_next_history_part(self, key_option):
        return self.opciones[key_option]["siguiente"]
    
    def print_story(self):
        for char in self.get_text():
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.03)
        print()