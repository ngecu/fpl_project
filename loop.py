from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys
import time
import json




players_gks = []
players_def = []
players_mid = []
players_att = []


driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

with open('result.json') as json_file:
    data = json.load(json_file)
    out = list(data.values())

    for count,x in enumerate(out):
        driver.get(x)
        driver.maximize_window() 

        time.sleep(10)
        driver.switch_to.window(driver.window_handles[-1])
        try:
            driver.find_element(By.CSS_SELECTOR,".js-accept-all-close").click()
        except:
            print("Element does not exist")
        

        positions = driver.find_elements(By.CSS_SELECTOR,".Pitch__ElementRow-sc-1mctasb-1.Pitch__PitchRow-sc-1mctasb-2.iAuEaL.gPAVqU")

        gks = positions[0].find_elements(By.CSS_SELECTOR,".PitchElementData__ElementName-sc-1u4y6pr-1")
        defenders = positions[1].find_elements(By.CSS_SELECTOR,".PitchElementData__ElementName-sc-1u4y6pr-1")
        mid = positions[2].find_elements(By.CSS_SELECTOR,".PitchElementData__ElementName-sc-1u4y6pr-1")
        att = positions[3].find_elements(By.CSS_SELECTOR,".PitchElementData__ElementName-sc-1u4y6pr-1")



        for t in gks:
            players_gks.append(str(t.get_attribute('innerText')))

        for t in defenders:
            players_def.append(str(t.get_attribute('innerText')))

        for t in mid:
            players_mid.append(str(t.get_attribute('innerText')))
        
        for t in att:
            players_att.append(str(t.get_attribute('innerText')))
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.COMMAND + 't') 




mygks={}
for gk in players_gks:
    player_count = players_gks.count(gk)
    selection_percentage = (player_count/len(players_gks))*100
    mygks[gk]=selection_percentage

mydefs={}
for defender in players_def:
    player_count = players_def.count(defender)
    selection_percentage = (player_count/len(players_def))*100
    mydefs[defender]=selection_percentage

mymids={}
for mid in players_mid:
    player_count = players_mid.count(mid)
    selection_percentage = (player_count/len(players_mid))*100
    mymids[mid]=selection_percentage

myattackss={}
for attacker in players_att:
    player_count = players_att.count(attacker)
    selection_percentage = (player_count/len(players_att))*100
    myattackss[attacker]=selection_percentage


sorted_gks_by_percentage = sorted(mygks.items(), key=lambda x:x[1], reverse=True)
converted_gk_dict = dict(sorted_gks_by_percentage)

sorted_def_by_percentage = sorted(mydefs.items(), key=lambda x:x[1], reverse=True)
converted_def_dict = dict(sorted_def_by_percentage)

sorted_mid_by_percentage = sorted(mymids.items(), key=lambda x:x[1], reverse=True)
converted_mid_dict = dict(sorted_mid_by_percentage)

sorted_att_by_percentage = sorted(myattackss.items(), key=lambda x:x[1], reverse=True)
converted_attack_dict = dict(sorted_att_by_percentage)


with open('attackers.json', 'w') as fp:
    json.dump(converted_attack_dict, fp)

with open('midfielders.json', 'w') as fp:
    json.dump(converted_mid_dict, fp)

with open('defenders.json', 'w') as fp:
    json.dump(converted_def_dict, fp)

with open('goalkeepers.json', 'w') as fp:
    json.dump(converted_gk_dict, fp)



driver.quit()
