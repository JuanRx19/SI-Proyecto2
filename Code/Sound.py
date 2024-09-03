from dotenv import load_dotenv
import openal
import os
load_dotenv()
path = os.path.abspath(os.getenv("sounds_path"))

class Sound:
  def __init__(self, name, posicion, ganancia, velocidad):
    self.buffer = openal.oalOpen('/'.join([path, name]))
    self.buffer.set_position(posicion)
    self.buffer.set_gain(ganancia)
    self.buffer.set_velocity(velocidad)
  
  def play(self):
    self.buffer.play()
    while self.buffer.get_state() == openal.AL_PLAYING:
      pass