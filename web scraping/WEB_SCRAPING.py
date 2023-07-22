import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get("https://www.linkedin.com/jobs/view/3660532900/")
driver.maximize_window()

poster_name_element = driver.find_element(By.CSS_SELECTOR, "div.message-the-recruiter h3")
driver.find_element(By.CSS_SELECTOR, 'div.description__text button.show-more-less-button[aria-expanded="false"]').click()
time.sleep(2)
about_job_element = driver.find_element(By.CSS_SELECTOR, "div.description__text section div").text

poster_name = poster_name_element.text

print("Job Poster's Name:", poster_name)
print("About the Job:")
print(about_job_element)
