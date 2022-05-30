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
data = {"ID": {"login": "<your_nickname>", "password": "<your_password>"}}

# The game has a unique coordinate for each area.
districts = {
    "Ungovernable Steppe": "cx=48&cy=48", 
    "Eagle Nest": "cx=49&cy=48", 
    "Peaceful Camp": "cx=50&cy=48",
    "Crystal Garden": "cx=51&cy=48",
    "Fairy Trees": "cx=52&cy=48",
    "Sunny City": "cx=48&cy=49",
    "Shining Spring": "cx=49&cy=49",
    "Tiger Lake": "cx=50&cy=49",
    "Rogues' Wood": "cx=51&cy=49",
    "Bear Mountain": "cx=52&cy=49",
    "Mithril Coast": "cx=53&cy=49",
    "Sublime Arbor": "cx=48&cy=50",
    "Green Wood": "cx=49&cy=50",
    "Empire Capital": "cx=50&cy=50",
    "East River": "cx=51&cy=50",
    "Magma Mines": "cx=52&cy=50",
    "Harbour City": "cx=53&cy=50",
    "Lizard Lowland": "cx=49&cy=51",
    "Wolf Dale": "cx=50&cy=51",
    "Dragons' Caves": "cx=51&cy=51",
    "The Wilderness": "cx=49&cy=52",
    "Portal Ruins": "cx=50&cy=52",
    "Great Wall": "cx=51&cy=52",
    "Titans' Valley": "cx=51&cy=53",
    "Fishing Village": "cx=52&cy=53",
    "Kingdom Castle": "cx=52&cy=54"
    }

# structure of enterprises to work
structures = ["sh", "fc", "mn"]