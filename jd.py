from selenium import webdriver
import time

driver=webdriver.Chrome()
driver.get("http://www.jd.com")
h = driver.current_window_handle
driver.find_element_by_xpath("//*[@id='key']").send_keys("小米11pro")
driver.find_element_by_xpath("//*[@class='button']").click()
for handle in driver.window_handles:
    driver.switch_to.window(handle)
time.sleep(2)
driver.find_element_by_xpath('//*[@id="J_goodsList"]/ul/li[1]/div/div[4]/a').click()
for handle in driver.window_handles:
    driver.switch_to.window(handle)
driver.find_element_by_xpath('//*[@id="choose-attr-2"]/div[2]/div[3]/a').click()
time.sleep(2)
for handle in driver.window_handles:
    driver.switch_to.window(handle)
driver.find_element_by_xpath('//*[@id="btn-reservation"]').click()
time.sleep(2)
for handle in driver.window_handles:
    driver.switch_to.window(handle)
driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[1]/div/div[3]/a').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="loginname"]').send_keys("15803422277")
driver.find_element_by_xpath('//*[@id="nloginpwd"]').send_keys("ld199458")
driver.find_element_by_xpath('//*[@id="loginsubmit"]').click()
