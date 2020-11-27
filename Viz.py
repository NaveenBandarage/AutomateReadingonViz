from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import difflib


readingBool = True
print("Welcome to the Viz automated reader!\n")
#just realised it won't be uptodate dependent on where the manga is currently uploaded. 
mangaDictionary = {'Demon Slayer' : '//*[@id="section0"]/div/div[2]/div[1]/a/a', 'My Hero' : '//*[@id="section0"]/div/div[2]/div[2]/a/div[2]', 'My Hero V' : '//*[@id="section0"]/div/div[2]/div[19]/a', 'One Punch Man' : '//*[@id="section0"]/div/div[2]/div[21]/a/div[2]', 'Haikyuu' : '//*[@id="section0"]/div/div[2]/div[11]/a', 'Black Clover' : '//*[@id="section0"]/div/div[2]/div[4]/a', 'Promised Neverland' : '//*[@id="section0"]/div/div[2]/div[5]/a', 'Dr Stone' : '//*[@id="section0"]/div/div[2]/div[6]/a', 'Undead Unlock' : '//*[@id="section0"]/div/div[2]/div[7]/a', 'Guardian of the witch' : '//*[@id="section0"]/div/div[2]/div[10]/a/div[2]', 'Chainsaw Man' : '//*[@id="section0"]/div/div[2]/div[13]/a/div[2]', 'Hells paradise' : '//*[@id="section0"]/div/div[2]/div[18]/a/div[2]', 'One Piece' : '//*[@id="section0"]/div/div[2]/div[22]/a/div[2]', 'Boruto' : '//*[@id="section0"]/div/div[2]/div[26]/a/div[2]', 'Mashle' : '//*[@id="section0"]/div/div[2]/div[9]/a/div[2]', 'Spy x Family' : '//*[@id="section0"]/div/div[2]/div[24]/a/div[2]', 'Jujutsu' : '//*[@id="section0"]/div/div[2]/div[14]/a/div[2]' }
mangaNameDictionary = {"One Piece" : "one-piece", "Kaiju No 8": "kaiju-no-8","Mashle": "mashle","Jujutsu Kaisen":"jujutsu-kaisen", "Black Clover":"black-clover", "Chainsaw Man":"chainsaw-man", "We never learn":"we-never-learn", "Undead Unlock":"undead-unluck", "Agravity Boys":"agravity-boys", "Ayakashi Triangle":"ayakashi-triangle", "Dr Stone":"dr-stone", "Hard Boiled Cop and Dolphin":"hard-boiled-cop-and-dolphin", "Magu Chan: God of Destruction":"magu-chan-god-of-destruction", "Mission: Yozakura Family":"mission-yozakura-family", "Moriking":"moriking", "Our Blood Oath":"our-blood-oath", "Phantom Seer":"phantom-seer", "My Hero Acaademia":"my-hero-academia", "Spy x Family":"spy-x-family"}


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

    #compare case sensitive strings.
    # s1.lower() == s3.lower()
    #https://www.edureka.co/blog/hash-tables-and-hashmaps-in-python/
    #prints out the keys
print("Key Value is =:" + mangaNameDictionary.get(closestWord[0])+ "\n") 
mangaName = mangaNameDictionary.get(closestWord[0])
browser = webdriver.Chrome(executable_path=r'/Users/naveenbandarage/Desktop/OtherProjects/PythonProjects/SeleniumViz/chromedriver')
    # browser = webdriver.Chrome("/Users/naveenbandarage/Downloads/chromedriver")
    # browser = webdriver.Chrome(ChromeDriverManager().install())

    #test here to see if I can get the element of the xpath and then check if the xpath contains the words of the series of the name and if they are equal then click on it. 
# elem = browser.find_elements_by_xpath('//*[@id="section0"]/div/div[2]/div[15]/a/div[2]')


    #This method works to get 
browser.get("https://www.viz.com/shonenjump/chapters/"+ mangaName)
if(browser.find_element_by_class_name('icon-close')):
        print("There exists an icon")
        elem = browser.find_element_by_class_name('icon-close')
        browser.implicitly_wait(30)
        print("There exists an icon after waiting")
        elem = browser.find_element_by_xpath('//*[@id="modal-follow"]/a/i')
        print("icon clicked and exited.")
        elem.click()
elem = browser.find_element_by_xpath('//*[@id="section0"]/div/div[2]/div[2]/a/div[2]/table/tbody/tr/td[2]/div/span/i')

elem.click()

fullScreen = browser.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div[2]/a[6]/i')


browser.implicitly_wait(20)


fullScreen.click()
    # fullScreen.click()

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
