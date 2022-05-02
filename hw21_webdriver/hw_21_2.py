from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import unittest


class TestSite2(unittest.TestCase):
    browser = None
    first_name = "Natallia"
    last_name = "Kod"
    phone = "7777777"
    email = "lychishko@mail.ru"
    address = "Gorovca 22"
    city = "Minsk"
    state = "Minsk region"
    postal_code = "220194"
    user_name = "lych"
    password = "170385"
    url = "http://demo.guru99.com/test/newtours/register.php"

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

    def test_registration(self):
        field1 = self.browser.find_element(by=By.NAME, value="firstName")
        field1.click()
        field1.send_keys(self.first_name)

        field2 = self.browser.find_element(by=By.NAME, value="lastName")
        field2.click()
        field2.send_keys(self.last_name)

        field3 = self.browser.find_element(by=By.NAME, value="phone")
        field3.click()
        field3.send_keys(self.phone)

        field4 = self.browser.find_element(by=By.NAME, value="userName")
        field4.click()
        field4.send_keys(self.email)

        field5 = self.browser.find_element(by=By.NAME, value="address1")
        field5.click()
        field5.send_keys(self.address)

        field6 = self.browser.find_element(by=By.NAME, value="city")
        field6.click()
        field6.send_keys(self.city)

        field7 = self.browser.find_element(by=By.NAME, value="state")
        field7.click()
        field7.send_keys(self.state)

        field8 = self.browser.find_element(by=By.NAME, value="postalCode")
        field8.click()
        field8.send_keys(self.postal_code)

        field9_selector = Select(self.browser.find_element
                                 (by=By.NAME, value="country"))
        field9_selector.select_by_value("BELARUS")

        field10 = self.browser.find_element(by=By.NAME, value="email")
        field10.click()
        field10.send_keys(self.user_name)

        field11 = self.browser.find_element(by=By.NAME, value="password")
        field11.click()
        field11.send_keys(self.password)

        field12 = self.browser.find_element(by=By.NAME,
                                            value="confirmPassword")
        field12.click()
        field12.send_keys(self.password)

        button = self.browser.find_element(by=By.NAME, value="submit")
        button.click()

        name_surname = self.browser.find_element(by=By.XPATH, value="/html/"
        "body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/"
        "td[2]/table/tbody/tr[3]/td/p[1]/font/b").text
        self.assertEqual(name_surname, f'Dear {self.first_name}'
                                       f' {self.last_name},')

        username = self.browser.find_element(by=By.XPATH, value="/html/body/"
        "div[2]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]"
        "/table/tbody/tr[3]/td/p[3]/font/b").text
        self.assertEqual(username, f'Note: Your user name is'
                                   f' {self.user_name}.')
