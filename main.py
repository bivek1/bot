import time

import requests
from PIL import Image
from io import BytesIO
import pytesseract
from getimage import getCode

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
from selenium.webdriver.support.ui import Select



driver.get("https://www.g4k.go.kr/cipl/0100/login.do")


# eng = driver.find_element(By.CLASS_NAME, "btnLang") 
# eng.click()


engs = driver.find_element(By.ID, "memberLogin") 
engs.click()




name_input = driver.find_element(By.ID, "loginId")
name_input.send_keys("m.ar.i.s.saal.d.a0@gmail.com")


email_input = driver.find_element(By.ID, "loginPwd")
email_input.send_keys("Aa@981825356") 


captcha_select = driver.find_element(By.CLASS_NAME, "captcha")

div_location = captcha_select.location
div_size = captcha_select.size

# Take a screenshot of the entire page
screenshot = driver.get_screenshot_as_png()

# Open the screenshot as an Image object
img = Image.open(BytesIO(screenshot))

div_screenshot = img

# Save the cropped screenshot
# div_screenshot.save("/Users/bibekdhakal/Python/Bot/div_screenshot.png")
# code = getCode('/Users/bibekdhakal/Python/Bot/div_screenshot.png')
# print(code)



# email_input = driver.find_element(By.ID, "captchaTxt")

# email_input.send_keys(code) 



# login_button = driver.find_element(By.ID, "btn_login")
# login_button.click()




email_input = driver.find_element(By.ID, "captchaTxt")
codes = input("Enter captcha code seen in screen")
email_input.send_keys(codes) 


login_button = driver.find_element(By.ID, "btn_login")
login_button.click()

# # Wait for the alert to appear
# wait = WebDriverWait(driver, 5)
# alert = wait.until(EC.alert_is_present())

# # Get the alert text and accept the alert
# alert_text = alert.text
# print("Alert text:", alert_text)
# alert.accept()

# time.sleep(10)



wait = WebDriverWait(driver, 10)
wait.until(EC.url_changes(driver.current_url))
driver.get("https://www.g4k.go.kr/biz/main/main.do")

# driver.get("https://www.g4k.go.kr/cipl/0100/login.do")

language_link = driver.find_element(By.CSS_SELECTOR, "a.btnLang[href='/en/main.do']")
language_link.click()


reserve_element = driver.find_element(By.XPATH, "//img[@src='/images/en/v2/main-ico0105.svg']")
# reserve_element = driver.find_element_by_xpath("//img[@src='/images/en/v2/main-ico0105.svg']")
reserve_element.click()

# reservation_select = driver.find_element(By.CLASS_NAME, "icoBox")
# reservation_select.click()


make_reserve = driver.find_element(By.CLASS_NAME, "btnA_r")
make_reserve.click()


select_element = Select(driver.find_element(By.XPATH, "//select[@id='visitRegnCd']"))

# Add a value to the select element
value_to_add = "CC"
select_element.select_by_value(value_to_add)


select_element_1 = Select(driver.find_element(By.XPATH, "//select[@id='visitNatnCdView']"))

# Add a value to the select element
value_to_add = "213"
select_element_1.select_by_value(value_to_add)

select_element_2 = driver.find_element(By.ID, "visitEmblCdView_chosen")
select_element_2.click()

element_text = "[CANADA] Consulate General of the Republic of Korea in Montreal"
li_element = driver.find_element(By.XPATH, f"//li[contains(text(), '{element_text}')]")

li_element.click()
time.sleep(3)


driver.quit()


