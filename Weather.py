import time
import requests
import pyautogui
import pytesseract
from PIL import Image
import io
import datetime

def Search_information_weather():
    try:
        
        pyautogui.press('win')
        time.sleep(1)
        pyautogui.typewrite('https://www.msn.com/en-gb/wweather/')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(1)
        weather_region = (171,837, 533, 949)  
        screenshot = pyautogui.screenshot(region=weather_region)

        text = pytesseract.image_to_string(screenshot)       
        
        pyautogui.hotkey('ctrl', 'w')
        pyautogui.hotkey('alt', 'tab')
                
        return text
    except Exception as e:
        print(f"Lỗi khi lấy thông tin thời tiết: {e}")
        return "Không thể lấy thông tin thời tiết."
