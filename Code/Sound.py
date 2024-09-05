from dotenv import load_dotenv
import openal
import os
load_dotenv()
path = os.path.abspath(os.getenv("sounds_path"))

class Sound:
  def __init__(self, name, posicion, ganancia, velocidad):
    self.buffer = openal.oalOpen('/'.join([path, f"[MONO] {name}"]))
    self.buffer.set_position(posicion)
    self.buffer.set_gain(ganancia)
    self.buffer.set_velocity(velocidad)
    
  def play_in_loop(self):
    self.buffer.set_looping(True)
    self.buffer.play()