import time
from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome('Add path of Chromedriver here')
url = "https://gu.icloudems.com/corecampus/index.php"

# Opening the website
driver.get(url)
driver.maximize_window()

time.sleep(2)
username = driver.find_element_by_xpath('//*[@id="useriid"]')
password = driver.find_element_by_xpath('//*[@id="actlpass"]')

# Change user name and passwords with your icloud username and password
username.send_keys('Username')  ##################################### Change This Text ############################
password.send_keys('Password')  ##################################### Change This Text ############################

time.sleep(1)

login = driver.find_element_by_xpath('//*[@id="psslogin"]')
login.click()

time.sleep(2)

feedback = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/div/div[7]/a/img')
feedback.click()

time.sleep(2)

selectClass = driver.find_element_by_xpath('//*[@id="classid"]')
sel = Select(selectClass)

sel.select_by_index(1)

time.sleep(5)

start = driver.find_element_by_class_name('btn-rounded')
start.click()

next = driver.find_element_by_xpath('/html/body/div[1]/div/div/center/div[1]/form[1]/div[3]/div/button')

try:
    while next:
        time.sleep(5)
        radios = driver.find_elements_by_class_name('yn--1')

        for radio in radios:
            try:
                radio.click()
            except:
                None

        time.sleep(2)
        driver.execute_script("window.scroll(0, 0);")

        stars = driver.find_elements_by_class_name('star-1')

        for star in stars:
            print(star)
            try:
                star.click()
            except:
                print("Star exception occurred")

        driver.execute_script("window.scroll(0, 0);")

        comments_boxes = driver.find_elements_by_class_name('suggestion')

        for comments_box in comments_boxes:
            try:
                comments_box.send_keys('Good')
            except:
                None

        driver.execute_script("window.scroll(0, 0);")

        suggestion_boxes = driver.find_elements_by_class_name('suggestion_boxes')

        for suggestion_box in suggestion_boxes:
            try:
                suggestion_box.send_keys('Good Teacher')
            except:
                None

        next.click()
        time.sleep(5)
except:
    None
