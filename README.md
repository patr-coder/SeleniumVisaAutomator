
# SeleniumVisaAutomator

## Overview

**SeleniumVisaAutomator** (also referred to as **SeleniumTravelBot**) is an automation script written in Python using Selenium. It is designed to streamline the process of filling out and submitting travel-related forms on the web, including tasks like entering personal details, selecting travel dates, and choosing visa options. This tool helps reduce manual input and minimizes potential errors during the form submission process.

## Features

- **Automated Form Filling**: Automatically inputs personal information such as name, date of birth, and contact details.
- **Date Selection**: Efficiently selects travel dates, including departure and return.
- **Dropdown Handling**: Manages dropdown selections for options like traveler type, visa type, country, and prefecture.
- **Error Handling**: Ensures that the browser closes properly in case of any errors during execution.

## Prerequisites

Before running the script, ensure you have the following installed:

- [Python 3.x](https://www.python.org/downloads/)
- [Selenium WebDriver](https://pypi.org/project/selenium/)
- [Google Chrome](https://www.google.com/chrome/) (or another supported browser)
- [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) (Ensure the version matches your Chrome browser)
- [PyCharm Community Edition](https://www.jetbrains.com/pycharm/download/) (Optional but recommended for editing and running Python scripts)

## Installation

1. **Clone the Repository**

   ```bash
   git clone git@github.com/patr-coder/SeleniumVisaAutomator.git
   cd SeleniumVisaAutomator
2. **Install Required Python Packages**

     Use pip to install Selenium:

   ```bash
   pip install selenium
   
3. **Download ChromeDriver** 

   Ensure [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) is downloaded and installed. 

   Make sure the version matches your installed version of [Google Chrome](https://www.google.com/chrome/).

   After downloading, place the chromedriver executable in a known directory 
   and update `the executable_path` in the script to point to this location:
 
   ````bash
   service = Service(executable_path="/path/to/your/chromedriver")
   
4. **Run the Script**

   Execute the script by running:

   ````bash
   python ticket.py
5. **Watch the Automation**

   The script will open a Chrome browser window
   and begin automating the form submission process on the specified website.

6. **Code Overview  Selenium Script**

   The following Python script demonstrates how to use Selenium with ChromeDriver to automate form submission on a travel-related website. This script sets up Chrome to ignore certificate errors and disable notifications, navigates to the website, and fills out the form.

  ```python
from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

# Set up Chrome options to ignore certificate errors and disable notifications
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--disable-blink-features=AutomationControlled')

# Set up Chrome with Service object
service = Service(executable_path="/path/to/your/chromedriver")
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Navigate to the website and perform form filling
    driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
    driver.maximize_window()
    time.sleep(2)
    # Complete code as mentioned above...

finally:
    driver.quit()  # Ensure the browser is closed properly


 ```
7. **Troubleshooting**
   Browser Not Opening: Ensure that the ChromeDriver version matches your installed version of Chrome. Incompatible versions can prevent the browser from launching.
  Timeout Errors: If you encounter timeout errors, consider increasing the wait times using WebDriverWait, especially if your internet connection is slow or the website you are automating is unresponsive.

8. **Contributing:**

   Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes. Your contributions help improve the project and ensure its ongoing success.

9. **License:**
  This project is licensed under the MIT License - see the LICENSE file for details.

  ````bash
  
    This structure provides a clear and organized `README.md` file with all necessary sections:

    - **Code Overview**: Details and code explanation.
    - **Troubleshooting**: Tips for resolving common issues.
    - **Contributing**: Information on how others can contribute to the project.
    - **License**: Specifies the license under which the project is distributed. 

    Each section is numbered sequentially, making it easy for users to navigate through the document.
    

  









