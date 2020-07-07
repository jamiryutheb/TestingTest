from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

PATH = "C:\\Users\\EnesGuven\\Documents\\stuff\\chromedriver.exe"

driver = webdriver.Chrome(PATH)
driver.get("http://www.beatsperminuteonline.com/")
driver.implicitly_wait(4)

# loginMe = "testing.programming02@gmail.com"

for i in range(10):
    driver.find_element_by_id("bpm_text").click()
    time.sleep(0.7)

bpm = driver.find_element_by_id("bpm_display").text
print(f"Beats per minutes measured at : {bpm} bpm")
driver.close()
