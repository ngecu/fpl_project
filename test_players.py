# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestPlayers():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def wait_for_window(self, timeout = 2):
    time.sleep(round(timeout / 1000))
    wh_now = self.driver.window_handles
    wh_then = self.vars["window_handles"]
    if len(wh_now) > len(wh_then):
      return set(wh_now).difference(set(wh_then)).pop()
  
  def test_players(self):
    self.driver.get("https://www.premierleague.com/players")
    self.driver.set_window_size(1920, 1040)
    self.driver.find_element(By.CSS_SELECTOR, ".mobile > .current").click()
    self.driver.find_element(By.CSS_SELECTOR, ".mobile li:nth-child(2)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".mobile > .current").click()
    self.driver.find_element(By.CSS_SELECTOR, ".mobile li:nth-child(3)").click()
    element = self.driver.find_element(By.LINK_TEXT, "Will Dennis")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".mobile > .current").click()
    self.driver.find_element(By.CSS_SELECTOR, ".mobile li:nth-child(21)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".mobile > .current").click()
    self.driver.find_element(By.CSS_SELECTOR, ".mobile li:nth-child(20)").click()
    self.driver.execute_script("window.scrollTo(0,159)")
    element = self.driver.find_element(By.LINK_TEXT, "Vladimír Coufal")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    self.driver.find_element(By.LINK_TEXT, "Lukasz Fabianski").click()
    self.driver.find_element(By.CSS_SELECTOR, ".name:nth-child(1)").click()
    self.vars["window_handles"] = self.driver.window_handles
    self.driver.find_element(By.CSS_SELECTOR, ".playerContainer").click()
    self.vars["win4485"] = self.wait_for_window(2000)
    self.vars["root"] = self.driver.current_window_handle
    self.driver.switch_to.window(self.vars["win4485"])
    self.driver.switch_to.window(self.vars["root"])
    self.driver.find_element(By.CSS_SELECTOR, ".img").click()
  
