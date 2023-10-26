#from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.action_chains import ActionChains
from seleniumwire import webdriver  
from seleniumwire.utils import decode

import time


# Launch a Chrome browser using Selenium
#options = {'disable_encoding': True}
driver = webdriver.Chrome()

# Navigate to the login page and fill in your credentials
login_url = 'https://betstamp.app/login'
driver.get(login_url)

time.sleep(5)

#locate the login by email button
email_login_button_X_Path = driver.find_element(By.XPATH,'//*[@id="root"]/div/div/a[1]/div/button')
actions = ActionChains(driver)
actions.move_to_element(email_login_button_X_Path).double_click().perform() #this page is weird and requires a double click

time.sleep(3)

#enter username and password
email_field_xpath = driver.find_element(By.XPATH,'//*[@id="root"]/div/div/form/div[1]/div[2]/input')
email_field_xpath.send_keys('nperic360@gmail.com')

password_field_xpath = driver.find_element(By.XPATH,'//*[@id="root"]/div/div/form/div[2]/div[2]/input')
password_field_xpath.send_keys('64pr88!ABC')


#Click Login button

login_button_xpath = driver.find_element(By.XPATH,'//*[@id="root"]/div/div/form/div[4]/button')
actions = ActionChains(driver)
actions.move_to_element(login_button_xpath).click().perform()

time.sleep(5)
#data_url = 'https://www.google.com/search?q=current+date+and+time&rlz=1C1ONGR_enCA1014CA1014&oq=current+date+and+time&aqs=chrome..69i57j0i512l9.2039j0j7&sourceid=chrome&ie=UTF-8'
data_url = 'https://betstamp.app/odds-comparison'
driver.get(data_url)

#NEED TO SELECT ALL TYPES OF LEAGUES 

NCAAF = driver.find_element(By.XPATH,'//*[@id="infinite-scroll-target"]/div[1]/div[1]/div[2]/div[2]/button')
actions = ActionChains(driver)
actions.move_to_element(NCAAF).click().perform()

UFC = driver.find_element(By.XPATH,'//*[@id="infinite-scroll-target"]/div[1]/div[1]/div[2]/div[3]/button')
actions = ActionChains(driver)
actions.move_to_element(UFC).click().perform()

MLB = driver.find_element(By.XPATH,'//*[@id="infinite-scroll-target"]/div/div[1]/div[2]/div[4]/button')
actions = ActionChains(driver)
actions.move_to_element(MLB).click().perform()

NHL = driver.find_element(By.XPATH,'//*[@id="infinite-scroll-target"]/div/div[1]/div[2]/div[5]/button')
actions = ActionChains(driver)
actions.move_to_element(NHL).click().perform()

NBA = driver.find_element(By.XPATH,'//*[@id="infinite-scroll-target"]/div/div[1]/div[2]/div[6]/button')
actions = ActionChains(driver)
actions.move_to_element(NBA).click().perform()

driver.refresh()


# Wait for the page to load after logging in
data_url = 'https://betstamp.app/odds-comparison'
driver.get(data_url)

driver.refresh()
time.sleep(10) #make sure the site loads for all API requests to be made, specifically the odd-compare


#There are some requests where their parameters contain game_id's but they don't contain all games
#I.e.  {'game_ids': '[109990]', 'book_ids': '[482]', 'period': 'FT'} only shows one game
#We want: {'game_ids': '[122254,122253,122252,122251,122250,122249,122248,122255,122257,122256,122258,122260,122259,122261,122263]', 'book_ids': '[482]', 'period': 'FT'}

list_gameIDS = []

for request in driver.requests:
    # Wait for API response
    if request.response:
        request_parameter = request.params
        if 'game_ids' in request_parameter: #there are some entries where it just shows a single game ID
            print(request_parameter)
            list_gameIDS.append(request.params)

#filter out the request parameter that contains the most amount of game ID's

max_game_ID=0
game_ID_string = ''
for i in list_gameIDS:
    num_games = i['game_ids'].count(',')
    if num_games>max_game_ID:
        game_ID_string = i['game_ids']
        max_game_ID = num_games
    #convert string to array
    gameIDS = game_ID_string[1:-1].split(',') #remove the square brackets and split the string by commas into a list
    
print('The game IDs that get updated everyday is: {}'.format(gameIDS))





time.sleep(30)


# Close the browser
driver.quit()