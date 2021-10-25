from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.get("http://www.suning.com")
driver.find_element_by_xpath('//*[@id="searchKeywords"]').send_keys("iphone13")
driver.find_element_by_xpath('//*[@id="searchSubmit"]').click()
for handle in driver.window_handles:
    driver.switch_to.window(handle)
driver.find_element_by_xpath('//*[@id="0000000000-12314319135"]/div/div/div[2]/div[2]/a').click()
time.sleep(2)
for handle in driver.window_handles:
    driver.switch_to.window(handle)
driver.find_element_by_xpath('//*[@id="versionItemList"]/dd/ul/li[3]/a').click()
driver.find_element_by_xpath('//*[@id="addCart"]').click()

