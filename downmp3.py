from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import selenium.webdriver as wb
import time
from bs4 import BeautifulSoup
def down(url):
    chrome_driver = r'./chromedriver.exe'
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = wb.Chrome(service=Service(chrome_driver), options=options)
    driver.get(url)

    # 获取网页的HTML文本
    time.sleep(0.1)
    html_text = driver.page_source
    ss = BeautifulSoup(html_text,'html.parser')
    try:
        down_url = ss.find('source')['src']
    except:
        print("下载地址不存在")
        return
    # print(down_url)
    return down_url