# src/utils/abdul_kerim.py
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import time
from enum import Enum
import os
from dotenv import load_dotenv
from utils.logger import log  # Import the log function
import chromedriver_autoinstaller

class AbdulKerim:
    def __init__(self):
        chromedriver_autoinstaller.install()
        log("AbdulKerim is ready to serve!")
        load_dotenv()

        # Use the getenv function to retrieve the values
        self.spotify_username = os.getenv("SPOTIFY_USERNAME")
        self.spotify_password = os.getenv("SPOTIFY_PASSWORD")
        self.main_device_name = os.getenv("MAIN_DEVICE_NAME")
        self.tahajjud_device_name = os.getenv("TAHAJJUD_DEVICE_NAME")
        log("AbdulKerim read system variables from .env file.")
        log(f"AbdulKerim knows SPOTIFY_USERNAME is {self.spotify_username}")
        log(f"AbdulKerim knows MAIN_DEVICE_NAME is {self.main_device_name}")
        log(f"AbdulKerim knows TAHAJJUD_DEVICE_NAME is {self.tahajjud_device_name}")
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get("https://accounts.spotify.com/en/login?continue=https%3A%2F%2Fopen.spotify.com%2F%3Fflow_ctx%3D66da0c01-0012-4684-a22a-644eb3444108%253A1701134009")
        log("AbdulKerim is on the login page.")

        email = self.driver.find_element(By.ID, 'login-username')
        password = self.driver.find_element(By.ID, 'login-password')

        email.send_keys(self.spotify_username)
        password.send_keys(self.spotify_password)
        password.send_keys(Keys.RETURN)
        log("AbdulKerim submitted the login form.")
        time.sleep(5)

    def play(self, playlist_url, device_name):
        from utils.prayer_time_decider import PLAYLISTS
        self.driver.get(playlist_url)
        log(f"AbdulKerim is playing the playlist at the URL: {playlist_url}.")
        time.sleep(5)

        try:
            log("AbdulKerim is trying to accept cookies...")
            self.driver.find_element(By.ID, "onetrust-accept-btn-handler").click()
        except Exception:
            log("AbdulKerim noticed cookies were already accepted.")

        try:
            log(f"AbdulKerim is trying to select the device: {device_name}.")
            time.sleep(5)
            self.select_device(device_name)
            time.sleep(5)
            self.select_device(device_name)
            time.sleep(5)
            self.select_device(device_name)
        except Exception:
            log("AbdulKerim noticed the device was already selected.")

        log("AbdulKerim will play the playlist play button.")
        self.driver.find_elements(By.CSS_SELECTOR, "button[data-testid='play-button']")[1].click()
        time.sleep(3)
        log("AbdulKerim will play the skip button.")
        self.driver.find_element(By.CSS_SELECTOR, "button[data-testid='control-button-skip-forward']").click()
        time.sleep(10)
        log("AbdulKerim will get the duration.")
        duration = self.get_duration() - 15
        log(f"AbdulKerim got the duration as {duration} seconds.")
        self.stop(duration)

    def select_device(self, device_name):
        try:
            log("AbdulKerim is trying to click the devices icon...")
            self.driver.find_element(By.ID, "device-picker-icon-button").click()
            log(f"AbdulKerim is trying to click the device: {device_name}.")
            self.driver.find_elements(By.CSS_SELECTOR, f"button[aria-label='{device_name}']")[-1].click()
            time.sleep(5)
        except Exception:
            try:
                self.driver.find_elements(By.CSS_SELECTOR, f"button[aria-label='{self.main_device_name}']")[-1].click()
            except Exception:
                log("AbdulKerim noticed the correct device was already selected.")

    def stop(self, duration):
        log(f"AbdulKerim will sleep for {duration} seconds, don't disturb ({datetime.now()}).")
        time.sleep(duration)
        log(f"AbdulKerim woke up ({datetime.now()}).")
        self.driver.find_element(By.CSS_SELECTOR, "button[data-testid='control-button-playpause']").click()
        log("AbdulKerim clicked the pause button.")
        time.sleep(5)
        self.driver.quit()

    def get_duration(self):
        log("AbdulKerim is trying to find the duration of the track.")
        playback_duration = self.driver.find_element(By.CSS_SELECTOR, "div[data-testid='playback-duration']")
        data_test_position_str = playback_duration.text
        log(f"AbdulKerim noticed its text-based duration is ({data_test_position_str}) as hh:mm.")
        minutes, seconds = map(int, data_test_position_str.split(':'))
        log(f"AbdulKerim parsed the text as ({minutes}) minutes and ({seconds}) seconds.")
        data_test_position = minutes * 60 + seconds
        log(f"AbdulKerim calculated duration as ({data_test_position}) from the string ({data_test_position_str}).")
        return data_test_position
