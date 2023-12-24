import time

from pages.base_page import BasePage


class SettingsPage(BasePage):

    def remove_account(self):
        self._find_element_by_xpath("//body//button[text()='Remove my account']").click()
        time.sleep(1)
        self._find_element_by_xpath("//body//button[text()='Remove']").click()
