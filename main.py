import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image
from io import BytesIO
from selenium.webdriver.common.action_chains import ActionChains
import pytesseract
# from getimage import getCode  # Assuming this is your custom module for OCR

from concurrent.futures import ThreadPoolExecutor

def login(driver):
    driver.get("https://www.g4k.go.kr/cipl/0100/login.do")
    
    engs = driver.find_element(By.ID, "memberLogin") 
    engs.click()
    name_input = driver.find_element(By.ID, "loginId")
    name_input.send_keys("m.ar.i.s.saal.d.a0@gmail.com")
    email_input = driver.find_element(By.ID, "loginPwd")
    email_input.send_keys("Aa@981825356") 
    captcha_select = driver.find_element(By.CLASS_NAME, "captcha")
    div_location = captcha_select.location
    div_size = captcha_select.size
    screenshot = driver.get_screenshot_as_png()
    img = Image.open(BytesIO(screenshot))
    div_screenshot = img
    email_input = driver.find_element(By.ID, "captchaTxt")
    codes = input("Enter captcha code seen in screen")
    email_input.send_keys(codes) 
    login_button = driver.find_element(By.ID, "btn_login")
    login_button.click()

    time.sleep(10)

    language_link = driver.find_element(By.CSS_SELECTOR, "a.btnLang[href='/en/main.do']")
    language_link.click()
    reserve_element = driver.find_element(By.XPATH, "//img[@src='/images/en/v2/main-ico0105.svg']")
    reserve_element.click()
    make_reserve = driver.find_element(By.CLASS_NAME, "btnA_r")
    make_reserve.click()

    time.sleep(5)

    next_now = driver.find_element(By.ID, "aftBtn")
    next_now.click()

    time.sleep(10)

    # Select Date and time progress
    # visa = driver.find_element(By.ID, "bussCd_NR0033")
    # visa.click()



    checkbox = driver.find_element(By.CLASS_NAME, "checkbox")

    # Click on the checkbox
    checkbox.click()

    # element = driver.find_element(By.ID, "")
    
    # wait = WebDriverWait(driver, 10)
    # element = wait.until(EC.invisibility_of_element_located((By.ID, 'bussCd_NR0033')))
    # element_button = wait.until(EC.element_to_be_clickable((By.ID, 'bussCd_NR0033')))
    # element_button.click()


    for i in range(1, 31):
        day_id = driver.find_element(By.ID, "day"+str(i))
        try:
            day_id.click()
            break
        except:
            pass
    # time.sleep(3)


    time.sleep(5)
    
    time_div = driver.find_element(By.ID, "timeDiv")

    # Find all input elements inside the timeDiv
    input_elements = time_div.find_elements(By.CLASS_NAME, "checkbox")

    # Click on the first input element and break the loop
    for input_element in input_elements:
        input_element.click()
        break

    time.sleep(5)


    next_now = driver.find_element(By.ID, "aftBtn")
    next_now.click()
    time.sleep(2)

    identify_now = driver.find_element(By.ID, "idnyCnfrmNo")
    identify_now.send_keys("0819719871")

    remk_now = driver.find_element(By.ID, "remk")
    remk_now.send_keys("This visa is very essential for me.")

    email_input = driver.find_element(By.ID, "captchaTxt")
    codes = input("Enter captcha code seen in screen")
    email_input.send_keys(codes) 

    next_now = driver.find_element(By.ID, "reserveBtn")
    next_now.click()

    time.sleep(10)


def main():
    driver = webdriver.Chrome()
    login(driver)
    # reserve()
    # with ThreadPoolExecutor(max_workers=2) as executor:
    #     login_future = executor.submit(login, driver)
    #     login_future.result()
    #     time.sleep(10)
    #     reserve_future = executor.submit(reserve, driver)
    #     reserve_future.result()
    driver.quit()

if __name__ == "__main__":
    main()
