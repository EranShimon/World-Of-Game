import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement

url = "http://127.0.0.1:5000"

def test_scores_service(url):
    try:
        # Set up Chrome WebDriver
        driver = webdriver.Chrome()
        # Open the URL in the browser
        driver.get(url)
        # Wait for the score container to be present
        wait = WebDriverWait(driver, 10)
        score_container: WebElement = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "score-container")))
        score_element: WebElement = score_container.find_element(By.CLASS_NAME, "score-value")
        # Get the text of the score element
        score_text = score_element.text
        # Check if the score is a number between 1 and 1000
        if score_text.isdigit() and 1 <= int(score_text) <= 1000:
            return True
        else:
            return False

    except Exception as e:
        print(f"Error occurred: {e}")
        return False

    finally:
        # Close the WebDriver
        driver.quit()

def main_function():
    # Perform tests on the Flask service
    if test_scores_service(url):
        return 0 # Tests passed
    else:
        return -1 # Tests failed

if __name__ == "__main__":
    sys.exit(main_function())
