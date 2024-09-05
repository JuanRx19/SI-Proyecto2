# SI-Proyecto2

## Integrantes
- José Manuel García L.
- Juan Miguel Rojas

## Descripción del Proyecto

Este proyecto está diseñado para gestionar la historia, los audios y la reproducción de los audios asociados a la narrativa.

### 1. Clases

3 classes were created to manage the history, the audios and the playback of the audios.

#### 1.1 Clase `History`
The `History` class is in charge of mapping the story with its corresponding narrative, options and audios. 

#### 1.2 Clase `Sound`
The `Sound` class is in charge of obtaining the audio information and saves its corresponding information.

#### 1.3 Clase `SoundConfigure`
The `SoundConfigure` class is in charge of obtaining the list of objects of type Sound and has a method that is in charge of playing the audios.

### 2. Narrativa

The narrative is composed by a dictionary which contains: the text, the sound configuration and the options, these last ones contain the key of the next element.

- **Text:** The story or narrative.
- **Sound Configuration:** Audio configuration.
- **Options:** The options contain the key to the next element in the story.

### 3. Audios

All audios had to be set to mono in order to be used with OpenAL and 3D sound.

- The `SoundNoEdit` folder contains the audios before being converted to mono
- The `Sounds` folder already has the audios converted to mono.
