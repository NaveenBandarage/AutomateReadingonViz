from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import difflib

booleanA = True
readingBool = True
while(booleanA):
    print("Welcome to the Viz automated reader!\n")
    mangaNameDictionary = {"One Piece" : "one-piece", "Kaiju No 8": "kaiju-no-8","Mashle": "mashle","Jujutsu Kaisen":"jujutsu-kaisen", "Black Clover":"black-clover", "Chainsaw Man":"chainsaw-man", "We never learn":"we-never-learn", "Undead Unlock":"undead-unluck", "Agravity Boys":"agravity-boys", "Ayakashi Triangle":"ayakashi-triangle", "Dr Stone":"dr-stone", "Hard Boiled Cop and Dolphin":"hard-boiled-cop-and-dolphin", "Magu Chan: God of Destruction":"magu-chan-god-of-destruction", "Mission: Yozakura Family":"mission-yozakura-family", "Moriking":"moriking", "Our Blood Oath":"our-blood-oath", "Phantom Seer":"phantom-seer", "My Hero Academia":"my-hero-academia", "Spy x Family":"spy-x-family"}

    print("These are all the series to read:")
    for x in mangaNameDictionary:
        print(x)  
    boolean = True     
    while(boolean):
        print("\nWhat series do you want to read? (Must match names printed above)")
        seriesRead = input("Series: ")

        closestWord = difflib.get_close_matches(seriesRead, list(mangaNameDictionary.keys()), 1, 0.4)
        if(len(closestWord)!=0):
            print("The series is: " + closestWord[0])
            boolean = False
        else:
            print("Input was not a valid series name")
            print("Looping to try again...")

    print("Key Value is =:" + mangaNameDictionary.get(closestWord[0])+ "\n") 
    mangaName = mangaNameDictionary.get(closestWord[0])
    browser = webdriver.Chrome(executable_path=r'/Users/naveenbandarage/Desktop/OtherProjects/PythonProjects/SeleniumViz/chromedriver')

        #This method works to get 
    browser.get("https://www.viz.com/shonenjump/chapters/"+ mangaName)
    if(browser.find_element_by_class_name('icon-close')):
            print("There exists an icon...")
            elem = browser.find_element_by_class_name('icon-close')
            browser.implicitly_wait(30)
            print("There exists an icon after waiting...")
            elem = browser.find_element_by_xpath('//*[@id="modal-follow"]/a/i')
            print("Therefore an icon clicked and exited.")
            elem.click()
    # elem = browser.find_element_by_xpath('//*[@id="section0"]/div/div[2]/div[2]/a/div[2]/table/tbody/tr/td[2]/div/span/i')
    # elem = browser.find_element_by_xpath('//*[@id="section0"]/div/div[2]/div[2]/a/div[2]')
    elem = browser.find_element_by_xpath('//*[@id="section0"]/div/div[2]/div[2]/a/div[2]/table/tbody/tr/td[2]/div/span')
    elem.click()

    fullScreen = browser.find_element_by_xpath('//*[@id="reader_tools"]/a[6]/i')
    

    browser.implicitly_wait(20)


    fullScreen.click()

    keepReading = input("Do you want to keep reading (y/n): " )
    if keepReading == "y":
            readingBool = True
            browser.close()

    else:
            readingBool = False

    userInput = input("Do you want to quit? (y/n): ")


    #quitting works need to add delay. 
    if userInput == "y":
        print("Quitting thanks for using!")
        browser.close()
        booleanA = False
