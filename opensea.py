
from selenium.webdriver.common.by import By
from seleniumwire import webdriver
from time import sleep

from metaMask import MetaMask # либа функций метамаска
from sessionChromeDriver.session import Session # либа создания/загрузки профиля хрома


class OpenSea:

    def __init__(self, profile):
        self.URL = "https://testnets.opensea.io/"
        self.driver = Session(profile).createChromeDriverSession()

    def connectWallet(self):
        self.driver.get(self.URL)
        sleep(5)
        self.driver.find_elements(By.CLASS_NAME, "material-icons")[1].click()
        sleep(1)
        self.driver.find_element(By.CLASS_NAME, "bBXuZv").click()
        sleep(1)
        self.driver.find_element(By.CLASS_NAME, "cOrlxV").click()
        sleep(10)
        MetaMask(phrase, metamask_pass, self.driver).connectWallet()
        sleep(10)



    def addToCart(self, urlNft):
        self.driver.get(urlNft)
        sleep(7)
        self.driver.find_element(By.CLASS_NAME, "ecluaf").click()
        sleep(10)


    def buyNowNFT(self):
        self.driver.get(self.URL)
        sleep(7)
        self.driver.find_elements(By.CLASS_NAME, "material-icons-outlined")[1].click()
        sleep(1)
        self.driver.find_element(By.CLASS_NAME, "bBXuZv").click()
        sleep(7)
        MetaMask(phrase, metamask_pass, self.driver).confirmTransaction()
        sleep(15)




# profile3 = "Profile 3"
# a = OpenSea(profile3)
# a.connectWallet()
# a.addToCart("https://testnets.opensea.io/assets/goerli/0xe29f8038d1a3445ab22ad1373c65ec0a6e1161a4/167")
# a.buyNowNFT()