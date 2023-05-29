import os
from selenium import webdriver
from selenium.webdriver.common.by import By


html_file_path = "L:\SEM-6\SE project\index.html"
if not os.path.exists(html_file_path):
    print("HTML file does not exist!")
    exit(1)

try:
    driver = webdriver.Chrome()
    driver.get("file://" + os.path.abspath(html_file_path))
    print("HTML file opened successfully")
except Exception as e:
    print("Failed to open HTML file:", str(e))
finally:
    driver.quit()

try:
    driver = webdriver.Chrome()
    driver.get("file://" + os.path.abspath(html_file_path))
    login_link = driver.find_element(By.CSS_SELECTOR,"a[href='login.html']")
    login_link.click()
    print("Login page opened successfully")
except Exception as e:
    print("Failed to open Login page:", str(e))
finally:
    driver.quit()

try:
    driver = webdriver.Chrome()
    driver.get("file://" + os.path.abspath(html_file_path))
    register_link = driver.find_element(By.CSS_SELECTOR,"a[href='register.html']")
    register_link.click()
    print("Register page opened successfully")
except Exception as e:
    print("Failed to open Register page:", str(e))
finally:
    driver.quit()
