from pages.base_page import BasePage


class FuelExpensesPage(BasePage):

    def open_settings(self):
        self._find_element_by_xpath("//a[@routerlink='settings']").click()

    def get_date_from_page(self):
        return self._find_element_by_xpath("//body//tr//td[1]").text

    def get_mileage_from_page(self):
        return int(self._find_element_by_xpath("//body//tr//td[2]").text)

    def get_litres_from_page(self):
        return self._find_element_by_xpath("//body//tr//td[3]").text

    def get_cost_from_page(self):
        return self._find_element_by_xpath("//body//tr//td[4]").text
