import openal

# Inicializar OpenAL
openal.oalInit()

# Establecer la posición del oyente
openal.Listener.position = (0, 0, 0)
openal.Listener.orientation = ((0, 0, -1), (0, 1, 0))

# Abrir el archivo de sonido
sound = openal.oalOpen("C:/Users/USER/OneDrive/Documentos/Universidad Javeriana/S8/SI2/SI-Proyecto2/Sonidos/disparo-mono.wav")

# Ajustar el volumen (ganancia) de la fuente
sound.set_gain(0.08)

# Establecer la posición de la fuente de sonido en 3D
sound.set_position((10, 0, 0))  # 1 unidad a la derecha del oyente

# Reproducir el sonido
sound.play()

# Esperar a que el sonido termine de reproducirse
while sound.get_state() == openal.AL_PLAYING:
    pass

# Cerrar el dispositivo OpenAL
openal.oalQuit()
