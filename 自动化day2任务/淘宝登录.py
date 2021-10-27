from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver=webdriver.Chrome()
driver.get("http://www.taobao.com")
driver.maximize_window()
driver.find_element_by_xpath('//*[@id="J_SiteNavLogin"]/div[1]/div[1]/a[1]').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="fm-login-id"]').send_keys("15803422277")
driver.find_element_by_xpath('//*[@id="fm-login-password"]').send_keys("ld199458")
driver.find_element_by_xpath('//*[@id="login-form"]/div[4]/button').click()
time.sleep(2)
ac=ActionChains(driver)
le=driver.find_element_by_xpath('//*[@id="nc_1_n1z"]')
time.sleep(3)
ac.click_and_hold(le).move_by_offset(258,0).perform()
ac.release()