from selenium import webdriver
from time import sleep
from config import *



url = "https://www.heroeswm.ru/home.php"
driver = webdriver.Chrome(executable_path=webdriver_path)


try:
    driver.get(url=url)
    sleep(5)
except Exception as _ex:
    print(f'[Error!] {_ex}')
finally:
    driver.close()
    driver.quit()