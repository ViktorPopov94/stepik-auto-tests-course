from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()

try:
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # говорим Selenium проверять в течение 12 сек, пока цена не упадёт до 100 долларов
    price = WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "$100")
        )

    book = browser.find_element_by_id('book')
    book.click()
    print('забучено')

    x = int(browser.find_element_by_id("input_value").text)
    ans = calc(x)

    answer_pitch = browser.find_element_by_id("answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", answer_pitch)
    answer_pitch.send_keys(ans)

    submit = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "solve"))
    )
    submit.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()