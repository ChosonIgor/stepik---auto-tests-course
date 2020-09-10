from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_css_selector('input[placeholder="Enter first name"]').send_keys("Igor")

    browser.find_element_by_css_selector('input[placeholder="Enter last name"]').send_keys("Igor")

    browser.find_element_by_css_selector('input[placeholder="Enter email"]').send_keys("Igor@gmail.com")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'new_file.txt')

    element = browser.find_element_by_css_selector('#file')
    element.send_keys(file_path)

    button1 = browser.find_element_by_css_selector("button.btn")
    button1.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
