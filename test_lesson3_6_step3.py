import time
import math
import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('part_of_link', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_homework(browser, part_of_link):
    link = f"https://stepik.org/lesson/{part_of_link}/step/1"
    browser.get(link)
    browser.implicitly_wait(5)
    y = str(math.log(int(time.time())))
    print(y)
    browser.find_element_by_css_selector('[placeholder="Напишите ваш ответ здесь..."]').send_keys(y)
    browser.find_element_by_css_selector('button.submit-submission').click()
    time.sleep(10)
