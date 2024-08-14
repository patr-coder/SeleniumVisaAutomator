from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

# Set up Chrome options to ignore certificate errors and disable notifications
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")

# Set up Chrome with Service object
service = Service(executable_path="/Users/Patrick/chromedriver/chromedriver")
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Navigate to the website
    driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
    driver.maximize_window()
    time.sleep(2)

    # Click Buy Ticket
    driver.find_element(By.XPATH, "//a[contains(text(),'Buy Ticket')]").click()

    # Choose Ticket Price
    driver.find_element(By.XPATH, "(//input[@id='product_549'])[1]").click()

    # Enter Identity Details
    driver.find_element(By.XPATH, "//input[@id='travname']").send_keys("Kato")
    driver.find_element(By.XPATH, "(//input[@id='travlastname'])[1]").send_keys("PM")
    driver.find_element(By.XPATH, "//textarea[@id='order_comments']").send_keys(
        "Special Billet"
    )

    # Enter Date of Birth
    driver.find_element(By.XPATH, "//input[@id='dob']").click()
    Select(
        driver.find_element(By.XPATH, "//select[@aria-label='Select month']")
    ).select_by_visible_text("Feb")
    Select(
        driver.find_element(By.XPATH, "//select[@aria-label='Select year']")
    ).select_by_visible_text("2000")

    # Select Date
    for date in driver.find_elements(
        By.XPATH, "//table[@class='ui-datepicker-calendar']/tbody/tr/td/a"
    ):
        if date.text == "18":
            date.click()
            break

    # Select Sex
    driver.find_element(By.XPATH, "//label[@for='sex_1']").click()
    time.sleep(2)

    # Add More Passengers
    driver.find_element(By.XPATH, "//input[@id='addmorepax']").click()
    time.sleep(2)

    # Select Traveler Type
    driver.find_element(By.XPATH, "(//span[@role='combobox'])[1]").click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, '//li[contains(text(), "I\'m the only traveler")]')
        )
    ).click()

    # Select Type of Trip
    driver.find_element(By.XPATH, "(//input[@name='traveltype'])[2]").click()

    # Enter Destination
    driver.find_element(
        By.XPATH, "//span[@class='woocommerce-input-wrapper']/input[@id='fromcity']"
    ).send_keys("TOKYO")
    driver.find_element(By.XPATH, "//input[@id='tocity']").send_keys("KINSHASA")
    time.sleep(2)

    # Enter Date of Departure
    driver.find_element(By.XPATH, "//input[@id='departon']").click()
    Select(
        driver.find_element(By.XPATH, "//select[@aria-label='Select month']")
    ).select_by_visible_text("Sep")
    Select(
        driver.find_element(By.XPATH, "//select[@aria-label='Select year']")
    ).select_by_visible_text("2024")

    for date in driver.find_elements(
        By.XPATH, "//table[@class='ui-datepicker-calendar']/tbody/tr/td/a"
    ):
        if date.text == "1":
            date.click()
            break

    # Enter Date of Return
    driver.find_element(By.XPATH, "//input[@id='returndate']").click()
    Select(
        driver.find_element(By.XPATH, "//select[@aria-label='Select month']")
    ).select_by_visible_text("Oct")
    Select(
        driver.find_element(By.XPATH, "//select[@aria-label='Select year']")
    ).select_by_visible_text("2024")

    for date in driver.find_elements(
        By.XPATH, "//table[@class='ui-datepicker-calendar']/tbody/tr/td/a"
    ):
        if date.text == "30":
            date.click()
            break

    # Add Additional Options
    driver.find_element(By.XPATH, "(//textarea[@id='notes'])[1]").send_keys(
        "I forgot to choose a seat and a green card."
    )

    # Select Visa Option
    driver.find_element(By.XPATH, "//span[text()='Visa application']").click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//li[contains(text(), 'Visa extension')]")
        )
    ).click()
    time.sleep(2)

    # Enter Contact Information
    driver.find_element(By.XPATH, "(//input[@id='deliverymethod_3'])[1]").click()
    driver.find_element(By.XPATH, "//input[@id='billname']").send_keys(
        "Kato PM  PATRICK"
    )
    driver.find_element(By.XPATH, "(//input[@id='billing_phone'])[1]").send_keys(
        "09070002222"
    )
    driver.find_element(By.XPATH, "(//input[@id='billing_email'])[1]").send_keys(
        "kato@roboco-op.org"
    )
    time.sleep(2)

    # Select Country
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "select2-billing_country-container"))
    ).click()
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "select2-billing_country-results"))
    )
    driver.find_element(By.XPATH, "//li[text()='Japan']").click()

    # Enter Postal Code
    driver.find_element(By.XPATH, "//*[@id='billing_postcode']").send_keys("1735026")
    time.sleep(2)

    # Select Prefecture
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "select2-billing_state-container"))
    ).click()
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "select2-billing_state-results"))
    )
    driver.find_element(By.XPATH, "//li[text()='Tokyo']").click()

    # Enter Address
    driver.find_element(By.XPATH, "//input[@id='billing_city']").send_keys("City")
    driver.find_element(By.XPATH, "//input[@id='billing_address_1']").send_keys(
        "City-KU Pays 29-8 MASON"
    )
    driver.find_element(By.XPATH, "//input[@id='billing_address_2']").send_keys(
        "Bldg 304"
    )
    driver.find_element(By.XPATH, "//textarea[@id='order_comments']").send_keys(
        "Please note that this is for people who are not working in the house and will be out of town for the weekend."
    )
    time.sleep(5)

finally:
    driver.quit()  # Ensure the browser is closed properly
