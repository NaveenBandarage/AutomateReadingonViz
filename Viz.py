from selenium import webdriver
print("This is a test to see if import works. ")
browser = webdriver.Chrome("/Users/naveenbandarage/Downloads/chromedriver")
browser.get("https://www.viz.com/")
elem = browser.find_element_by_xpath('//*[@id="curtain"]/header/div/nav/ul[1]/li[3]/a')
print(elem.text)
elem.click()
mangaSeries = browser.find_elements_by_link_text("Mitama Security: Spirit Busters")
print(mangaSeries)