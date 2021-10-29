from selenium import webdriver
import time

driver=webdriver.Chrome()
driver.get("http://localhost:8080/HKR")
driver.maximize_window()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="loginname"]').send_keys("liduan")
keys = driver.find_element_by_xpath('//*[@id="password"]').send_keys("123456")
driver.find_element_by_xpath('//*[@id="submit"]').click()

driver.find_element_by_xpath('//*[@id="img"]').click()
h=driver.current_window_handle
time.sleep(2)
#driver.find_element_by_xpath('//*[@id="ul_pic"]/li[10]/img').click()
driver.find_element_by_xpath('//*[@id="file1"]').send_keys(r"F:\Python自动化\练习的html\上传文件和下拉列表\流鼻血.jpg")
driver.find_element_by_xpath('//*[@id="pic_btn"]').click()

driver.quit()