from selenium import webdriver
import time

# creating an obect to open chrome
driver = webdriver.Chrome('/home/kali/Downloads/chromedriver')

# passing the url
driver.get('https://web.whatsapp.com/')

# getting data from user
name ='PARESHAN🤬👹👹AATMAS😡✊👊🤜'
msg ='hello \nhi \nbye bye'
count = int(input("enter the count : "))
input('enter anything after scanning QR code')

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name)).click()

msg_box = driver.find_element_by_class_name('_2A8P4')

time.sleep(2)

for i in range(count):
    msg_box.send_keys(msg)
    time.sleep(1)
    button = driver.find_element_by_class_name('_1E0Oz')
    button.click()
