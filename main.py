from typing import Union
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from config import *



# Account autorization
def autorization() -> None:
    print(">> Autorization... ")
    autorization_process()
    sleep(1)
    
    if driver.current_url == urls["login"]:
        autorization_process(flag=True)


# Autorization function: if you need to enter captcha or without. flag = True -> captcha present, else -> no captcha
def autorization_process(flag=False) -> None: 
    try:
        if flag == False:
            driver.get(url=urls["main"])
            login = driver.find_element(By.CLASS_NAME, "inp_login")
            login.clear()
            login.send_keys(data["ID"]["login"])
            sleep(1)

            password = driver.find_element(By.CLASS_NAME, "inp_pass")
            password.clear()
            password.send_keys(data["ID"]["password"])
            sleep(1)

            log_in = driver.find_element(By.CLASS_NAME, "entergame")
            log_in.click()
        else:
            login = driver.find_element(By.XPATH, "/html/body/center/table/tbody/tr/td/table/tbody/tr/td/form/table/tbody/tr[1]/td[2]/input")
            login.clear()
            login.send_keys(data["ID"]["login"])
            sleep(1)

            password = driver.find_element(By.XPATH, "/html/body/center/table/tbody/tr/td/table/tbody/tr/td/form/table/tbody/tr[2]/td[2]/input")
            password.clear()
            password.send_keys(data["ID"]["password"])
            sleep(1)

            # EDIT
            # captcha = driver.find_element(By.XPATH, "/html/body/center/table/tbody/tr/td/table/tbody/tr/td/form/table/tbody/tr[4]/td/table/tbody/tr/td[1]/img")
            # code = captcha_solution(src_link=, flag=True)
            # sleep(5)

            # input_code_form = driver.find_element(By.XPATH, "/html/body/center/table/tbody/tr/td/table/tbody/tr/td/form/table/tbody/tr[4]/td/table/tbody/tr/td[2]/input")
            # input_code_form.send_keys(code)
            # sleep(5)

            log_in = driver.find_element(By.XPATH, "/html/body/center/table/tbody/tr/td/table/tbody/tr/td/form/table/tbody/tr[5]/td/input[1]")
            log_in.click()
            
        print(">> [Successful authorization!]")
    except Exception as _ex:
        print(">> [Autorization error]: {_ex}")


# Captcha solution: flag = True -> captcha present, else -> there is only a button
def captcha_solution(src_link=None, flag=True) -> Union[str, None]:
    if flag == True:
        pass
    else:
        try:
            getjob = driver.find_element(By.XPATH, '//*[@id="wbtn"]')
            getjob.click()
        except:
            print("[Are you employed]")


# character employment
def employ() -> None:
    print(">> Employment... ")

    driver.get(url=urls["map"]) 
    current_district = determination_current_district()

    for structure in structures:
        url = urls["map"] + "?" + current_district + "&st=" + structure
        driver.get(url)
        try:
            concern_link = driver.find_element(By.LINK_TEXT, "»»»")
            concern_link.click()
            # check: is there a captcha?
            # EDIT
            captcha_solution(flag=False) 
            print(">> [Successful employment!]")

            if "object-info" in driver.current_url:
                break
        except Exception as _ex:
            print("[No free work]")


# Defines a unique coordinate for a character based on its location
def determination_current_district() -> str:
    district_name = driver.find_element(By.XPATH, '//*[@id="set_mobile_max_width"]/div[1]/b').text 
    return districts[district_name]


def main() -> None:
    try:
        autorization()
        sleep(5)
        employ()
    except Exception as _ex:
        print(f'[Error!] {_ex}')
    finally:
        driver.close()
        driver.quit()


if __name__ == "__main__":
    # options
    options = webdriver.ChromeOptions()
    options.add_argument(f"user-agent={user_agents['ID']}")

    driver = webdriver.Chrome(
        executable_path=webdriver_path, 
        options=options
        )
        
    main()
