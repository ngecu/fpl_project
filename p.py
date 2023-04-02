from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

driver.quit()