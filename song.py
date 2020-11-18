import random
import time 
from sense_hat import SenseHat

sense = SenseHat();
sense.clear()

listtone = []
sang = ""

#A B E H E G A A C D
def GetTone(nr):
  #tal = random.randint(1,4);
  print("tal: "+ str(nr));
  
  if nr == 1:
    sense.show_letter("D");
    return "D";
  elif nr == 2:
    sense.show_letter("E");
    return "E";
  elif nr == 3:
    sense.show_letter("F");
    return "F";
  elif nr == 4:
    sense.show_letter("G");
    return "G";
  else:
    return "UKENDT";
    


while True:
  tal = random.randint(1,4);
  tone = GetTone(tal)
  print("tone:" + tone)
  #listtone.append(tone)
  sang += tone
  
  time.sleep(1)
  
  if len(sang) >= 10:
    break
  
print("sangen er: " + sang)
sense.show_message(sang)
