from History import History
from Sound import Sound
from Narrative import get_narrative

def main():
  #Inicio de la historia
  current_history_part = "inicio"
  narrative = get_narrative()
  key_history = narrative[current_history_part]
  story = History(key_history["text"], key_history["sounds"], key_history["options"])
  sound = Sound(story.sonido, key_history["sounds_config"][0], key_history["sounds_config"][1], key_history["sounds_config"][2])
  sound.reproducir()
  print(story)
  key_option = int(input())
  
  #Ciclo que itera la historia, hasta el final
  while(story.get_next_history_part(key_option) != "final"):
    current_history_part = story.get_next_history_part(key_option)
    key_history = narrative[current_history_part]
    story = History(key_history["text"], key_history["sounds"], key_history["options"])
    sound = Sound(story.sonido, key_history["sounds_config"][0], key_history["sounds_config"][1], key_history["sounds_config"][2])
    sound.reproducir()
    print(story)
    key_option = int(input())
    
  
main()