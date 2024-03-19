from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import winsound

options = Options()
options.use_chromium = True
edge_driver_path = r"C:\Users\lsibbald\msedgedriver.exe"
service = Service(executable_path=edge_driver_path)
driver = webdriver.Edge(service=service, options=options)
wait = WebDriverWait(driver, 10)  # Adjust timeout as needed

url = "https://atleta.cc/e/zRLhVgiDSdOK/resale"
driver.get(url)

try:
    # Wait for the page elements to load without using time.sleep()
    wait.until(EC.presence_of_element_located((By.XPATH, "//body")))

    while True:
        try:
            # Use WebDriverWait to wait for the "Ticket kopen" element to be clickable
            ticket_kopen_element = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[self::a or self::button][contains(., 'Ticket kopen')]")))
            print("Tickets are available!")
            ticket_kopen_element.click()
            winsound.Beep(440, 2000)  # Alert the user
            # Break out of the loop after successfully clicking the button
            # The script ends here, but the browser remains open for manual inspection or further actions
            break
        except TimeoutException:
            print("Tickets are not available at the moment. Checking again...")
            driver.refresh()  # Consider the frequency of refresh to avoid being blocked by the website
            wait.until(EC.presence_of_element_located((By.XPATH, "//body")))  # Wait for the page to load again

except KeyboardInterrupt:
    print("Script stopped by user.")
# Removed the finally block to prevent closing the WebDriver automatically
