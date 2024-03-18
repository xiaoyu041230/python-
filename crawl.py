import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

def get_exchange_rate(date,currency_code):
    #匹配货币英文代码和货币类型在货币列表中的位置
    currency_mapping = {
        "NULL": 0, "GBP": 1, "HKD": 2, "USD": 3, "CHF": 4, "DEM": 5, "FRF": 6, "SGD": 7, "SEK": 8,
        "DKK": 9, "NOK": 10, "JPY": 11, "CAD": 12, "AUD": 13, "EUR": 14, "MOP": 15, "PHP": 16, "THP": 17,
        "NZD": 18, "ISO": 19, "SUR": 20, "MYR": 21, "NYD": 22, "ESP": 23, "ITL": 24, "NLG": 25, "BEF": 26,
        "FIM": 27, "INR": 28, "IDR": 29, "BRC": 30, "ISO": 31, "INR2": 32, "ZAR": 33, "SAR": 34, "TRL": 35,
    }

    #检查日期的有效性
    try:
        datetime.datetime.strptime(date, '%Y%m%d')
    except ValueError:
        print("Invalid date")
        return

    #检查货币代码是否存在于currency_mapping字典中
    if currency_code not in currency_mapping:
        print("Code does not exist")
        return

    #获取到中国银行网页
    driver = webdriver.Chrome()

    try:
        driver.get("https://www.boc.cn/sourcedb/whpj/")

        #填入开始日期
        search_start = driver.find_element(By.ID,"erectDate")
        search_start.clear()
        search_start.send_keys(date)

        #填入结束日期
        search_end = driver.find_element(By.ID,"nothing")
        search_end.clear()
        search_end.send_keys(date)

        #选择货币类型
        search_currency = driver.find_element(By.ID,"pjname")
        select_currency = Select(search_currency)
        select_currency.select_by_index(currency_mapping[currency_code])

        #等待页面加载
        time.sleep(1)

        #点击搜索按钮
        search_button = driver.find_element(By.XPATH,'//input[@onclick="executeSearch()"]')
        search_button.click()

        #提取表格中第一个现汇卖出价
        get_price = driver.find_element(By.XPATH,'//tr[2]/td[4]')

        #将现汇卖出价写入result.txt中
        with open("result.txt", "w", encoding="utf-8") as file:
            file.write(get_price.text)

    finally:
        #关闭浏览器
        driver.quit()

if __name__ == "__main__":
    #获取用户输入的日期
    date = input("Enter date (YYYYMMDD): ")
    #获取用户输入的货币英文代码
    currency_code = input("Enter currency code: ")

    #获取现汇卖出价
    exchange_rate = get_exchange_rate(date, currency_code)
