from map import *
from ui import *

while True:
    clear()
    print()
    printMap(GameMap)
   
    
    if GameMap[rr+2][rc] ==3 or GameMap[rr][rc+2] ==3 or GameMap[rr-2][rc] ==3 or GameMap[rr][rc-2] == 3:
         print()
         print("🕱 Warning! Mines! 🕱\n")
      
    key = controls()
    if key == "x":
       clear()
       print("GAME OVER!")
       break
    

    GameMap[rr][rc] = 0
      
    #right
    if key == "d" and GameMap[rr][rc+1] != 1 and rc < 8:
        rc += 1            
         
    #left
    elif key == "a" and GameMap[rr][rc-1] != 1 and rc > 0:
       rc -= 1
    #up
    if key == "s" and GameMap[rr+1][rc] != 1 and rr < 8:
        rr += 1
      #down  
    elif key == "w" and GameMap[rr-1][rc] != 1 and rr > 0 :
       rr -= 1
    GameMap[rr][rc] = 2