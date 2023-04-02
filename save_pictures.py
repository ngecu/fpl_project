import urllib.request
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys
import time
import json
import os.path

save_path = 'static/player_photo/'

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

with open('players.json') as json_file:
    data = json.load(json_file)
    out = list(data.values())

    for count,x in enumerate(out):
        driver.get(x)
        driver.maximize_window() 

        time.sleep(10)
        driver.switch_to.window(driver.window_handles[-1])
        try:
            driver.find_element(By.CSS_SELECTOR,"#onetrust-accept-btn-handler").click()
            time.sleep(10)
            driver.find_element(By.CSS_SELECTOR,"#advertClose").click()
            
        except:
            print("Element does not exist")

        player_img = driver.find_element(By.CSS_SELECTOR, ".img").get_attribute("src")
        try:
            player_name = driver.find_element(By.CSS_SELECTOR, ".name.t-colour").get_attribute('innerText').split()[1] 
        except:
            try:
                player_name = driver.find_element(By.CSS_SELECTOR, ".name.t-colour").get_attribute('innerText').split()[0] 
            except:
                player_name = driver.find_element(By.CSS_SELECTOR, ".name.t-colour").get_attribute('innerText') 

        if "Photo-Missing.png" not in player_img:
            with urllib.request.urlopen(player_img) as url:
                path = 'static/player_photo/{}.png'.format(player_name)
                isExist = os.path.exists(path)
                if isExist:
                    print("{} exists".format(player_name))
                else:
                    output = open(os.path.join(save_path, "{}.png".format(player_name) ) ,"wb")
                    output.write(url.read())
                    output.close()
                    print("{} added".format(player_name))




driver.quit()
