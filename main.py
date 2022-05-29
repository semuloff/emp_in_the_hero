from selenium import webdriver
from time import sleep
from config import *



# options
options = webdriver.ChromeOptions()
options.add_argument(f"user-agent={user_agents['ID']}")

driver = webdriver.Chrome(
    executable_path=webdriver_path, 
    options=options
    )


try:
    driver.get(url=url)
    sleep(5)
except Exception as _ex:
    print(f'[Error!] {_ex}')
finally:
    driver.close()
    driver.quit()