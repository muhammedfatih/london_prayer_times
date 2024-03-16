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

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9",
            "Connection": "keep-alive",
        }

        response = requests.get(url, headers=headers)
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
