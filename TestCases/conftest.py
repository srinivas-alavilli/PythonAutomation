from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

#ser_Obj = Service(r"C:\Users\SrinivasaRaoAlavilli\PythonProgramming\pythonHybridFrWork\Browser\chromedriver.exe")

ser_Obj = Service('.\\Browser\\chromedriver.exe')

# Driver Initialization
@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome(service=ser_Obj)
        print("Launching Chrome Browser")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Launching Firefox Browser")
    else:
        driver = webdriver.Edge()
        print("Launching Edge Browser")
    return driver


def pytest_addoption(parser):  # This will get the browser name from CLI/hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # This will return the browser value to setup method
    return request.config.getoption("--browser")


####################### Generating the Html Report #######################

# It is a hook for adding Environment info to Html report
def pytest_configure(config):
    config._metadata = {
        "Tester": "Srinivas Alavilli",
        "Project Name": "Non Commerce",
        "Module Name": "Customers"
    }

    # config._metadata['Project Name'] = 'Non Commerce'
    # config._metadata['Module Name'] = 'Customers'
    # config._metadata['Tester'] = 'Srinivas'


# It is a hook for delete/Modify Environment info to Html report
# @pytest.mark.optionalhook
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop('JAVA_HOME', None)
    metadata.pop('Plugins', None)
