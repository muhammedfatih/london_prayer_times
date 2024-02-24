# src/prayer_times_sources/aziz.py
import requests
from datetime import datetime
from utils.logger import log  # Import the log function

class Aziz:
    def __init__(self):
        log(f"Aziz is preparing...")
        self.times=['', '', '', '', '', '']
        current_date = datetime.now()
        day_of_year = current_date.timetuple().tm_yday
        self.dayOfYear = day_of_year
        log(f"Aziz set number of day of year: ({self.dayOfYear}).")
        index_to_retrieve = day_of_year - 1
        log(f"Aziz set index_to_retrieve: ({index_to_retrieve}).")
        url = 'https://www.aziziye.org.uk/namaz.json'
        response = requests.get(url)
        log(f"Aziz sent the request to api and status code is ({response.status_code}).")
        if response.status_code == 200:
            data = response.json()['ptimes']
            if 0 <= index_to_retrieve < len(data):
                item = data[index_to_retrieve]
                self.times=[
                    self.convertToHM(item['fajr']),
                    self.convertToHM(item['sunrise']),
                    self.convertToHM(item['zuhr']),
                    self.convertToHM(item['asr']),
                    self.convertToHM(item['maghrib']),
                    self.convertToHM(item['isha'])
                ]
                log(f"Aziz knows prayer times are ({self.times})")
            else:
                log(f"Aziz didn't get prayer times properly.")
        else:
            log(f"Aziz didn't get prayer times properly.")

    def convertToHM(self, decimal_number):
        log(f"Aziz will learn hour and minutes from the given decimal number ({decimal_number}).")
        hours = int(float(decimal_number) * 24)
        log(f"Aziz found hours as ({hours}).")
        minutes = int((float(decimal_number) * 24 - hours)*60)
        log(f"Aziz found minutes as ({minutes}).")
        log(f"Aziz will return as decimal_number ({decimal_number}) as ({hours:02d}:{minutes:02d}).")
        return f"{hours:02d}:{minutes:02d}"
