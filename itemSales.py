
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import time
from appium.webdriver.common.touch_action import TouchAction


TITLE = "object"
CHOICE = "New"
PRICE = "20"
ZIPCODE = "11111"

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2'
)

appium_server_url = 'http://localhost:4723'

driver = webdriver.Remote(appium_server_url, capabilities)

offerUp = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@content-desc="OfferUp"]')
offerUp.click()
time.sleep(20)

post = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@content-desc="Post, Navigates to the Post screen"]')
post.click()
time.sleep(20)

title = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value ='new UiSelector().resourceId("post-flow-screen.1.listing-title.input")')
title.click()
time.sleep(20)

title_input = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value ='new UiSelector().resourceId("post-flow-screen.1.listing-title.input.text-entry")')
title_input.clear()
title_input.send_keys(TITLE)
time.sleep(20)

select = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value ='new UiSelector().resourceId("post-flow-screen.1.select-photo")')
select.click()
time.sleep(10)

select = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value ='new UiSelector().resourceId("post-flow-screen.1.select-photo")')
select.click()
time.sleep(20)

image1 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value ='new UiSelector().resourceId("post-flow-select-photos-screen.item.1")')
image1.click()
time.sleep(15)

image2 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value ='new UiSelector().resourceId("post-flow-select-photos-screen.item.2")')
image2.click()
time.sleep(15)

done = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value ='new UiSelector().resourceId("post-flow-select-photos-screen.done.button")')
done.click()
time.sleep(15)

next = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value ='new UiSelector().resourceId("post-flow-screen.1.next.button")')
next.click()
time.sleep(20)

condition = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@content-desc="Condition"]')
condition.click()
time.sleep(20)

condition_choice = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="New" and @resource-id="ucl.flex-row.main.text"]')
condition_choice.click()
time.sleep(20)

next_two = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value ='new UiSelector().resourceId("post-flow-screen.2.next.button")')
next_two.click()
time.sleep(20)

price = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value ='new UiSelector().resourceId("post-flow.3.price.input")')
price.click()
time.sleep(20)

#firm_price_switch = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value ='new UiSelector().resourceId("post-flow.3.firm-price.flex-row.right-notification.toggle")')
#firm_price_switch.click()
#time.sleep(20)

price_input = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value ='new UiSelector().resourceId("post-flow.3.price.input.text-entry")')
price_input.clear()
price_input.send_keys(PRICE)
time.sleep(20)

next_three = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value ='new UiSelector().resourceId("post-flow-screen.3.next.button")')
next_three.click()
time.sleep(20)

set_location = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value ='new UiSelector().resourceId("post-flow.4.set-location.flex-row")')
set_location.click()
time.sleep(20)

zip_code = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value ='new UiSelector().resourceId("location-picker.zipcode.input")')
zip_code.click()
time.sleep(20)

zip_code_input = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value ='new UiSelector().resourceId("location-picker.zipcode.input.text-entry")')
zip_code_input.clear()
zip_code_input.send_keys(ZIPCODE)
time.sleep(20)

apply = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value ='new UiSelector().resourceId("location-picker.apply.button")')
apply.click()
time.sleep(20)

ship = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value ='new UiSelector().resourceId("post-flow.4.shell-and-ship.flex-row.right-notification.toggle")')
ship.click()
time.sleep(20)

#post_item = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value ='new UiSelector().resourceId("post-flow-screen.4.post.button")')
#post_item.click()
#time.sleep(20)







