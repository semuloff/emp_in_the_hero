from selenium import webdriver
from time import sleep
from config import *



def main():
    try:
        authorization()
        sleep(5)
        employ()
    except Exception as _ex:
        print(f'[Error!] {_ex}')
    finally:
        driver.close()
        driver.quit()


# account authorization
def authorization():
    driver.get(url=urls["main"])
    
    try:
        login = driver.find_element_by_class_name("inp_login")
        login.clear()
        login.send_keys(data["ID"]["login"])

        password = driver.find_element_by_class_name("inp_pass")
        password.clear()
        password.send_keys(data["ID"]["password"])

        log_in = driver.find_element_by_class_name("entergame")
        log_in.click()
    except Exception as _ex:
        print("[Authorization error]")

# character employment
def employ():
    driver.get(url=urls["map"])
 
    for structure in structures:
        url = urls["map"] + "?" + current_district + "&st=" + structure
        driver.get(url)

        try:
            concern_link = driver.find_element_by_link_text("»»»")
            concern_link.click()

            captcha_solution()

            if "object-info" in driver.current_url:
                break
        except Exception as _ex:
            print(f"[Mistake in employment] {_ex}")
 
    print("[Done!]")        


def captcha_solution():
    try:
        getjob = driver.find_element_by_xpath('//*[@id="wbtn"]')
        getjob.click()
    except Exception as _ex:
        print("[Can't find button]")


if __name__ == "__main__":
    # options
    options = webdriver.ChromeOptions()
    options.add_argument(f"user-agent={user_agents['ID']}")

    driver = webdriver.Chrome(
        executable_path=webdriver_path, 
        options=options
        )

    main()
