from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys
import time
import json



players_url = []
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.get("https://www.premierleague.com/players")
driver.maximize_window() 
time.sleep(10)




try:
    driver.find_element(By.CSS_SELECTOR,"#onetrust-accept-btn-handler").click()
    time.sleep(10)
    driver.find_element(By.CSS_SELECTOR,"#advertClose").click()

    
except:
    print("Element does not exist")

for nu in range(1,21):
    try:
        driver.find_element(By.CSS_SELECTOR,"#onetrust-accept-btn-handler").click()
    except:
        print("Element does not exist")
        
    driver.find_element(By.CSS_SELECTOR, ".mobile > .current").click()
    driver.find_element(By.CSS_SELECTOR, ".mobile li:nth-child({})".format(nu)).click()
    print("clicked")
    time.sleep(5)
    

    SCROLL_PAUSE_TIME = 0.5

    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height


    
    # playerElements = driver.find_elements(By.CSS_SELECTOR,".dataContainer .playerName")
    playerElements = driver.find_elements(By.CSS_SELECTOR, 'a.playerName')
  
    print(len(playerElements))
    for elem in playerElements:
        try:
            print(elem.get_attribute('href'))
            players_url.append(elem.get_attribute('href'))
        except:
            print("no url")
    time.sleep(5)


mydict={}
for index, i in enumerate(players_url):
    mydict[index]=f"{i}"
    
with open('players.json', 'w') as fp:
    json.dump(mydict, fp)

print(players_url)
print(len(players_url))
driver.quit()


