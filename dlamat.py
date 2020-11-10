from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 
import selenium
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener
from termcolor import colored
import pyfiglet
import sys
import getpass

class GGBOT():
    
    
    def __init__(self):
        
        self.gender = r""
        self.login = r""
        self.passwd = r""
        self.message = r""
        
        
        print("\n")
        print(colored("#################################################################",'yellow'))
        ascii_banner = pyfiglet.figlet_format("GaduGaduBot")
        ascii_bannerVers = pyfiglet.figlet_format("Version     1.0")
        print(colored(ascii_banner, 'yellow'))
        print(colored(ascii_bannerVers,'yellow'),end="")
        print(colored("#################################################################",'yellow'))
        print("\n")
        print(colored("[Set Gender -", 'magenta'), colored("K or M, Q to Quit", 'yellow'), colored("] ---> ",'magenta'), end="")
        self.gender = input("")

        print(colored("[GG number] ---> ", 'magenta'), end="")
        self.login = input("")
        
        
        while(len(self.login) != 8):
            print(colored("[ERROR] invalid number-> ", 'red'), end="")
            self.login = input("")
            
        print(colored("[GG password] ---> ", 'magenta'))
        self.passwd = getpass.getpass("")
        
        with open('dataGG.txt', 'r') as file:
            self.message = file.read()
        
        
        
        self.driver = webdriver.Chrome()


    def loginGG(self):     
        
        login = ""
        passwd = ""
        #login = self.login
        #passwd = self.passwd
        
        
        self.driver.get(r'https://login.ggapp.com/scopes_request?client_id=13a8aec5f6e60b5880d83fdd18a314d5&context=parent&id=frame_7399&origin=https%3A%2F%2Fwww.ggapp.com%2F&transport=PostMessage&useStatus=true&forceSyncStatus=false&lang=en&urlhashUri=https%3A%2F%2Fwww.ggapp.com%2Fwp-content%2Fplugins%2Facforms%2Ftransport.html#client_id=13a8aec5f6e60b5880d83fdd18a314d5&context=parent&id=frame_7399&origin=https%3A%2F%2Fwww.ggapp.com%2F&transport=PostMessage&useStatus=true&forceSyncStatus=false&lang=en&urlhashUri=https%3A%2F%2Fwww.ggapp.com%2Fwp-content%2Fplugins%2Facforms%2Ftransport.html')
        self.driver.maximize_window()

        time.sleep(2.0)   
        usernameLabel = self.driver.find_element_by_css_selector('#login_input')   
        usernameLabel.send_keys(login)
        time.sleep(1.0) 
          
        passwordLabel = self.driver.find_element_by_css_selector('#password')
        passwordLabel.send_keys(passwd)
        time.sleep(1.0) 
        
        submitLabel = self.driver.find_element_by_css_selector('button.btn')
        submitLabel.click()
        time.sleep(4.0) 
        self.driver.get(r'https://ggapp.com')
        time.sleep(1.0)
        self.driver.refresh()
        time.sleep(2.0)
        self.driver.refresh()
        time.sleep(2.0)
        self.driver.refresh()
        time.sleep(5.0)
        
    def sendMessage(self):
        time.sleep(1.0)
        
        
        nextDivIteratorText = 1
        while True:
            try:
                print(colored('[INFO]-Getting div : /html/body/div[1]/div[4]/div[2]/div/div[1]/div[5]/div[{}]/div[2]/div[8]/div[2]/div/div','green').format(nextDivIteratorText))
                writeHello = self.driver.find_element_by_xpath('/html/body/div[1]/div[4]/div[2]/div/div[1]/div[5]/div[{}]/div[2]/div[8]/div[2]/div/div'.format(nextDivIteratorText))
                print(colored("[INFO] SENDING MESSAGE",'green'))
                writeHello.send_keys(self.message)
            except selenium.common.exceptions.NoSuchElementException:
                nextDivIteratorText += 1
                continue
            except selenium.common.exceptions.ElementNotInteractableException:
                continue
            break
                
                
        time.sleep(1.0)
        nextDivIteratorSubmit = 1
        
        while True:
            try:
                print(colored('[INFO]-Getting div : /html/body/div[1]/div[4]/div[2]/div/div[1]/div[5]/div[{}]/div[2]/div[8]/div[3]/div/a[2]','green').format(nextDivIteratorSubmit))
                writeSubmitHello = self.driver.find_element_by_xpath('/html/body/div[1]/div[4]/div[2]/div/div[1]/div[5]/div[{}]/div[2]/div[8]/div[3]/div/a[2]'.format(nextDivIteratorSubmit))
                time.sleep(1.0)
                print(colored("[INFO] SENDING MESSAGE", 'green'))
                writeSubmitHello.click()
            except selenium.common.exceptions.NoSuchElementException:
                #writeSubmitHello = self.driver.find_element_by_xpath('/html/body/div[1]/div[4]/div[2]/div/div[1]/div[5]/div[%i]/div[2]/div[8]/div[3]/div/a[2]'.format(nextDivIterator))
                nextDivIteratorSubmit += 1
                continue
            except selenium.common.exceptions.ElementNotInteractableException:
                continue
            break
        
        
        time.sleep(1.0)
        
        nextDivIteratorClose = 1
        
        while True:
            try:
                print(colored('[INFO]-Getting div : /html/body/div[1]/div[4]/div[2]/div/div[1]/div[5]/div[{}]/div[2]/div[1]/div[1]/a[2]/i','green').format(nextDivIteratorClose))
                closeConv = self.driver.find_element_by_xpath('/html/body/div[1]/div[4]/div[2]/div/div[1]/div[5]/div[{}]/div[2]/div[1]/div[1]/a[2]/i'.format(nextDivIteratorClose))
                closeConv.click()
            except selenium.common.exceptions.NoSuchElementException:
                nextDivIteratorClose += 1
                continue
        
            except selenium.common.exceptions.ElementNotInteractableException:
                continue
            break
                
        time.sleep(1.0)
        
    
    def initiateConversation(self):
        
        self.driver.get(r'https://www.ggapp.com/#roulette')
        time.sleep(2.0)
        self.gender = "K"
        
        
        while True:
            try:
                setGender = self.driver.find_element_by_xpath('/html/body/div[1]/div[4]/div[2]/div/div[2]/div/div[1]/div[9]/div[2]/label/input')
                setGender.click()
                time.sleep(1.0)
            except:
                continue
            break

        
        if self.gender == 'K': #or self.gender == 'KOBIETA' or self.gender == 'WOMAN' or self.gender == 'W':
            clickOnFemale = self.driver.find_element_by_xpath('/html/body/div[1]/div[4]/div[2]/div/div[3]/div/div[1]/div/ul/li[1]/label/img')
            clickOnFemale.click()
            time.sleep(1.0)
            
        elif self.gender == 'M': #or self.gender == 'MAN' or self.gender == 'MĘŻCZYZNA' or self.gender == 'MEZCZYZNA':
            clickOnMale = self.driver.find_element_by_xpath('/html/body/div[1]/div[4]/div[2]/div/div[3]/div/div[1]/div/ul/li[2]/label/img')
            clickOnMale.click()
            time.sleep(1.0)
            
        else:
            print(colored("[Error]-> Such gender does not exists", 'red'))
            sys.exit(0)
            
        returnToSearch = self.driver.find_element_by_xpath('/html/body/div[1]/div[4]/div[2]/div/div[3]/div/div[3]/div[1]/label/input')
        returnToSearch.click()
        time.sleep(1.0)

        randomConv = self.driver.find_element_by_xpath('/html/body/div[1]/div[4]/div[2]/div/div[2]/div/div[1]/div[6]/div/label/input')
        randomConv.click()
        
         
        print(colored("[INFO] SEARCHING...",'green'))
        start_time = time.time() 
        #while True:

        time.sleep(2.0)
            #print("[TIMER2] Finding user..." + colored(str((time.time() - start_time)),'green'))
            #try:
                #beginConv = self.driver.find_element_by_xpath('/html/body/div[1]/div[4]/div[2]/div/div[2]/div/div[1]/div[8]/div[1]/label/input')
                #time.sleep(1.0)
            
            #except selenium.common.exceptions.ElementNotInteractableException:
            #    continue
            #except selenium.common.exceptions.NoSuchElementException:
            #    continue
            #break    
        start_time = time.time()  
            
        while True:
            
            print("[TIMER] Finding user..." + colored(str((time.time() - start_time)),'green'))
            
            try:
                beginConv = self.driver.find_element_by_xpath('/html/body/div[1]/div[4]/div[2]/div/div[2]/div/div[1]/div[8]/div[1]/label/input')
                beginConv.click()
            except:
                if (time.time() - start_time) >= 30:
                
                    try:
                        randomConv = self.driver.find_element_by_xpath('/html/body/div[1]/div[4]/div[2]/div/div[2]/div/div[1]/div[6]/div/label/input')
                        randomConv.click()
                        start_time = time.time()  
                    except:
                        continue
                # nie znalazlo ale mniej niz 30s
                continue
            break
                
        time.sleep(1.0)    
        self.sendMessage()
        
    
    
    def keepGoing(self):
        
        while True:
            
            self.driver.get(r'https://www.ggapp.com/#roulette')
            time.sleep(1.0)
            
            while True:
                try:
                    findNext = self.driver.find_element_by_xpath('/html/body/div[1]/div[4]/div[2]/div/div[2]/div/div[1]/div[8]/div[2]/label/input') 
                    findNext.click()
                    print("findNext")
                    time.sleep(1.0)
                except:
                    continue
                break

            
            start_time = time.time()  # OD TERAZ LOSUJE
            time.sleep(1.0)
            
            while True:
                
                print("[TIMER] Finding user..." + colored(str((time.time() - start_time)),'green'))
                try:
                    beginConv = self.driver.find_element_by_xpath('/html/body/div[1]/div[4]/div[2]/div/div[2]/div/div[1]/div[8]/div[1]/label/input')
                    beginConv.click()
                except selenium.common.exceptions.ElementNotInteractableException:
                    
                    if (time.time() - start_time) >= 30:
                        try:
                            print("Minal czas")
                            restartConv = self.driver.find_element_by_xpath('/html/body/div[1]/div[4]/div[2]/div/div[2]/div/div[1]/div[6]/div/label/input')
                            restartConv.click()
                        except:
                            continue
                    continue # do selenium.common.exceptions.ElementNotInteractableException:
                break
            
            print(colored("[INFO] USER FOUND...",'green'))
            time.sleep(1.0)
            self.sendMessage()
        


def main():
    bot1 = GGBOT()
    bot1.loginGG()
    bot1.initiateConversation()
    bot1.keepGoing()




if __name__ == '__main__':
    main()
