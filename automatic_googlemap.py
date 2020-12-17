from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time

options = webdriver.ChromeOptions()

options.add_argument('--user-data-dir=C:\\Users\\<ユーザ名>\\AppData\\Local\\Google\\Chrome\\User Data')
options.add_argument('--profile-directory=Profile 2') 

# driver = webdriver.Chrome(options=options)
driver = webdriver.Chrome(
    executable_path='..\\chromedriver.exe', options=options, )
driver.get("https://www.google.co.jp/maps/@35.7056228,139.4564374,14z?hl=ja")
time.sleep(2)
places = []  # list up where you want to go. 

for place in places:
    Place = driver.find_element_by_class_name('tactile-searchbox-input')
    Place.send_keys(place)
    Search = driver.find_element_by_xpath(
      "/html/body/jsl/div[3]/div[9]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/button")
    Search.click()
    time.sleep(7)
    try:
        Hold = driver.find_element_by_xpath(
        "/html/body/jsl/div[3]/div[9]/div[7]/div/div[1]/div/div/div[5]/div[2]/div/button")
        Hold.click()
    except NoSuchElementException:
        try:
            Top = driver.find_element_by_xpath(
                '/html/body/jsl/div[3]/div[9]/div[7]/div/div[1]/div/div/div[5]/div[1]/a[1]')
            Top.click()
            time.sleep(5)
            Hold = driver.find_element_by_xpath(
                "/html/body/jsl/div[3]/div[9]/div[7]/div/div[1]/div/div/div[5]/div[2]/div/button")
            Hold.click()
        except NoSuchElementException:
            try:
                Top = driver.find_element_by_xpath(
                    '/html/body/jsl/div[3]/div[9]/div[7]/div/div[1]/div/div/div[4]/div[1]/a[1]')
                Top.click()
                time.sleep(5)
                Hold = driver.find_element_by_xpath(
                    "/html/body/jsl/div[3]/div[9]/div[7]/div/div[1]/div/div/div[5]/div[2]/div/button")
                Hold.click()
            except NoSuchElementException:
                Top = driver.find_element_by_xpath(
                    '/html/body/jsl/div[3]/div[9]/div[7]/div/div[1]/div/div/div[2]/div[1]/a[1]')
                Top.click()
                time.sleep(5)
                Hold = driver.find_element_by_xpath(
                    "/html/body/jsl/div[3]/div[9]/div[7]/div/div[1]/div/div/div[5]/div[2]/div/button")
                Hold.click()
    time.sleep(4)
    Goto = driver.find_element_by_xpath(
        "/html/body/jsl/div[3]/div[4]/div[1]/ul/li[3]")
    Goto.click()
    time.sleep(3)
    Clear = driver.find_element_by_class_name('tactile-searchbox-input')
    Clear.clear()
  

