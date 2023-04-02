# ---------------------------------------------------------------------------------
from selenium import webdriver
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
from webdriver_manager.firefox import GeckoDriverManager
import time
import json
import os

# ------------------------------------------------------------------------------------

MY_EMAIL_VAR = os.getenv('EMAIL')
MY_PASS_VAR = os.getenv('PASS')


# -------------------------------------------------------------------------------------
options = webdriver.FirefoxOptions()
options.headless = False
ua = UserAgent()
userAgent = ua.random
options.add_argument(f'user-agent={userAgent}')
# -------------------------------------------------------------------------------------

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(),options=options)
driver.get("https://fantasy.premierleague.com/")
driver.maximize_window() 
time.sleep(10)
try:
    driver.find_element(By.CSS_SELECTOR,"#onetrust-accept-btn-handler").click()
except:
    print("Element does not exist")
# -------------------------------------------------------------------------------------
time.sleep(5)
email_input = driver.find_element(By.ID, "loginUsername")
time.sleep(5)
email_input.send_keys(MY_EMAIL_VAR)
time.sleep(5)
password_input = driver.find_element(By.ID, "loginLoginWrap")
time.sleep(5)
password_input.send_keys(MY_PASS_VAR)

time.sleep(5)
driver.find_element(By.CSS_SELECTOR,".sc-bdnxRM.iToEuo").click()
time.sleep(5)

# ----------------------------------------------------------------------------------

time.sleep(5)
leagues = driver.find_elements(By.CSS_SELECTOR,".Link-a4a9pd-1.kofttw")  
leagues[3].click()

# --------------------------------------------------------------------------------

teams = []
players = driver.find_elements(By.CSS_SELECTOR,".StandingsRow-fwk48s-0")
for p in players:
    print(p.find_element(By.CSS_SELECTOR,".Link-a4a9pd-1.kofttw").get_attribute('href'))
    teams.append(p.find_element(By.CSS_SELECTOR,".Link-a4a9pd-1.kofttw").get_attribute('href'))


mydict={}
for index, i in enumerate(teams):
    mydict[index]=f"{i}"
    
with open('result.json', 'w') as fp:
    json.dump(mydict, fp)

driver.quit()
