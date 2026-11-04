from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

try:
    # Open the local login page
    file_path = Path("login.html").resolve().as_uri()
    driver.get(file_path)

    # Test valid login
    driver.find_element(By.ID, "username").send_keys("student")
    driver.find_element(By.ID, "password").send_keys("student123")

    driver.find_element(
        By.CSS_SELECTOR,
        "button[type='submit']"
    ).click()

    wait.until(
        EC.text_to_be_present_in_element(
            (By.ID, "message"),
            "Login successful"
        )
    )

    print("Valid login test passed")

    # Clear the fields
    driver.find_element(By.ID, "username").clear()
    driver.find_element(By.ID, "password").clear()

    # Test invalid login
    driver.find_element(By.ID, "username").send_keys("wrong")
    driver.find_element(By.ID, "password").send_keys("wrong")

    driver.find_element(
        By.CSS_SELECTOR,
        "button[type='submit']"
    ).click()

    wait.until(
        EC.text_to_be_present_in_element(
            (By.ID, "message"),
            "Invalid username or password"
        )
    )

    print("Invalid login test passed")

finally:
    driver.quit()