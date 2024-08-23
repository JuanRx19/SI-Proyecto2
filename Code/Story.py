import openal

# Abrir el archivo de sonido
sound = openal.oalOpen("C:/Users/juanr/Documents/SI-Proyecto2/Sonidos/disparo.wav")
sound.set_gain(0.08)
sound.set_position((10, 0, 0))  # Posición a la derecha

sound.play()

# Esperar a que el sonido termine de reproducirse
while sound.get_state() == openal.AL_PLAYING:
    pass

# Cerrar el dispositivo OpenAL
openal.oalQuit()
