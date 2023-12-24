import pytest
from selenium import webdriver


@pytest.fixture
def browser():
    return webdriver.Chrome()
