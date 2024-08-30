from dotenv import load_dotenv
import openal
import os
load_dotenv()
path = os.getenv("RUTA")

class Sonido:
  def __init__(self, sonido):
    openal.oalInit()
    self.buffer = openal.oalOpen('/'.join([path, sonido]))
  
  def configuracion(self, posicion, ganancia, velocidad):
    self.buffer.set_position(posicion)
    self.buffer.set_gain(ganancia)
    self.buffer.set_velocity(velocidad)
  
  def reproducir(self):
    self.buffer.play()
    while self.buffer.get_state() == openal.AL_PLAYING:
      pass
    openal.oalQuit()