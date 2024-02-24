# src/utils/prayer_time_decider.py
from enum import Enum
import os
from dotenv import load_dotenv
from src.utils.logger import log  # Import the log function
from src.utils.sahat_kula import SahatKula
from src.prayer_times_sources.aziz import Aziz
from src.prayer_times_sources.ebu_suud import EbuSuud
import datetime

class PRAYER_TIME(Enum):
    FAJR = 0
    SUNRISE = 1
    DHUHR = 2
    ASR = 3
    MAGHRIB = 4
    ISHA = 5
    TAHAJJUD = 6

class PLAYLISTS(Enum):
    FAJR = 'https://open.spotify.com/playlist/3mvO8StEttQRAwAM1uO6SU'
    SHORT_SURAS = 'https://open.spotify.com/playlist/5HPIJSR65nzVLqCY7G9kug'
    REGULAR = 'https://open.spotify.com/playlist/2iSDeKvaJq4x9G0ZQk0VHQ'
    MAGHRIB = 'https://open.spotify.com/playlist/0GQhUM1te6j5QGQZVsG3yz'

class PrayerTimeDecider:
    def __init__(self, sahatKula, aziz, ebuSuud):
        load_dotenv()
        log(f"PrayerTimeDecider is preparing...")
        self.sahatKula = sahatKula
        self.firstTimes=[
            sahatKula.getSmaller(aziz.times[0], ebuSuud.times[0]),
            sahatKula.getSmaller(aziz.times[1], ebuSuud.times[1]),
            sahatKula.getSmaller(aziz.times[2], ebuSuud.times[2]),
            sahatKula.getSmaller(aziz.times[3], ebuSuud.times[3]),
            sahatKula.getSmaller(aziz.times[4], ebuSuud.times[4]),
            sahatKula.getSmaller(aziz.times[5], ebuSuud.times[5])
        ]
        log(f"PrayerTimeDecider knows first times as ({self.firstTimes}).")
        self.secondTimes=[
            sahatKula.getBigger(aziz.times[0], ebuSuud.times[0]),
            sahatKula.getBigger(aziz.times[1], ebuSuud.times[1]),
            sahatKula.getBigger(aziz.times[2], ebuSuud.times[2]),
            sahatKula.getBigger(aziz.times[3], ebuSuud.times[3]),
            sahatKula.getBigger(aziz.times[4], ebuSuud.times[4]),
            sahatKula.getBigger(aziz.times[5], ebuSuud.times[5])
        ]
        log(f"PrayerTimeDecider knows second times as ({self.secondTimes}).")

        # Use the getenv function to retrieve the values
        self.main_device_name = os.getenv("MAIN_DEVICE_NAME")
        self.tahajjud_device_name = os.getenv("TAHAJJUD_DEVICE_NAME")
        log("PrayerTimeDecider read system variables from .env file.")
        log(f"PrayerTimeDecider knows MAIN_DEVICE_NAME is {self.main_device_name}")
        log(f"PrayerTimeDecider knows TAHAJJUD_DEVICE_NAME is {self.tahajjud_device_name}")

    def get_closest_prayer_times(self, now = None):
        log(f"PrayerTimeDecider is trying to get closest prayer times, now is ({now}).")
        if now is None:
            now = self.sahatKula.getCurrentTime()
        log(f"PrayerTimeDecider decided to use now as ({now}).")
        idx = self.get_closest_prayer_times_index(now)
        log(f"PrayerTimeDecider prayer time index is ({idx}).")
        if idx == PRAYER_TIME.TAHAJJUD.value:
            ret = [now, now]
        else:
            ret = [self.firstTimes[idx], self.secondTimes[idx]]
        log(f"PrayerTimeDecider will return ({ret}).")
        return ret

    def get_closest_prayer_times_index(self, now = None):
        log(f"PrayerTimeDecider is trying to get closest prayer time index, now is ({now}).")
        if now is None:
            now = self.sahatKula.getCurrentTime()
        log(f"PrayerTimeDecider decided to use now as ({now}).")
        now_minutes = int(now[:2]) * 60 + int(now[3:])
        log(f"PrayerTimeDecider calculated now_minutes as ({now_minutes}).")

        first_times_minutes = [int(t[:2]) * 60 + int(t[3:]) for t in self.firstTimes]
        log(f"PrayerTimeDecider calculated first_times_minutes as ({first_times_minutes}).")
        second_times_minutes = [int(t[:2]) * 60 + int(t[3:]) for t in self.secondTimes]
        log(f"PrayerTimeDecider calculated second_times_minutes as ({second_times_minutes}).")

        # Adjust for circular nature of time (midnight)
        first_times_minutes = [t + 1440 if t < now_minutes else t for t in first_times_minutes]
        log(f"PrayerTimeDecider corrected first_times_minutes as ({first_times_minutes}).")
        second_times_minutes = [t + 1440 if t < now_minutes else t for t in second_times_minutes]
        log(f"PrayerTimeDecider corrected second_times_minutes as ({second_times_minutes}).")

        closest_first_idx = min(range(len(first_times_minutes)), key=lambda x: abs(first_times_minutes[x] - now_minutes))
        log(f"PrayerTimeDecider found closest first_times index as ({closest_first_idx}).")
        minutes_until_closest_first = abs(first_times_minutes[closest_first_idx] - now_minutes)
        log(f"PrayerTimeDecider found minutes until closest first as ({minutes_until_closest_first}).")
        closest_second_idx = min(range(len(second_times_minutes)), key=lambda x: abs(second_times_minutes[x] - now_minutes))
        log(f"PrayerTimeDecider found closest second_times index as ({closest_second_idx}).")
        minutes_until_closest_second = abs(second_times_minutes[closest_second_idx] - now_minutes)
        log(f"PrayerTimeDecider found minutes until closest second as ({minutes_until_closest_second}).")
        minIdx = min(closest_first_idx, closest_second_idx)
        log(f"PrayerTimeDecider will return minIdx as ({minIdx}).")
        maxIdx = max(closest_first_idx, closest_second_idx)
        log(f"PrayerTimeDecider will return maxIdx as ({maxIdx}).")
        closest_minutes = min(minutes_until_closest_first, minutes_until_closest_second)
        idx = minIdx
        if maxIdx - 1 != minIdx:
            idx = maxIdx

        log(f"PrayerTimeDecider detects idx ({idx}) and closest_minutes ({closest_minutes}).")
        if idx == PRAYER_TIME.FAJR.value and closest_minutes == 60:
            idx = PRAYER_TIME.TAHAJJUD.value

        log(f"PrayerTimeDecider will return idx as ({idx}).")

        return idx

    def decide(self, index = None, times = None, now = None):
        log(f"PrayerTimeDecider is deciding if it is a praying time or not: now is ({now}), index is ({index}) and times are ({times}).")
        if now is None:
            now = self.sahatKula.getCurrentTime()
        if times is None:
            times = self.get_closest_prayer_times(now)
        if index is None:
            index = self.get_closest_prayer_times_index(now)
        log(f"PrayerTimeDecider decided to use now as now is ({now}), index is ({index}) and times are ({times}).")
        if index == PRAYER_TIME.FAJR.value:
            log(f"PrayerTimeDecider knows it is Fajr time!")
            return self.sahatKula.compareTimes(times[1], now) == 0, PLAYLISTS.FAJR.value, self.main_device_name
        elif index == PRAYER_TIME.DHUHR.value:
            log(f"PrayerTimeDecider knows it is Dhuhr time!")
            return self.sahatKula.compareTimes(times[0], now) == 0, PLAYLISTS.DHUHR.value, self.main_device_name
        elif index == PRAYER_TIME.ASR.value:
            log(f"PrayerTimeDecider knows it is Asr time!")
            return self.sahatKula.compareTimes(times[1], now) == 0, PLAYLISTS.ASR.value, self.main_device_name
        elif index == PRAYER_TIME.MAGHRIB.value:
            log(f"PrayerTimeDecider knows it is Maghrib time!")
            return self.sahatKula.compareTimes(times[0], now) == 0, PLAYLISTS.MAGHRIB.value, self.main_device_name
        elif index == PRAYER_TIME.ISHA.value:
            log(f"PrayerTimeDecider knows it is Isha time!")
            return self.sahatKula.compareTimes(times[1], now) == 0, PLAYLISTS.ISHA.value, self.main_device_name
        elif index == PRAYER_TIME.TAHAJJUD.value:
            log(f"PrayerTimeDecider knows it is Tahajjud time!")
            return self.sahatKula.compareTimes(times[1], now) == 0, PLAYLISTS.TAHAJJUD.value, self.tahajjud_device_name
        else:
            log(f"PrayerTimeDecider is confused. It will return false, empty, and empty.")
            return False, '', ''
