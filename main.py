from selenium import webdriver
from time import sleep
from config import *



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


def detect_captcha() -> str:
    pass


# Autorization function: if you need to enter captcha or without. flag = False -> without captcha, else -> with
def autorization_process(flag=False) -> None: 
    try:
        if flag == False:
            driver.get(url=urls["main"])
            login = driver.find_element_by_class_name("inp_login")
            login.clear()
            login.send_keys(data["ID"]["login"])
            sleep(5)

            password = driver.find_element_by_class_name("inp_pass")
            password.clear()
            password.send_keys(data["ID"]["password"])
            sleep(5)

            log_in = driver.find_element_by_class_name("entergame")
            log_in.click()
        else:
            login = driver.find_element_by_xpath("/html/body/center/table/tbody/tr/td/table/tbody/tr/td/form/table/tbody/tr[1]/td[2]/input")
            login.clear()
            login.send_keys(data["ID"]["login"])
            sleep(5)

            password = driver.find_element_by_xpath("/html/body/center/table/tbody/tr/td/table/tbody/tr/td/form/table/tbody/tr[2]/td[2]/input")
            password.clear()
            password.send_keys(data["ID"]["password"])
            sleep(20)

            # captcha = driver.find_element_by_xpath("/html/body/center/table/tbody/tr/td/table/tbody/tr/td/form/table/tbody/tr[4]/td/table/tbody/tr/td[1]/img")
            # code = detect_captcha(captcha)
            # sleep(5)

            # input_code_form = driver.find_element_by_xpath("/html/body/center/table/tbody/tr/td/table/tbody/tr/td/form/table/tbody/tr[4]/td/table/tbody/tr/td[2]/input")
            # input_code_form.send_keys(code)
            # sleep(5)

            log_in = driver.find_element_by_xpath("/html/body/center/table/tbody/tr/td/table/tbody/tr/td/form/table/tbody/tr[5]/td/input[1]")
            log_in.click()
            
            print("[Done]")
    except Exception as _ex:
        print("[Autorization error]")


# Account autorization
def autorization() -> None:
    print(">> Autorization... ")
    autorization_process()
    sleep(5)
    if driver.current_url == urls["login"]:
        autorization_process(flag=True)


# character employment
def employ() -> None:
    print(">> Employment... ") 
    driver.get(url=urls["map"])
 
    for structure in structures:
        url = urls["map"] + "?" + current_district + "&st=" + structure
        driver.get(url)

        try:
            concern_link = driver.find_element_by_link_text("»»»")
            concern_link.click()

            captcha_solution()
            
            print("[Done!]")

            if "object-info" in driver.current_url:
                break
        except Exception as _ex:
            print(f"[Mistake in employment] {_ex}")
 
           


# temporary function
def captcha_solution() -> None:
    try:
        getjob = driver.find_element_by_xpath('//*[@id="wbtn"]')
        getjob.click()
    except Exception as _ex:
        print("[You are employed]")


if __name__ == "__main__":
    # options
    options = webdriver.ChromeOptions()
    options.add_argument(f"user-agent={user_agents['ID']}")

    driver = webdriver.Chrome(
        executable_path=webdriver_path, 
        options=options
        )
        
    main()
