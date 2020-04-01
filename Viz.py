from selenium import webdriver
print("This is a test to see if import works. ")
browser = webdriver.Chrome("/Users/naveenbandarage/Downloads/chromedriver")


#This method works to get 
browser.get("https://www.viz.com/")

elem = browser.find_element_by_xpath('//*[@id="curtain"]/header/div/nav/ul[1]/li[3]/a')
print(elem.text)
elem.click()

print("What series do you want to read?")
seriesRead = input("Series: ")
print(seriesRead)

mangaDictionary = {}
# mangaSeries = browser.find_elements_by_link_text("My Hero Academia: Vigilantes")
# mangaSeries.click()
# print(mangaSeries)


userInput = input("Do you want to quit? (y/n): ")

print("User input is: " + str(userInput))
#quitting works need to add delay. 
if userInput == "y":
    browser.close()
