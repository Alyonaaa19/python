import random
import time
from datetime import datetime

from config import browser
from pages.fuel_expenses_page import FuelExpensesPage
from pages.garage_page import GaragePage
from pages.home_page import HomePage
from pages.profile_page import ProfilePage
from pages.settings_page import SettingsPage


def test_qauto(browser):
    home_page = HomePage(browser)

    home_page.open()

    random_number = random.randint(1, 1000)

    name = "TestName"
    last_name = "TestLastName"
    email = f"testHomeWork{random_number}@gmail.com"
    password = "Qwerty12345"

    home_page.registration(name, last_name, email, password)
    time.sleep(2)

    garage_page = GaragePage(browser)
    garage_page.open_my_profile()

    time.sleep(2)
    profile_page = ProfilePage(browser)
    full_name = profile_page.get_full_name()
    split_full_name = full_name.split(" ")

    name_profile = split_full_name[0]
    last_name_profile = split_full_name[1]

    assert name_profile == name
    assert last_name_profile == last_name

    profile_page.open_garage_page()
    time.sleep(2)

    brand = "Audi"
    model = "Q7"
    mileage = 12345
    garage_page.add_car(brand, model, mileage)

    time.sleep(2)

    full_car_name = garage_page.get_name_car()
    car_mileage = garage_page.get_car_mileage()
    split_full_name_car = full_car_name.split(" ")

    brand_garage = split_full_name_car[0]
    model_garage = split_full_name_car[1]

    assert brand_garage == brand
    assert model_garage == model
    assert car_mileage == mileage

    add_mileage = 10

    liters = 10
    cost = 325.25

    garage_page.add_fuel_expense(liters, cost, add_mileage)

    fuel_expenses_page = FuelExpensesPage(browser)

    now = datetime.now()

    date = f"{now.day}.{now.month}.{now.year}"

    new_mileage = mileage + add_mileage

    time.sleep(3)
    assert date == fuel_expenses_page.get_date_from_page()
    assert new_mileage == fuel_expenses_page.get_mileage_from_page()

    litres_from_page = fuel_expenses_page.get_litres_from_page()

    assert litres_from_page == f"{liters}L"

    cost_from_page = fuel_expenses_page.get_cost_from_page()

    assert cost_from_page == f"{cost} USD"

    fuel_expenses_page.open_settings()

    settings_page = SettingsPage(browser)

    settings_page.remove_account()

    print("\nСергію, дякую за курс!)")
