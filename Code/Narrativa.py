def obtenerNarrativa():
  historia = {
    "inicio": {
        "texto": "Te encuentras en un bosque oscuro. A tu izquierda hay un sendero, y a tu derecha un río.",
        "sonido": "disparo-mono.wav",
        "opciones": {
            1: {"texto": "Tomar el sendero", "siguiente": "sendero"},
            2: {"texto": "Ir al río", "siguiente": "rio"}
        }
    },
    "sendero": {
        "texto": "Caminas por el sendero y llegas a una cueva. Escuchas ruidos extraños desde adentro.",
        "sonido": "sonido_cueva.wav",
        "opciones": {
            1: {"texto": "Entrar a la cueva", "siguiente": "cueva"},
            2: {"texto": "Regresar al bosque", "siguiente": "inicio"}
        }
    },
    "rio": {
        "texto": "Te acercas al río y ves un puente roto.",
        "sonido": "sonido_rio.wav",
        "opciones": {
            1: {"texto": "Cruzar el puente", "siguiente": "puente"},
            2: {"texto": "Volver al bosque", "siguiente": "inicio"}
        }
    },
    # Agrega más nodos de historia según sea necesario
  }
  return historia