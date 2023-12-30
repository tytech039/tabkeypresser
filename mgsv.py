import pyautogui
import time
import random

print("""
      __________________
    .-'  \ _.-''-._ /  '-.
  .-/\   .'.      .'.   /\-.
 _'/  \.'   '.  .'   './  \'_
:======:======::======:======:
 '. '.  \     ''     /  .' .'
   '. .  \   :  :   /  . .'    DIAMOND
     '.'  \  '  '  /  '.'      DOGS
       ':  \:    :/  :'
         '. \    / .'
           '.\  /.'    
             '\/'
""")


def press_tab_randomly():
    try:
        while True:
            # Generate a random interval between 20 and 45 seconds
            interval = random.randint(20, 45)
            print(f"Waiting for {interval} seconds before pressing Tab.")
            
            # Wait for the specified interval
            time.sleep(interval)

            # Press the 'Tab' key
            pyautogui.press('tab')
            print("Tab key pressed.")

    except KeyboardInterrupt:
        print("Script stopped by user.")

if __name__ == "__main__":
    press_tab_randomly()
