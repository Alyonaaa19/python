from pages.base_page import BasePage


class ProfilePage(BasePage):
    def get_full_name(self):
        return self._find_element_by_xpath("/html/body/app-root/app-global-layout/div/div/div/app-panel-layout/div/div"
                                           "/div/div[2]/div/app-profile/div/div[2]/div/p").text

    def open_garage_page(self):
        self._find_element_by_xpath("//a[@routerlink='garage']").click()
