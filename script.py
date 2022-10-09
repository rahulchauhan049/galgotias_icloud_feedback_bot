import time
from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome('./chromedriver') ##################################### Change This Text with webdriver path which you downloaded ############################
url = "https://gu.icloudems.com/corecampus/index.php"

# Opening the website
driver.get(url)
driver.maximize_window()

time.sleep(2)
username = driver.find_element_by_xpath('//*[@id="useriid"]')
password = driver.find_element_by_xpath('//*[@id="actlpass"]')

# Change user name and passwords with your icloud username and password
username.send_keys('19scse123456')  ##################################### Change This Text With Admission Number ############################
password.send_keys('password')  ##################################### Change This Text with Icloud Password ############################

time.sleep(1)

login = driver.find_element_by_xpath('//*[@id="psslogin"]')
login.click()

time.sleep(1)

feedback = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/div/div[10]/a/img')
feedback.click()

time.sleep(1)

selectClass = driver.find_element_by_xpath('//*[@id="classid"]')
sel = Select(selectClass)

sel.select_by_index(1)

time.sleep(1)


selectClass = driver.find_element_by_xpath('//*[@id="turn"]')
sel = Select(selectClass)

sel.select_by_index(1)

time.sleep(1)

start = driver.find_element_by_class_name('btn-rounded')
start.click()

next = driver.find_element_by_xpath('/html/body/div[1]/div/div/center/div[1]/form[1]/div[3]/div/button')

try:
    while next:
        time.sleep(2)
        radios = driver.find_elements_by_class_name('yn--1')

        for radio in radios:
            try:
                radio.click()
            except:
                None

        time.sleep(2)
        driver.execute_script("window.scroll(0, 0);")

        stars = driver.find_elements_by_class_name('star-5')

        for star in stars:
            print(star)
            try:
                star.click()
            except:
                print("Star exception occurred")

        driver.execute_script("window.scroll(0, 0);")

        suggestion_boxes = driver.find_elements_by_class_name('suggestion_boxes')

        for suggestion_box in suggestion_boxes:
            try:
                suggestion_box.send_keys('Good')
            except:
                None

        next.click()
        time.sleep(2)
except:
    None
