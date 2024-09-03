from dotenv import load_dotenv
import openal
import os
load_dotenv()
path = os.path.abspath(os.getenv("sounds_path"))

class Sound:
  def __init__(self, sonido, posicion, ganancia, velocidad):
    openal.oalInit()
    self.buffer = openal.oalOpen('/'.join([path, sonido]))
    self.buffer.set_position(posicion)
    self.buffer.set_gain(ganancia)
    self.buffer.set_velocity(velocidad)
  
  def reproducir(self):
    self.buffer.play()
    while self.buffer.get_state() == openal.AL_PLAYING:
      pass
    openal.oalQuit()