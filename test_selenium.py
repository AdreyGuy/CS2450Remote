from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = Options()

options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--remote-debugging-port=9222") 

# THE FIX: Tell Windows Chrome to use a Windows folder, not a Linux /tmp/ folder
# Using a raw string (r"") so Python reads the backslashes correctly
options.add_argument(r"--user-data-dir=C:\Temp\SeleniumProfile")

# Note: Make sure your chromedriver path here ends in .exe!
driver = webdriver.Chrome(
    executable_path="/mnt/c/Users/batru/bin/chromedriver.exe", 
    options=options
)

driver.get("https://isitchristmas.com")

answer = driver.find_element(By.ID, "answer")

print("Page title:", driver.title)
print("Answer text:", answer.text)

driver.quit()
