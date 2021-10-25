from selenium import webdriver
driver=webdriver.Chrome()
driver.get(r"F:/Python自动化/练习的html/跳转页面/pop.html")
driver.find_element_by_xpath("//*[@id='goo']").click()













