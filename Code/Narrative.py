from Sound import Sound
from SoundConfigure import SoundConfigure
def get_narrative():
  history = {
    "inicio": {
        "text": "Te despiertas en un claro desconocido de un bosque espeso. El aire está cargado de misterio, y el silencio es roto por un lejano murmullo.",
        "sounds_config": SoundConfigure([Sound("murmullo-agua.wav", (-3, 0, 0), 0.5, (0, 0, 0)), Sound("sonido-hojas.wav", (10, 0, 0), 0.5, (0, 0, 0))]),
        "options": {
            1: {"text": "Explorar el bosque", "siguiente": "bosque"},
            2: {"text": "Permanecer en el claro", "siguiente": "claro"}
        },
    },
    "bosque": {
        "text": "Caminas por el bosque y, entre los árboles, vislumbras una figura encapuchada. Parece observarte desde lejos.",
        "sounds_config": "El crujido de las hojas bajo tus pies y un susurro que parece provenir de la figura.",
        "options": {
            1: {"text": "Acercarte a la figura", "siguiente": "acercarse"},
            2: {"text": "Esconderte y observar", "siguiente": "esconderse"}
        }
    },
    "acercarse": {
        "text": "Te acercas a la figura, que revela ser un guardián del bosque. Te advierte sobre los peligros que te esperan si sigues adelante.",
        "sounds_config": "La voz grave del guardián mezclada con el eco de su advertencia.",
        "options": {
            1: {"text": "Aceptar el consejo y retroceder", "siguiente": "retroceder"}
        }
    },
    "retroceder": {
        "text": "Decides retroceder, pero el guardián te detiene y te ofrece una misión: encontrar un objeto sagrado perdido en el bosque.",
        "sounds_config": "Un susurro bajo que se convierte en un eco envolvente.",
        "options": {
            1: {"text": "Aceptar la misión", "siguiente": "aceptarMision"}
        }
    },
    "aceptarMision": {
        "text": "El guardián te entrega un mapa antiguo y te indica la dirección del objeto sagrado. Sigues su consejo y te adentras más en el bosque.",
        "sounds_config": "El sonido del mapa desplegándose y el crujido de ramas mientras caminas.",
        "options": {
            1: {"text": "Continuar hacia el objeto", "siguiente": "continuarObjeto"}
        }
    },
    "continuarObjeto": {
        "text": "Siguiendo el mapa, llegas a una encrucijada. Un camino lleva a un río caudaloso, mientras que el otro parece desaparecer en la espesura del bosque, pero sientes que el río es tu única opción segura.",
        "sounds_config": "El sonido del agua fluyendo con fuerza, mezclado con el crujido de ramas bajo tus pies.",
        "options": {
            1: {"text": "Cruzar el río", "siguiente": "rio"}
        }
    },
    "rio": {
        "text": "Decides cruzar el río caudaloso. La corriente es fuerte, y el cruce es peligroso, pero logras llegar al otro lado. Allí, encuentras un camino que lleva a una cascada con un antiguo templo oculto detrás.",
        "sounds_config": "El rugido de la cascada y el susurro de la corriente del río.",
        "options": {
            1: {"text": "Entrar en el templo", "siguiente": "templo"}
        }
    },
    "templo": {
        "text": "Entras en el templo y descubres un altar cubierto de inscripciones antiguas. Un sacerdote fantasma aparece y te pide que demuestres tu devoción para obtener el objeto sagrado.",
        "sounds_config": "El susurro del sacerdote y un suave canto ritual en la distancia.",
        "options": {
            1: {"text": "Ofrecer una oración en el altar", "siguiente": "oración"},
            2: {"text": "Intentar tomar el objeto sin más", "siguiente": "tomarObjeto"}
        }
    },
    "oracion": {
        "text": "Te arrodillas y ofreces una oración sincera. El sacerdote sonríe y el altar se abre, revelando el objeto sagrado. (FINAL EXITOSO)",
        "sounds_config": "Un sonido suave y celestial mientras el altar se abre, revelando el objeto.",
        "options": {}
    },
    "tomarObjeto": {
        "text": "Ignoras al sacerdote y te lanzas a tomar el objeto. De repente, una trampa se activa y el suelo bajo tus pies empieza a colapsar.",
        "sounds_config": "El ruido de piedras cayendo y el sonido del templo desmoronándose.",
        "options": {
            1: {"text": "Escapar del templo", "siguiente": "escaparTemplo"}
        }
    },
    "escaparTemplo": {
        "text": "Logras escapar del templo a tiempo, pero el objeto sagrado se pierde para siempre bajo los escombros. (FINAL INTERMEDIO)",
        "sounds_config": "Un último estruendo cuando el templo se derrumba completamente, seguido de un silencio.",
        "options": {} 
    },
    "esconderse": {
        "text": "Te ocultas detrás de un árbol y observas a la figura. De repente, desaparece en un destello de luz.",
        "sounds_config": "Un destello brillante seguido por el susurro de hojas en el viento.",
        "options": {
            1: {"text": "Continuar explorando", "siguiente": "continuarExplorando"}
        }
    },
    "continuarExplorando": {
        "text": "Tras la desaparición de la figura, te adentras más en el bosque. El ambiente se vuelve más denso, y los sonidos de la naturaleza se intensifican.",
        "sounds_config": "El sonido de hojas crujientes y el canto lejano de aves nocturnas.",
        "options": {
            1: {"text": "Seguir adelante", "siguiente": "cueva"}
        }
    },
    "cueva": {
        "text": "Al final del camino, llegas a la entrada de una cueva oscura. Te sientes atraído por la oscuridad, pero también sientes una presencia inquietante.",
        "sounds_config": "Un eco profundo y un susurro inquietante desde el interior de la cueva.",
        "options": {
            1: {"text": "Entrar en la cueva", "siguiente": "entrarCueva"},
            2: {"text": "Retroceder", "siguiente": "aDormir"}
        }
    },
    "claro": {
        "text": "Decides quedarte en el claro y escuchar. A lo lejos, escuchas el murmullo de agua y el crujido de ramas. Al mismo tiempo, sientes una vibración en el suelo.",
        "sounds_config": "Sonidos de agua corriendo y un bajo zumbido que parece venir de debajo de ti.",
        "options": {
            1: {"text": "Investigar el murmullo de agua", "siguiente": "agua"},
            2: {"text": "Investigar la vibración en el suelo", "siguiente": "suelo"}
        }
    },
    "agua": {
        "text": "Sigues el sonido del agua y llegas a un pequeño arroyo. Ves algo moviéndose bajo la superficie.",
        "sounds_config": "El suave burbujeo del agua, con un tenue chapoteo que viene de un objeto sumergido.",
        "options": {
            1: {"text": "Meter la mano en el agua", "siguiente": "manoAgua"},
            2: {"text": "Evitar el arroyo y seguir explorando", "siguiente": "aDormir"}
        }
    },
    "aDormir": {
        "text": "Después de horas de caminar sin rumbo, te das cuenta de que el bosque te ha guiado de regreso al claro donde todo comenzó. Exhausto y sin respuestas, decides que lo mejor es dejar todo atrás. Te acuestas sobre la suave hierba y, mientras el cielo oscurece, cierras los ojos, dejándote llevar por el sueño. (FINAL INTERMEDIO)",
        "sounds_config": "El susurro del viento y el crujir de las hojas se desvanecen lentamente, dejando solo el tranquilo murmullo de la noche.",
        "options": {}  # No hay más opciones, ya que es un final intermedio.
    },
    "manoAgua": {
        "text": "Al meter la mano en el agua, sientes algo frío y metálico. Al sacarlo, descubres una llave antigua.",
        "sounds_config": "El tintineo de metal al extraer la llave del agua.",
        "options": {
            1: {"text": "Continuar", "siguiente": "continuarLlave"}
        }
    },
    "continuarLlave": {
        "text": "Guardas la llave y sigues explorando. El sonido del agua queda atrás, y el bosque se cierra a tu alrededor.",
        "sounds_config": "El murmullo del agua se desvanece, dejando solo el susurro del viento entre los árboles.",
        "options": {
            1: {"text": "Seguir avanzando", "siguiente": "cuevaLlave"}
        }
    },
    "cuevaLlave": {
        "text": "El camino te lleva a una colina rocosa. Al llegar a la cima, ves una estructura antigua a lo lejos. Decides explorar la estructura.",
        "sounds_config": "El viento sopla con fuerza en la cima de la colina, y un eco distante proviene de la estructura.",
        "options": {
            1: {"text": "Buscar la entrada", "siguiente": "entradaCueva"}
        }
    },
    "entradaCueva": {
        "text": "Te acercas a la estructura y descubres una entrada oculta entre las rocas. Parece que la llave encajaría en la cerradura.",
        "sounds_config": "Sonido de caminar",
        "options": {
            1: {"text": "Usar la llave", "siguiente": "entrarCueva"}
        }
    },
    "entrarCueva": {
        "text": "La puerta se abre, revelando un pasaje que lleva a una cámara interior. Allí, te encuentras con un ser anciano que custodia el lugar.",
        "sounds_config": "Puerta abriendose",
        "options": {
            1: {"text": "Hablar con el anciano", "siguiente": "hablarAnciano"}
        }
    },
    "hablarAnciano": {
        "text": "El anciano te dice que solo quienes demuestren su valentía y sabiduría pueden reclamar el tesoro. Te ofrece una prueba: responder un enigma o enfrentarlo en combate.",
        "sounds_config": "La voz del anciano reverbera en la cámara, mientras se escuchan susurros de fuerzas místicas a tu alrededor.",
        "options": {
            1: {"text": "Aceptar el enigma", "siguiente": "enigma"},
            2: {"text": "Aceptar el combate", "siguiente": "combate"}
        }
    },
    "enigma": {
        "text": "El anciano sonríe de forma burlona y pregunta: 'Me puedes romper sin tocarme. Puedes perderme sin querer. Me puedes guardar, pero nunca verme. ¿Qué soy?'",
        "sounds_config": "Un susurro suave, como si las palabras del anciano resonaran en tu mente.",
        "options": {
            1: {"text": "Responder: 'Una promesa'", "siguiente": "promesa"},
            2: {"text": "Responder: 'Una sombra'", "siguiente": "sombra"}
        }
    },
    "sombra": {
        "text": "Respondes 'Una sombra'. El anciano niega con la cabeza. 'Una sombra no se puede guardar ni romper,' dice, y la luz en la sala se atenúa, sumiéndote en la oscuridad. (FINAL FALLIDO)",
        "sounds_config": "Un apagón repentino de la luz, acompañado de un silencio opresivo.",
        "options": {}  # No hay más opciones, ya que es un final fallido.
    },
    "promesa": {
        "text": "Resuelves el enigma con éxito. El anciano sonríe y te permite acceder al tesoro oculto en la cámara. (FINAL EXITOSO)",
        "sounds_config": "Un sonido brillante y resonante, como una campana, cuando se revela el tesoro.",
        "options": {}  # No hay más opciones, ya que es un final exitoso.
    },
    "combate": {
        "text": "El anciano adopta una postura de combate y te desafía. 'Solo el más fuerte merece el tesoro,' dice mientras una energía oscura envuelve sus manos. ¿Qué harás?",
        "sounds_config": "Un crescendo de tambores y un zumbido bajo que indica la preparación para la batalla.",
        "options": {
            1: {"text": "Lanzar un ataque rápido", "siguiente": "ataqueRapido"},
            2: {"text": "Esperar y defenderse de su movimiento", "siguiente": "defenderse"}
        }
    },
    "ataqueRapido": {
        "text": "Atacas rápidamente con una ráfaga de energía, golpeando al anciano antes de que pueda reaccionar. Sin embargo, él se recupera rápidamente y te lanza un rayo de energía oscura.",
        "sounds_config": "El sonido de un choque de energía y el crepitar de la magia oscura del anciano.",
        "options": {
            1: {"text": "Esquivar el rayo", "siguiente": "rayo"},
            2: {"text": "Contraatacar con un ataque más fuerte", "siguiente": "contraatacar"}
        }
    },
    "rayo": {
        "text": "Logras esquivar el rayo por poco, sintiendo el calor oscuro pasar rozando tu rostro. El anciano sonríe, admirando tu velocidad.",
        "sounds_config": "El silbido del rayo pasando y un leve eco de la risa del anciano.",
        "options": {
            1: {"text": "Usar un ataque final", "siguiente": "ataqueFinal"},
            2: {"text": "Esperar el próximo movimiento del anciano", "siguiente": "esperarMovimiento"}
        }
    },
    "contraatacar": {
        "text": "Realizas un contraataque para anular el rayo de energía oscura que el anciano te había lanzado. El anciano sonríe, admirando tu velocidad.",
        "sounds_config": "El silbido del rayo pasando y un leve eco de la risa del anciano.",
        "options": {
            1: {"text": "Usar un ataque final", "siguiente": "ataqueFinal"},
            2: {"text": "Esperar el próximo movimiento del anciano", "siguiente": "esperarMovimiento"}
        }
    },
    "ataqueFinal": {
        "text": "Concentrando toda tu energía, lanzas un ataque final devastador. El anciano se confía e intenta bloquearlo, pero el poder es demasiado. El anciano cae al suelo, derrotado.",
        "sounds_config": "Un estallido ensordecedor seguido de un silencio repentino mientras la energía se disipa.",
        "options": {
            1: {"text": "Recibir el tesoro", "siguiente": "tesoro"}
        }
    },
    "esperarMovimiento": {
        "text": "Decides esperar, pero el anciano aprovecha tu vacilación. Con un movimiento rápido, lanza un hechizo que te inmoviliza. 'No deberías haber dudado,' dice antes de lanzarte al abismo. (FINAL FALLIDO)",
        "sounds_config": "Un sonido de cadenas cerrándose y el eco de la voz del anciano mientras te lanza a la oscuridad.",
        "options": {}  # No hay más opciones, ya que es un final fallido.
    },
    "defenderse": {
        "text": "Adoptas una postura defensiva, preparado para lo que venga. El anciano lanza un hechizo de parálisis hacia ti, pero tu defensa te protege parcialmente. Aún sientes un leve entumecimiento en tus extremidades.",
        "sounds_config": "Un zumbido bajo mientras el hechizo se despliega y un leve crujido mientras intentas sacudirte el entumecimiento.",
        "options": {
            1: {"text": "Romper la parálisis con un contraataque", "siguiente": "paralisis"},
            2: {"text": "Esperar a que el anciano se acerque", "siguiente": "ancianoAcerque"}
        }
    },
    "paralisis": {
        "text": "Con gran esfuerzo, reúnes tu energía y lanzas un contraataque que rompe la parálisis. El anciano se sorprende por tu determinación, retrocediendo un paso.",
        "sounds_config": "El estallido de energía cuando rompes el hechizo, seguido de un susurro de viento cuando el anciano retrocede.",
        "options": {
            1: {"text": "Aprovechar para atacar de nuevo", "siguiente": "atacarDeNuevo"},
            2: {"text": "Mantener la defensa y observar", "siguiente": "mantenerDefensa"}
        }
    },
    "ancianoAcerque": {
        "text": "Sorprendentemente, el aturdimiento se te va rápido. Sin embargo, esperas que el anciano se acerque para atacarlo rápido. El anciano se sorprende por tu determinación, retrocediendo un paso.",
        "sounds_config": "El estallido de energía cuando rompes el hechizo, seguido de un susurro de viento cuando el anciano retrocede.",
        "options": {
            1: {"text": "Aprovechar para atacar de nuevo", "siguiente": "atacarDeNuevo"},
            2: {"text": "Mantener la defensa y observar", "siguiente": "mantenerDefensa"}
        }
    },
    "atacarDeNuevo": {
        "text": "Aprovechas la vacilación del anciano y lanzas un poderoso ataque. El anciano, sin tiempo para reaccionar, es golpeado de lleno y cae, derrotado.",
        "sounds_config": "Un estruendo de poder seguido por el sonido sordo del anciano cayendo al suelo.",
        "options": {
            1: {"text": "Recibir el tesoro", "siguiente": "tesoro"}
        }
    },
    "mantenerDefensa": {
        "text": "Decides mantenerte en guardia, pero el anciano percibe tu pasividad como debilidad. Con un gesto rápido, te envuelve en sombras que te sofocan lentamente. 'No siempre la paciencia es una virtud,' murmura el anciano mientras te absorben las sombras. (FINAL FALLIDO)",
        "sounds_config": "Un sonido de sombras envolventes y un susurro final mientras la oscuridad te consume.",
        "options": {}  # No hay más opciones, ya que es un final fallido.
    },
    "tesoro": {
        "text": "Tras una feroz batalla, logras derrotar al anciano. Él, en su derrota, te entrega el tesoro y te advierte que su poder te acompañará. (FINAL EXITOSO)",
        "sounds_config": "Un eco de victoria y un suave zumbido que indica que has adquirido un gran poder.",
        "options": {}  # No hay más opciones, ya que es un final exitoso.
    },
    "suelo": {
        "text": "Sigues la vibración y descubres una piedra grande que emite un leve resplandor. Al tocarla, sientes una conexión con algo profundo en el bosque.",
        "sounds_config": "Un zumbido profundo y el crujido de la piedra bajo tus dedos.",
        "options": {
            1: {"text": "Levantar la piedra", "siguiente": "cogerPiedra"},
            2: {"text": "Dejar la piedra y seguir adelante", "siguiente": "dejarPiedra"}
        }
    },
    "dejarPiedra": {
        "text": "Después de dejar la piedra, caminas por horas sin rumbo, te das cuenta de que el bosque te ha guiado de regreso al claro donde todo comenzó. Exhausto y sin respuestas, decides que lo mejor es dejar todo atrás. Te acuestas sobre la suave hierba y, mientras el cielo oscurece, cierras los ojos, dejándote llevar por el sueño. (FINAL INTERMEDIO)",
        "sounds_config": "El susurro del viento y el crujir de las hojas se desvanecen lentamente, dejando solo el tranquilo murmullo de la noche.",
        "options": {}  # No hay más opciones, ya que es un final intermedio.
    },
    "cogerPiedra": {
        "text": "Al levantar la piedra, descubres un pasaje que conduce a un túnel oscuro. Sientes un viento helado que emana de su interior.",
        "sounds_config": "El eco de la piedra al caer y el viento soplando desde el túnel.",
        "options": {
            1: {"text": "Continuar por el túnel", "siguiente": "tunel"}
        }
    },
    "tunel": {
        "text": "Sigues el túnel hasta llegar a una cámara subterránea. En el centro, un altar rodeado de inscripciones antiguas. Un ser etéreo aparece y te habla.",
        "sounds_config": "Un susurro distante que crece en intensidad y se convierte en una voz que resuena en la cámara.",
        "options": {
            1: {"text": "Escuchar al ser", "siguiente": "escucharSer"},
            2: {"text": "Intentar atacar al ser", "siguiente": "atacarSer"}
        }
    },
    "escucharSer": {
        "text": "El ser etéreo te dice que para acceder al tesoro debes probar tu valía completando una tarea: resolviendo un enigma que ha trascendido por generaciones.",
        "sounds_config": "La voz del ser se desvanece, dejando solo un eco que te guía hacia la salida.",
        "options": {
            1: {"text": "Aceptar la tarea", "siguiente": "aceptarTarea"}
        }
    },
    "aceptarTarea": {
        "text": "El espíritu te plantea el enigma: 'Soy siempre visible, pero rara vez me ves. No tengo forma, pero mi presencia se siente. Puedo reflejarte, pero no soy un espejo. ¿Qué soy?'",
        "sounds_config": "Un susurro inquietante, como si el espíritu esperara ansioso tu respuesta.",
        "options": {
            1: {"text": "Responder: 'La sombra'", "siguiente": "sombra"},
            2: {"text": "Responder: 'El viento'", "siguiente": "viento"}
        }
    },
    "viento": {
        "text": "Decides responder 'El viento'. El espíritu sonríe de manera siniestra, y la cueva comienza a temblar. 'Incorrecto,' susurra. 'Ahora te enfrentarás a mi ira.' (FINAL FALLIDO)",
        "sounds_config": "Un eco oscuro y el sonido de rocas derrumbándose mientras la cueva comienza a colapsar.",
        "options": {}  # No hay más opciones, ya que es un final fallido.
    },
    "sombra": {
        "text": "Resuelves el enigma con éxito. El espíritu sonríe levemente mientras desaparece y te permite acceder al tesoro oculto en la cámara. (FINAL EXITOSO)",
        "sounds_config": "Un sonido brillante y resonante, como una campana, cuando se revela el tesoro.",
        "options": {}  # No hay más opciones, ya que es un final exitoso.
    },
    "atacarSer": {
        "text": "Intentas atacar al ser, pero tu ataque atraviesa su forma etérea. El ser se enfurece y comienza a atacarte con energía oscura.",
        "sounds_config": "El choque de energías y un rugido de ira del ser.",
        "options": {
            1: {"text": "Intentar un ataque directo con tu arma", "siguiente": "ataqueArma"},
            2: {"text": "Buscar una manera de usar el entorno a tu favor", "siguiente": "usarEntorno"},
            3: {"text": "Retroceder y esquivar sus ataques", "siguiente": "esquivarAtaques"}
        }
    },
    "ataqueArma": {
        "text": "Lanzas un ataque directo con tu arma, pero atraviesa al ser sin causarle daño. El ser te ataca con una ráfaga de energía oscura. (FINAL FALLIDO)",
        "sounds_config": "Un estallido de energía oscura y el eco de tu caída.",
        "options": {}  # No hay más opciones, ya que es un final fallido.
    },
    "usarEntorno": {
        "text": "Observas la cámara y notas que las inscripciones en las paredes parecen brillar cuando el ser se acerca. Podrían ser clave para derrotarlo.",
        "sounds_config": "Un zumbido creciente cuando te acercas a las inscripciones y el rugido frustrado del ser.",
        "options": {
            1: {"text": "Intentar usar las inscripciones", "siguiente": "usarInscripciones"}
        }
    },
    "usarInscripciones": {
        "text": "Decides utilizar las inscripciones en las paredes. Al tocarlas, emiten una luz intensa que hiere al ser etéreo.",
        "sounds_config": "Un destello de luz y el rugido de dolor del ser.",
        "options": {
            1: {"text": "Seguir activando las inscripciones para debilitar al ser", "siguiente": "seguirInscripciones"},
            2: {"text": "Detenerte y observar la reacción del ser", "siguiente": "detObservar"}
        }
    },
    "seguirInscripciones": {
        "text": "Activas todas las inscripciones, creando una red de luz que atrapa y destruye al ser etéreo. La cámara retumba y un portal se abre, revelando el tesoro. (FINAL EXITOSO)",
        "sounds_config": "El retumbar de la cámara y un sonido resonante cuando se abre el portal.",
        "options": {}  # No hay más opciones, ya que es un final exitoso.
    },
    "detObservar": {
        "text": "Al detenerte, el ser recupera fuerzas rápidamente y lanza un ataque devastador, destruyéndote. (FINAL FALLIDO)",
        "sounds_config": "Un rugido triunfante del ser y un estallido final de energía oscura.",
        "options": {}  # No hay más opciones, ya que es un final fallido.
    },
    "esquivarAtaques": {
        "text": "Intentas retroceder y esquivar los ataques del ser, pero su velocidad es abrumadora y te alcanza con facilidad, terminando tu vida. (FINAL FALLIDO)",
        "sounds_config": "El rugido del ser mientras te alcanza y un estallido de energía al impactarte.",
        "options": {}  # No hay más opciones, ya que es un final fallido.
    }
}
  
  return history