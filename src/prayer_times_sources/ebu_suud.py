# src/prayer_times_sources/ebu_suud.py
import requests
import re
from utils.logger import log  # Import the log function

class EbuSuud:
    def __init__(self):
        log(f"EbuSuud is preparing...")
        self.times=['', '', '', '', '', '']
        # Send a GET request to the webpage and retrieve the source code
        url = "https://namazvakitleri.diyanet.gov.tr/tr-TR/14096/londra-icin-namaz-vakti"
        response = requests.get(url)
        log(f"EbuSuud sent the request and its response ({response.status_code}).")

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Extract JavaScript part from the source code
            script_pattern = re.compile(r'var _imsakTime = "(.*?)";.*?var _gunesTime = "(.*?)";.*?var _ogleTime = "(.*?)";.*?var _ikindiTime = "(.*?)";.*?var _aksamTime = "(.*?)";.*?var _yatsiTime = "(.*?)"', re.DOTALL)
            matches = re.search(script_pattern, response.text)
            
            if matches:
                prayer_times = matches.groups()
                self.times = list(prayer_times)
                log(f"EbuSuud knows the prayer times as ({self.times}).")
            else:
                log(f"EbuSuud failed to know prayer times.")
        else:
            log(f"EbuSuud failed to know prayer times.")
