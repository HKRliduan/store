from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.get(r"F:/Python自动化/练习的html/弹框的验证/dialogs.html")
driver.maximize_window()
# driver.find_element_by_xpath("//*[@id='alert']").click
driver.find_element_by_xpath("//*[@id='confirm']").click()
time.sleep(3)
driver.switch_to.alert.accept()#确定
time.sleep(3)
driver.find_element_by_xpath("//*[@id='confirm']").click()
time.sleep(3)
driver.switch_to.alert.dismiss()#取消

driver.quit()