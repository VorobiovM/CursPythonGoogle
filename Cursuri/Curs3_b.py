import os
import os.path as path

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service


DRIVER_PATH = path.normpath(r"C:\Users\Misha\PycharmProjects\CursPythonGoogle\Drivers\geckodriver.exe")
LOG_PATH = path.normpath(r"C:\Users\Misha\PycharmProjects\CursPythonGoogle\Drivers\geckodriver.log")
URL = "https://www.bnr.ro/files/xml/nbrfxrates2021.htm"
service = Service(executable_path=DRIVER_PATH, log_path=LOG_PATH)

with webdriver.Firefox(service=service) as browser:
    browser.get(URL)
    table = browser.find_element(By.XPATH, '//*[@id="Data_table"]')
    table_text = table.text
    lista = table_text.split('\n')

    header = browser.find_element(By.XPATH, '//*[@id="Data_table"]/table/thead/tr').text.split('\n')
    dictionar = {i: [] for i in header}
    for j in range(len(header)):
        for i in range(len(header) + int(j), len(lista), len(header)):
            dictionar[header[j]].append(lista[i])
    print(dictionar)

    df = pd.DataFrame(dictionar)
    # noinspection PyTypeChecker
    df.to_csv(path_or_buf=f"BNR{os.sep}BNR_ALL_DATA.csv")

    browser.close()
