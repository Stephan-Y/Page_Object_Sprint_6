from selenium import webdriver
import pytest

@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    driver.get('https://qa-scooter.praktikum-services.ru/')
    yield driver
    driver.quit()