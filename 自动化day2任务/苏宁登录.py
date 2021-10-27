from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver= webdriver.Chrome()
driver.get("http://www.suning.com")
driver.maximize_window()
driver.find_element_by_xpath('//*[@id="reg-bar-node"]/a[1]').click()
driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[1]/a[2]/span').click()
driver.find_element_by_xpath('//*[@id="userName"]').send_keys("15803422277")
driver.find_element_by_xpath('//*[@id="password"]').send_keys("ld199458")
time.sleep(2)
driver.find_element_by_xpath('//*[@id="iar1_sncaptcha_button"]/span').click()
ac=ActionChains(driver)
le=driver.find_element_by_xpath('/html/body/div[5]/div[2]/div[2]/div[2]/div/div[3]')
try:
    for i in range(170,185):
        ac.click_and_hold(le).move_by_offset(i,0).perform()
        ac.release()
except Exception:
    print("验证通过了")
finally:
    driver.find_element_by_xpath('//*[@id="submit"]').click()
