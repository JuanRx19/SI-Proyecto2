def get_narrative():
  history = {
    "inicio": {
        "text": "Te encuentras en un bosque oscuro. A tu izquierda hay un sendero, y a tu derecha un río.",
        "sounds": "disparo-mono.wav",
        "sounds_config": [(0, 0, 10), 0.3, (0, 0, 0)],
        "options": {
            1: {"text": "Tomar el sendero", "siguiente": "sendero"},
            2: {"text": "Ir al río", "siguiente": "rio"}
        },
    
    },
    "sendero": {
        "text": "Caminas por el sendero y llegas a una cueva. Escuchas ruidos extraños desde adentro.",
        "sounds": "disparo-mono.wav",
        "sounds_config": [(10, 0, 0), 0.7, (0, 0, 0)],
        "options": {
            1: {"text": "Entrar a la cueva", "siguiente": "cueva"},
            2: {"text": "Regresar al bosque", "siguiente": "inicio"},
            3: {"text": "Ir hacia el mar", "siguiente": "final"}
        }
    },
    "rio": {
        "text": "Te acercas al río y ves un puente roto.",
        "sounds": "disparo-mono.wav",
        "sounds_config": [(10, 0, 0), 0.7, (0, 0, 0)],
        "options": {
            1: {"text": "Cruzar el puente", "siguiente": "puente"},
            2: {"text": "Volver al bosque", "siguiente": "inicio"}
        }
    },
    # Agrega más nodos de historia según sea necesario
  }
  return history