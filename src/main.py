# main.py
import os
import time
from datetime import datetime

def main():
    from src.utils.abdul_kerim import AbdulKerim
    from src.prayer_times_sources.aziz import Aziz
    from src.prayer_times_sources.ebu_suud import EbuSuud
    from src.utils.sahat_kula import SahatKula
    from src.utils.prayer_time_decider import PrayerTimeDecider
    from src.utils.logger import log  # Import the log function
    log(f"Application is started.")
    
    log(f"Application is starting Aziz.")
    aziz = Aziz()
    log(f"Application is started Aziz.")
    
    log(f"Application is starting EbuSuud.")
    ebuSuud = EbuSuud()
    log(f"Application is started EbuSuud.")
    
    log(f"Application is starting SahatKula.")
    sahatKula = SahatKula()
    log(f"Application is started SahatKula.")
    
    log(f"Application is starting PrayerTimeDecider.")
    prayerTimeDecider = PrayerTimeDecider(sahatKula, aziz, ebuSuud)
    log(f"Application is started PrayerTimeDecider.")

    while True:
        now = datetime.now()
        log(f"-------------------------------------------------")
        shouldPlay, playListUrl, deviceName = prayerTimeDecider.decide()
        log(f"Time: ({now}) and shouldPlay: ({shouldPlay})")
        if shouldPlay:
            log(f"Azan time! Abdulkerim will play: ({playListUrl}).")
            abdulkerim = AbdulKerim()
            abdulkerim.login()
            abdulkerim.play(playListUrl, deviceName)
        log(f"-------------------------------------------------")
        time.sleep(60)

if __name__ == "__main__":
    main()
