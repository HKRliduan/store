from selenium import webdriver
driver = webdriver.Chrome()
driver.get(r"F:/Python自动化/练习的html/上传文件和下拉列表/autotest.html")

driver.maximize_window()

driver.find_element_by_xpath("//*[@id='accountID']").send_keys("李端")
driver.find_element_by_xpath("//*[@id='passwordID']").send_keys("admin")
driver.find_element_by_xpath("//*[@id='areaID']").send_keys("北京市")
driver.find_element_by_xpath("//*[@id='sexID1']").click()
driver.find_element_by_xpath("//*[@value='Auterm']").click()
driver.find_element_by_xpath("//*[@value='winter']").click()
driver.find_element_by_xpath("//*[@name='file' and @type='file']").send_keys(r"F:\Python自动化\练习的html\上传文件和下拉列表\流鼻血.jpg")
driver.find_element_by_xpath("//*[@id='buttonID']").click()










