import openal

class SoundConfigure:
  def __init__(self, sounds):
    self.sounds = sounds
    
  def play(self):
    for sound in self.sounds:
        sound.buffer.play()
    
    # Mantener el programa en ejecución hasta que todos los sonidos hayan terminado
    while any(sound.buffer.get_state() == openal.AL_PLAYING for sound in self.sounds):
        pass