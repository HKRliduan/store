from selenium import webdriver
import time

driver=webdriver.Chrome()
driver.get("http://www.qichacha.com")
driver.find_element_by_xpath('/html/body/header/div/ul/li[10]/a/span').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="normalLogin"]').click()
driver.find_element_by_xpath('//*[@id="nameNormal"]').send_keys("15803422277")
driver.find_element_by_xpath('//*[@id="pwdNormal"]').send_keys("ld199458")
driver.find_element_by_xpath('//*[@id="user_login_normal"]/button/b').click()