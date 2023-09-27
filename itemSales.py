from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import time
import subprocess
import os
import re

## step 1.) run IDE or command prompt as Administrator
## Choices: New, Reconditioned/Certified, Open box(never used), Used(normal wear), For parts, Other(see description)

# Load variables from .env
load_dotenv()

# The name of your task
task_name = os.environ.get("TASKNAME")

# Enable the task
subprocess.run(['schtasks', '/change', '/tn', task_name, '/enable'])

# Run the task
subprocess.run(['schtasks', '/run', '/tn', task_name])
time.sleep(45)  

# Start adb server
subprocess.run(["adb", "start-server"], shell=True)
subprocess.run(["adb", "devices"], shell=True)
subprocess.Popen(["appium"], shell=True)
time.sleep(60)  

def add_spaces_to_camel_case(s):
    # Add a space before all occurrences of a lowercase letter followed by an uppercase letter
    return re.sub(r'(?<=[a-z])(?=[A-Z])', ' ', s)

directory_path = os.environ.get("DIRECTORY")
filenames = sorted(os.listdir(directory_path), key=lambda x: os.path.getctime(os.path.join(directory_path, x)),reverse=True)
print(filenames)

i = 0
count = 0

for filename in filenames:
    
    parts = filename.split('-')   
     
    if len(parts) == 3:  
        
        i += 1
        if i == 2:
            break

        title, choice, price = parts
        title = add_spaces_to_camel_case(title)
        price = price.strip(".jpg")

    count += 1

print(title,choice,price)
print(count)

TITLE = title
CHOICE = choice
PRICE = price
ZIPCODE = os.environ.get("ZIPCODE")

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2'
)

appium_server_url = 'http://localhost:4723'

driver = webdriver.Remote(appium_server_url, capabilities)

offerUp = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@content-desc="OfferUp"]'))
)
offerUp.click()

post = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.Button[@content-desc="Post, Navigates to the Post screen"]'))
)
post.click()

title = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("post-flow-screen.1.listing-title.input")'))
)
title.click()

title_input = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("post-flow-screen.1.listing-title.input.text-entry")'))
)
title_input.clear()
title_input.send_keys(TITLE)

select = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("post-flow-screen.1.select-photo")'))
)
select.click()
select.click()

for index in range(1, count + 1):
    image = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().resourceId("post-flow-select-photos-screen.item.{index}")'))
    )
    image.click()

done = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("post-flow-select-photos-screen.done.button")'))
)
done.click()

time.sleep(20)
next = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value ='new UiSelector().resourceId("post-flow-screen.1.next.button")')
next.click()

condition = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.Button[@content-desc="Condition"]'))
)
condition.click()

time.sleep(10)
condition_choice = driver.find_element(by=AppiumBy.XPATH, value=f'//android.widget.TextView[@text="{CHOICE}" and @resource-id="ucl.flex-row.main.text"]')
condition_choice.click()

time.sleep(10)
next_two = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value ='new UiSelector().resourceId("post-flow-screen.2.next.button")')
next_two.click()
next_two.click()

price = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("post-flow.3.price.input")'))
)
price.click()

price_input = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("post-flow.3.price.input.text-entry")'))
)
price_input.clear()
price_input.send_keys(PRICE)

#firm_price_switch = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value ='new UiSelector().resourceId("post-flow.3.firm-price.flex-row.right-notification.toggle")')
#firm_price_switch.click()
#time.sleep(20)

time.sleep(10)
next_three = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value ='new UiSelector().resourceId("post-flow-screen.3.next.button")')
next_three.click()


set_location = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("post-flow.4.set-location.flex-row")'))
)
set_location.click()

zip_code = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("location-picker.zipcode.input")'))
)
zip_code.click()

zip_code_input = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("location-picker.zipcode.input.text-entry")'))
)
zip_code_input.clear()
zip_code_input.send_keys(ZIPCODE)

apply = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("location-picker.apply.button")'))
)
apply.click()

ship = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("post-flow.4.shell-and-ship.flex-row.right-notification.toggle")'))
)
ship.click()

for index, filename in enumerate(filenames):
    if index < count:
        os.remove(os.path.join(directory_path, filename))
        print("file deleted:", filename)


post_item = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("post-flow-screen.4.post.button")'))
)
post_item.click()


