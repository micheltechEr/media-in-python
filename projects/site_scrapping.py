from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException

import time
import pandas as pd

class WebMiiAuto:
    def __init__(self):
        self.openSite()
        self.fillInput()
        self.scrappingDatas()
    
    def openSite(self):
        global driver
        options = Options()
        options.profile = r'C:\Users\Ângelo Miguel\AppData\Roaming\Mozilla\Firefox\Profiles\n3vnmcxd.default-release-1685582882527'
        driver = webdriver.Firefox(options=options,executable_path=r'C:\Users\Ângelo Miguel\AppData\Local\Programs\Python\Python311\geckodriver-v0.33.0-win32\geckodriver.exe')
        driver.get("https://webmii.com")
        time.sleep(1)
    
    def fillInput(self):
        personName = input('Digite o nome da pessoa:\n')
        driver.find_element(By.ID,'name').send_keys(personName)
        driver.find_element(By.CLASS_NAME,'submit-button').click()

    def clickMore(self):
        try:
            buttonMore = driver.find_elements(By.ID,"more-news-button-block")
            if len(buttonMore) > 0:
                buttonClickMore = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.ID,"more-news-icon")))
                driver.execute_script("arguments[0].click()",buttonClickMore)
            else:
                time.sleep(4)
        except NoSuchElementException:
            time.sleep(4)

    def importData(self,resultFont,resultBox,resultContent,webFont,webTitle,webContent):
        if len(resultFont) != len(resultBox) != len(resultContent) != len(webFont) != len(webTitle) != len(webContent):
                raise ValueError("All arrays must be of the same length")
        else:
            df = pd.DataFrame({'boxFont':resultFont,'boxTitle':resultBox,'boxContent':resultContent,'websiteFont':webFont,'websiteTitle':webTitle,'websiteContent':webContent})
            df.to_csv('person_information.csv',index=False,encoding="utf-8")
            print(df)

    def scrappingDatas(self):
        time.sleep(10)
        self.clickMore()

        newsPersonElement = driver.find_elements(By.XPATH,'//div[@class="resultdate-box"]')
        webPersonElement = driver.find_elements(By.XPATH,'//div[@class="result-box"]')

        resultBoxFont = []
        resultBoxTitle = []
        resultBoxContent = []
        resultBoxWebFont = []
        resultBoxWebTitle = []
        resultBoxWebContent = []
        for newsInfo in newsPersonElement:
            resultBoxFont.append(newsInfo.find_element(By.XPATH,'./div[@class="resultdate-domainname"]').text)
            resultBoxTitle.append(newsInfo.find_element(By.XPATH,'./div[@class="resultdate-title"]').text)
            resultBoxContent.append(newsInfo.find_element(By.XPATH,'./div[@class="resultdate-snippet"]').text)
        
        for webInfo in webPersonElement:
            resultBoxWebFont.append(webInfo.find_element(By.XPATH,'./div[@id="result-title"]').text)
            resultBoxWebTitle.append(webInfo.find_element(By.XPATH,'./div[@id="result-title"]').text)
            resultBoxWebContent.append(webInfo.find_element(By.XPATH,'./div[@id="result-snippet"]').text)
        # driver.quit()
        min_length = min(len(resultBoxFont), len(resultBoxTitle), len(resultBoxContent), len(resultBoxWebFont), len(resultBoxWebTitle), len(resultBoxWebContent))
        resultBoxFont, resultBoxTitle, resultBoxContent, resultBoxWebFont, resultBoxWebTitle, resultBoxWebContent = zip(
        *zip(resultBoxFont[:min_length], resultBoxTitle[:min_length], resultBoxContent[:min_length], resultBoxWebFont[:min_length], resultBoxWebTitle[:min_length], resultBoxWebContent[:min_length])
        )
        self.importData(resultBoxFont,resultBoxTitle,resultBoxContent,resultBoxWebFont,resultBoxWebTitle,resultBoxWebContent)

start = WebMiiAuto()


