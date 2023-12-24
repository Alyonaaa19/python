from pages.base_page import BasePage


class HomePage(BasePage):

    def open(self):
        self._driver.get("https://guest:welcome2qauto@qauto.forstudy.space/")

    def registration(self, name, last_name, email, password):
        self._find_element_by_xpath("//body//button[text()= 'Sign up']").click()
        name_input = self._find_element_by_id("signupName")
        name_input.send_keys(name)

        last_name_input = self._find_element_by_id("signupLastName")
        last_name_input.send_keys(last_name)

        email_input = self._find_element_by_id("signupEmail")
        email_input.send_keys(email)

        password_input = self._find_element_by_id("signupPassword")
        password_input.send_keys(password)

        re_enter_password_input = self._find_element_by_id("signupRepeatPassword")
        re_enter_password_input.send_keys(password)

        self._find_element_by_xpath("//body//button[text()='Register']").click()
