# SI-Proyecto2

## Integrantes
- José Manuel García L.
- Juan Miguel Rojas

## Project Description

The project is a decision game played on console which uses `OpenAL` for 3D sounds.

### 1. Clases

3 classes were created to manage the history, the audios and the playback of the audios.

#### 1.1 `History` class
The `History` class is in charge of mapping the story with its corresponding narrative, options and audios. 

#### 1.2 `Sound` class
The `Sound` class is in charge of obtaining the audio information and saves its corresponding information.

#### 1.3 `SoundConfigure` class
The `SoundConfigure` class is in charge of obtaining the list of objects of type Sound and has a method that is in charge of playing the audios.

### 2. Narrative

The narrative is composed by a dictionary which contains: the text, the sound configuration and the options, these last ones contain the key of the next element.

- **Text:** The story or narrative.
- **Sound Configuration:** Audio configuration.
- **Options:** The options contain the key to the next element in the story.

### 3. Audios

All audios had to be set to mono in order to be used with `OpenAL` and 3D sound.

- The `SoundNoEdit` folder contains the audios before being converted to mono
- The `Sounds` folder already has the audios converted to mono.
