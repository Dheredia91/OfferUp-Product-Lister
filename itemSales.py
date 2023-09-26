from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

TITLE = "object"
CHOICE = "New"
PRICE = "20"
ZIPCODE = "95212"

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


image1 = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("post-flow-select-photos-screen.item.1")'))
)
image1.click()

image2 = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("post-flow-select-photos-screen.item.2")'))
)
image2.click()

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

# post_item = WebDriverWait(driver, 20).until(
#     EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("post-flow-screen.4.post.button")'))
# )
# post_item.click()


