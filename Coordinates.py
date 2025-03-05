
# from PIL import Image, ImageDraw

# width, height = 1919, 1079
# image = Image.new('RGB', (width, height), 'white')
# draw = ImageDraw.Draw(image)

# weather_region = (230, 676, 310, 811)  

# draw.rectangle(weather_region, outline='red')

# image.show()  
import requests
import pyautogui
import pytesseract
from PIL import Image
import io
import time
try:
        
        pyautogui.press('win')
        time.sleep(1)
        pyautogui.typewrite('https://www.msn.com/en-gb/weather/')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(5)
        weather_region = (171,837, 533, 949)  
        screenshot = pyautogui.screenshot(region=weather_region)

        text = pytesseract.image_to_string(screenshot)       
        print(text) 
        pyautogui.hotkey('ctrl', 'w')
        pyautogui.hotkey('alt', 'tab')
                
       
except Exception as e:
        print(f"Lỗi khi lấy thông tin thời tiết: {e}")
   