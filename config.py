# Path to webdriver
webdriver_path = "./chromedriver/driver"

# key - ID; value - user-agent_pattern
# [Insert your values]
user_agents = {"ID": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36"}

# URLs
urls = {"main": "https://www.heroeswm.ru", "login": "https://www.heroeswm.ru/login.php", "map": "https://www.heroeswm.ru/map.php"}

# key - Nickname; values - ID
# [Insert your values]
account_ID = {"Nickname": "ID"}

# login and password
# [Insert your values]
data = {"ID": {"login": "your_nickname", "password": "your_password"}}

# the current location of the character on the map (what area?)
# [Insert your values]
# Example: For district "Rogues' Wood" value - "cx=51&cy=49" 
current_district = "cx=51&cy=49"

# structure of enterprises to work
structures = ["sh", "fc", "mn"]