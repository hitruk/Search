import pytest
from selenium import webdriver

@pytest.fixture
def browser():
    #driver = webdriver.Firefox(executable_path='/home/hitruk/dir/geckodriver')
    driver = webdriver.Chrome(executable_path='/home/hitruk/dir/chromedriver')
    driver.implicitly_wait(10)
    yield driver
    driver.close()