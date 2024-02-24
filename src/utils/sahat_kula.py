# src/utils/sahat_kula.py
from datetime import datetime
from utils.logger import log  # Import the log function

class SahatKula:
    def __init__(self):
        self.currentTime = self.getCurrentTime()
        log(f"SahatKula is prepared.")

    def getCurrentTime(self):
        # Get the current time
        current_time = datetime.now()
        log(f"SahatKula noticed current time is ({current_time}).")

        # Extract the hour and minute from the current time
        hour = current_time.strftime("%H")  # Extracts hour in 24-hour format
        minute = current_time.strftime("%M")  # Extracts minute
        log(f"SahatKula parsed current time ({current_time}), as ({hour}) hour and as ({minute}) minute.")
        return f"{hour}:{minute}"

    def compareTimes(self, hm1, hm2):
        log(f"SahatKula is comparing ({hm1}) and ({hm2}).")
        # Splitting the strings into hours and minutes
        hour1, minute1 = map(int, hm1.split(':'))
        log(f"SahatKula is comparing ({hm1}) and ({hm2}).")
        hour2, minute2 = map(int, hm2.split(':'))
        log(f"SahatKula analyzed hm2 ({hm2}) as ({hour2}) as hour, and ({minute2}).")

        # Comparing the hours
        if hour1 > hour2:
            log(f"SahatKula found out hour1 ({hour1}) is bigger than hour2 ({hour2}) and will return -1.")
            return -1
        elif hour1 < hour2:
            log(f"SahatKula found out hour1 ({hour1}) is smaller than hour2 ({hour2}) and will return 1.")
            return 1
        else:
            # If hours are equal, compare the minutes
            if minute1 > minute2:
                log(f"SahatKula found out hour1 ({hour1}) is equal to hour2 ({hour2}), but minute1 ({minute1}) is bigger than minute2 ({minute2}) and will return -1.")
                return -1
            elif minute1 < minute2:
                log(f"SahatKula found out hour1 ({hour1}) is equal to hour2 ({hour2}), but minute1 ({minute1}) is smaller than minute2 ({minute2}) and will return 1.")
                return 1
            else:
                log(f"SahatKula found out hour1 ({hour1}) is equal to hour2 ({hour2}), and minute1 ({minute1}) is equal to minute2 ({minute2}) and will return 0.")
                return 0

    def getSmaller(self, hm1, hm2):
        log(f"SahatKula is comparing hm1 ({hm1}), and hm2 ({hm2}) and will return smaller.")
        if self.compareTimes(hm1, hm2) == 1:
            log(f"SahatKula is comparing hm1 ({hm1}), and hm2 ({hm2}), it will return hm1 ({hm1}) as smaller.")
            return hm1
        else:
            log(f"SahatKula is comparing hm1 ({hm1}), and hm2 ({hm2}), it will return hm1 ({hm2}) as smaller.")
            return hm2

    def getBigger(self, hm1, hm2):
        log(f"SahatKula is comparing hm1 ({hm1}), and hm2 ({hm2}) and will return bigger.")
        if self.compareTimes(hm1, hm2) == 1:
            log(f"SahatKula is comparing hm1 ({hm1}), and hm2 ({hm2}), it will return hm1 ({hm1}) as bigger.")
            return hm2
        else:
            log(f"SahatKula is comparing hm1 ({hm1}), and hm2 ({hm2}), it will return hm1 ({hm2}) as bigger.")
            return hm1
