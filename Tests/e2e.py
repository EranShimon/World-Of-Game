import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_scores_service(url):
    try:
        driver = webdriver.Chrome()
        driver.get(url)
        score_element = driver.find_element(By.ID, "score")
        score = int(score_element.text)
        driver.quit()
        return 1 <= score <= 1000
    except Exception as e:
        print(f"Test failed: {e}")
        return False

def main_function():
    url = 'http://localhost:8777/score'
    result = test_scores_service(url)
    return 0 if result else -1