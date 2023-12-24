from selenium.webdriver.common.by import By


class BasePage:

    def __init__(self, driver):
        self._driver = driver

    def _find_element_by_id(self, element_id):
        return self._driver.find_element(By.ID, element_id)

    def _find_element_by_xpath(self, xpath):
        return self._driver.find_element(By.XPATH, xpath)
