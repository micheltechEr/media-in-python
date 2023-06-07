from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.firefox.options import Options

class NetflixAuto:
    global driver
    def __init__(self) :
        self.startGeckoDriver()
        self.inputCredentials()
        self.logNetflix()
        self.selectProfile()
        self.selectMovie()
    
    def startGeckoDriver(self):
        
        global driver
        options = Options()
        options.profile = r'C:\Users\Ângelo Miguel\AppData\Roaming\Mozilla\Firefox\Profiles\n3vnmcxd.default-release-1685582882527'
        driver = webdriver.Firefox(options=options,executable_path=r'C:\Users\Ângelo Miguel\AppData\Local\Programs\Python\Python311\geckodriver-v0.33.0-win32\geckodriver.exe')
        driver.get("https://www.netflix.com/br/login")
        time.sleep(4)

    def inputCredentials(self):
         global credentials
         emailUser = input('Type your email \n')
         passUser = input('Type your password\n')

         credentials = {
            "email": emailUser,
            "password": passUser
        }
         
    def logNetflix(self):
        driver.find_element(By.ID,'id_userLoginId').send_keys(credentials["email"])
        driver.find_element(By.ID,'id_password').send_keys(credentials["password"])
        driver.find_element(By.CLASS_NAME,"login-button").click()
        time.sleep(3)
        try:
            errorElements = driver.find_elements(By.XPATH,'//div[@data-uia="error-message-container"]|//div[@data-uia="password-field+error"]')
            if len(errorElements) > 0:
                print('\033[31mInvalid credentials\033[1')
            else:
                time.sleep(4)
        except NoSuchElementException:
            time.sleep(4)

    def selectProfile(self):
        global new_url
        new_url = 'https://www.netflix.com/browse'

        if driver.current_url == new_url:
            print('\033[32mSuccessfully\033[0m')
            driver.find_element(By.XPATH,'//div[@data-profile-guid="TN2JYHRYKJGXXJPN4JTVWOG2WQ"]').click()
            anchor = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//a[@href="/browse/genre/34399"]')))
            driver.execute_script("arguments[0].click()",anchor)
        else:
            print('Navegação mal sucedida')
        time.sleep(4)

    def selectMovie(self):
        driver.find_element(By.CLASS_NAME,"searchTab").click()
        time.sleep(2)

        movieName = input('Type the movie or the serie name\n')
        driver.find_element(By.ID,"searchInput").send_keys(movieName)
        driver.find_element(By.ID,"searchInput").send_keys(Keys.ENTER)
        try:
            moviePlay = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH, f'//div[@class="ptrack-content"]/a[@aria-label="{movieName}"]')))
            driver.execute_script("arguments[0].click();",moviePlay)
        except NoSuchElementException:
            print('The movie isn´t or on the list. Or you typed it incorretly')

start = NetflixAuto()
