from selenium import webdriver
import time

driver= webdriver.Chrome()
driver.get('http://www.bilibili.com')
driver.maximize_window()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="i_cecream"]/div[1]/div[1]/ul[2]/li[1]/li/div/div/span').click()
data=driver.window_handles
driver.switch_to.window(data[1])
driver.find_element_by_xpath('//*[@id="login-username"]').send_keys("15803422277")
driver.find_element_by_xpath('//*[@id="login-passwd"]').send_keys("ld199458")
time.sleep(2)
driver.find_element_by_xpath('//*[@id="geetest-wrap"]/div/div[5]/a[1]').click()


