from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

print("This is a test to see if import works. ")
browser = webdriver.Chrome("/Users/naveenbandarage/Downloads/chromedriver")


#This method works to get 
browser.get("https://www.viz.com/")

elem = browser.find_element_by_xpath('//*[@id="curtain"]/header/div/nav/ul[1]/li[3]/a')
# print(elem.text)
elem.click()
# wait = WebDriverWait(manga, 10)
browser.implicitly_wait(20)
#Demonslaye
# manga = browser.find_element_by_xpath('//*[@id="section0"]/div/div[2]/div[1]/a/div[2]')


# #My hero
manga = browser.find_element_by_xpath('//*[@id="section0"]/div/div[2]/div[2]/a/div[2]')

manga.click()
browser.implicitly_wait(10)


#this works for all manga opens the latest chapter.
chapter =  browser.find_element_by_xpath('/html/body/div[3]/section[2]/div/div[2]/div[2]') 

print(chapter.text)
chapter.click()

browser.implicitly_wait(10)it 

fullScreen = browser.find_element_by_xpath('//*[@id="reader_tools"]/a[6]/i')
fullScreen.click()
# elem = browser.find_element_by_link_text("Ch. 266")
# print(elem.text)
print("What series do you want to read?")
seriesRead = input("Series: ")
print(seriesRead)

#compare case sensitive strings. 
# s1.lower() == s3.lower()
#https://www.edureka.co/blog/hash-tables-and-hashmaps-in-python/
mangaDictionary = {'Demon Slayer' : '//*[@id="section0"]/div/div[2]/div[1]/a/a', 'My Hero' : '', 'My Hero V' : '', 'One Punch Man' : '', 'Haikyuu' : '', 'Black Clover' : '', 'Promised Neverland' : '', 'Dr Stone' : '', 'Undead Unlock' : 'Guardian of the witch', 'Chainsaw Man' : '', 'Hells paradise' : '', 'One Piece' : '', 'Boruto' : '', 'Mashe' : '', 'One Piece' : '',  }
#prints out the keys
print("These are all the series:")
for x in mangaDictionary:
    print(x)  
# mangaSeries = browser.find_elements_by_link_text("My Hero Academia: Vigilantes")
# mangaSeries.click()
# print(mangaSeries)


userInput = input("Do you want to quit? (y/n): ")

print("User input is: " + str(userInput))
#quitting works need to add delay. 
if userInput == "y":
    browser.close()
