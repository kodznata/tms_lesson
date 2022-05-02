from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest


class TestSite1(unittest.TestCase):
    browser = None
    email = "lychishko@mail.ru"
    password = "17031985"
    url = "http://automationpractice.com/index.php"

    @classmethod
    def setUpClass(cls):
        cls.browser = webdriver.Chrome("C:/Users/Natasha/PycharmProjects/"
                                       "tms_lesson/chromedriver.exe")
        cls.browser.maximize_window()
        cls.browser.get(cls.url)
        cls.browser.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()

    def test_login(self):
        elem1 = self.browser.find_element(by=By.XPATH,
            value="/html/body/div/div[1]/header/div[2]/div/div/nav/div[1]/a")
        elem1.click()

        elem2 = self.browser.find_element(by=By.XPATH, value="/html/body/div/"
                    "div[2]/div/div[3]/div/div/div[2]/form/div/div[1]/input")
        elem2.click()
        elem2.send_keys(self.email)

        elem3 = self.browser.find_element(by=By.XPATH, value="/html/body/div/"
                "div[2]/div/div[3]/div/div/div[2]/form/div/div[2]/span/input")
        elem3.click()
        elem3.send_keys(self.password)

        elem4 = self.browser.find_element(by=By.ID, value="SubmitLogin")
        elem4.click()

        user = self.browser.find_element(by=By.XPATH, value="/html/body/div/"
                    "div[1]/header/div[2]/div/div/nav/div[1]/a/span").text
        self.assertEqual(user, "Natallia K")
