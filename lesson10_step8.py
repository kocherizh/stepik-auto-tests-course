from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

try:
            browser = webdriver.Chrome()

            browser.get("http://suninjuly.github.io/explicit_wait2.html")
            def calc(x):
                return str(math.log(abs(12*math.sin(int(x)))))


            button = browser.find_element_by_id("book") 
            price = WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
            button.click()
            browser.execute_script("return arguments[0].scrollIntoView(true);", button)

            x_check = browser.find_element_by_css_selector("#input_value")
            x = x_check.text
            y = calc(x)
            print("x=")
            print (x)
            
            
    
            input1 = browser.find_element_by_id("answer")
            browser.execute_script("return arguments[0].scrollIntoView(true);", input1)
            input1.send_keys(y)
            button1 = browser.find_element_by_id("solve")
            button1.click()
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после
    browser.quit()