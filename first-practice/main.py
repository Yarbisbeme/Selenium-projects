from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

service = Service(executable_path="chromedriver.exe");
driver = webdriver.Chrome(service=service);
driver.get("http://selenium.dev/")

title = driver.title
print(title);

"""
    Verdadero
"""
assert "Selenium" in title;
driver.quit();