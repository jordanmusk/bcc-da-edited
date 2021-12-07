from os.path import isfile, join
from os import listdir
import datetime
import time
import csv

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os

# -------------- START THE BOT WORKING -------------- #
options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-sandbox")
options.add_argument("--start-maximized")
options.add_argument("download.default_directory=C:/Documents/gaala")
driver = webdriver.Chrome("chromedriver.exe", options=options)
number = 0

driver.get('https://developmenti.brisbane.qld.gov.au/Home/MapSearch')  # go to the website


def find_element_click(location_of_the_element):
    """
    :param location_of_the_element: XPATH of te any web element.
    :return: Find element until it present on webpage and click on it.
    """
    while True:
        try:
            driver.find_element(By.XPATH, location_of_the_element).click()
            break
        except:
            pass


# ------------------------------------------ #
# ---------> SETTING UP FILTERS <----------- #
total_data = []
add = 0
while True:
    start_date = "01/01/2020"
    date_1 = datetime.datetime.strptime(start_date, "%d/%m/%Y")
    pre_date = str(date_1 + datetime.timedelta(days=number + add)).split(" ")[0].replace("-", "/")
    pre_date_end = str(date_1 + datetime.timedelta(days=number + 5)).split(" ")[0].replace("-", "/")

    if add == 0:
        add += 1
    exact_start_date = datetime.datetime.strptime(pre_date, "%Y/%m/%d").date().strftime("%d/%m/%Y")
    exact_end_date = datetime.datetime.strptime(pre_date_end, "%Y/%m/%d").date().strftime("%d/%m/%Y")
    find_element_click("//h2[@class='mobile-filters']")  # Show navigation bar to filter out
    find_element_click("(//select[@class='form-control active'])[1]")  # click on options
    find_element_click("(//option)[4]")  # select ALL from options
    find_element_click("//p[@id='show-daterange']")  # select date range
    find_element_click("//input[@id='dateRangeInput']")  # input date click
    start_from = driver.find_element(By.XPATH, "//input[@class='input-mini form-control active']")
    start_from.clear()
    start_from.send_keys(exact_start_date)
    end_date = driver.find_element(By.XPATH, "//input[@class='input-mini form-control']")
    end_date.clear()
    end_date.send_keys(exact_end_date)
    find_element_click("//button[@class='applyBtn btn btn-sm btn-success']")
    find_element_click("//h2[@class='mobile-filters']")  # close filter option
    if exact_start_date != "07/12/2021":
        time.sleep(5)
        try:
            data = driver.find_element(By.XPATH, '//span[@class="application-count"]').text
            data = int(str(data).split(" ")[0])
            total_data.append(data)
            print(f"CSV TOTAL CELLS ---> {data}")
        except:
            pass
        try:
            driver.find_element('//div/select[@class="form-control"]').clear()
            driver.find_element('//div/select[@class="form-control"]/option[2]').click()
        except:
            pass

        time.sleep(5)
        print(f"{exact_start_date}: ------> Start date")
        print(f"{exact_end_date}: ------> End date")
        find_element_click('(//i[@class="fa fa-download"])[1]')

        number += 5
        print(sum(total_data))
        if exact_start_date == "07/12/2021":
            break
