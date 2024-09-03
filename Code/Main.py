from History import History
from Narrative import get_narrative
import openal

def main():
  #Inicio de la historia
  openal.oalInit()
  current_history_part = "inicio"
  narrative = get_narrative()
  key_history = narrative[current_history_part]
  story = History(key_history["text"], key_history["sounds_config"], key_history["options"])
  story.print_story()
  story.sonido.play()
  key_option = int(input())
  
  #Ciclo que itera la historia, hasta el final
  while(story.get_next_history_part(key_option) != "final"):
    current_history_part = story.get_next_history_part(key_option)
    key_history = narrative[current_history_part]
    story = History(key_history["text"], key_history["sounds_config"], key_history["options"])
    story.print_story()
    story.sonido.play()
    key_option = int(input())
  openal.oalQuit()
  
main()