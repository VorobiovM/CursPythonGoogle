import datetime
import os
import os.path as path

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service

# noinspection SpellCheckingInspection
MONTHS = {
    1: "ianuarie",
    2: "februarie",
    3: "martie",
    4: "aprilie",
    5: "mai",
    6: "iunie",
    7: "iulie",
    8: "august",
    9: "septembrie",
    10: "octombrie",
    11: "noiembrie",
    12: "decembrie",
}
URL_PREFIX = "https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-"
URL_SUFFIX = "-ora-13-00"
DRIVER_PATH = path.normpath(r"C:\Users\Misha\PycharmProjects\CursPythonGoogle\Drivers\geckodriver.exe")
LOG_PATH = path.normpath(r"C:\Users\Misha\PycharmProjects\CursPythonGoogle\Drivers\geckodriver.log")
service = Service(executable_path=DRIVER_PATH, log_path=LOG_PATH)

try:
    month = int(input("Please enter a month [1-12]: "))
    day = int(input("Please enter a day [1-31]: "))
    date = datetime.date(year=2021, month=month, day=day)
except ValueError:
    # Default values
    date = datetime.date(year=2021, month=1, day=20)

covid_rates = dict()
with webdriver.Firefox(service=service) as browser:
    for i in range(7):
        iter_date = date + datetime.timedelta(days=i)
        browser.get(f"{URL_PREFIX}{iter_date.day}-{MONTHS[iter_date.month]}{URL_SUFFIX}")
        table = browser.find_element(By.CSS_SELECTOR, "table > tbody")
        rows = (table.find_elements(By.CSS_SELECTOR, "tr"))
        cells = []
        for row in rows[:-1]:
            data = row.find_elements(By.CSS_SELECTOR, "td")
            cells.append([datum.text for datum in data])
        if len(cells) == 44:  # Valid list has 44 rows, excluding total
            covid_rates.update({iter_date: cells})
    browser.close()

for date, table in covid_rates.items():
    df = pd.DataFrame(data=table[1:], columns=table[0])
    # noinspection PyTypeChecker
    df.to_csv(path_or_buf=f"COVID{os.sep}{date}.csv", encoding="utf-8")
