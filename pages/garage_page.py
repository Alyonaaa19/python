import time

from pages.base_page import BasePage


class GaragePage(BasePage):
    def open_my_profile(self):
        self._find_element_by_xpath("//a[@routerlink='profile']").click()

    def add_car(self, brand, model, mileage):
        self._find_element_by_xpath("//body//button[text()='Add car']").click()
        time.sleep(2)

        self._find_element_by_id("addCarBrand").send_keys(brand)
        self._find_element_by_id("addCarModel").send_keys(model)
        self._find_element_by_id("addCarMileage").send_keys(mileage)

        self._find_element_by_xpath("//body//button[text()='Add']").click()

    def get_name_car(self):
        return self._find_element_by_xpath("/html/body/app-root/app-global-layout/div/div/div/app-panel-layout/div/div/"
                                           "div/div[2]/div/app-garage/div/div[2]/div/ul/li/app-car/div/"
                                           "div[1]/div[1]/div[2]/p").text

    def get_car_mileage(self):
        return int(self._find_element_by_xpath("/html/body/app-root/app-global-layout/div/div/div/app-panel-layout"
                                               "/div/div/div/div[2]/div/app-garage/div/div["
                                               "2]/div/ul/li/app-car/div/div["
                                               "2]/app-update-mileage-form/form/input").get_attribute("value"))

    def add_fuel_expense(self, number_of_liters, total_cost, mileage):
        self._find_element_by_xpath("//body//button[text()='Add fuel expense']").click()
        time.sleep(2)

        self._find_element_by_id("addExpenseLiters").send_keys(number_of_liters)

        self._find_element_by_id("addExpenseTotalCost").send_keys(total_cost)
        mileage_input = self._find_element_by_id("addExpenseMileage")
        mileage_input.clear()
        mileage_input.send_keys(self.get_car_mileage() + mileage)

        self._find_element_by_xpath("//body//button[text()='Add']").click()
