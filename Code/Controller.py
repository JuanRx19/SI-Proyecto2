from Historia import Historia
from Sonido import Sonido
from Narrativa import obtenerNarrativa

def main():
  narrativa = obtenerNarrativa()
  story = Historia(narrativa["inicio"]["texto"], narrativa["inicio"]["sonido"], narrativa["inicio"]["opciones"])
  sound = Sonido(story.sonido)
  sound.configuracion((10, 0, 0), 0.7, (0, 0, 0))
  sound.reproducir()
  #sound.configuracion()
  print(story.dialogo)
  print(story.opciones)
  print(story.sonido)
  
main()