from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import time
import winsound  # Import the winsound module

options = Options()
options.use_chromium = True
edge_driver_path = r"C:\Users\lsibbald\msedgedriver.exe"
service = Service(executable_path=edge_driver_path)
driver = webdriver.Edge(service=service, options=options)

url = "https://atleta.cc/e/zRLhVgiDSdOK/resale"

try:
    driver.get(url)
    time.sleep(5)  # Allow time for the page to fully load
    while True:
        # Search for "Ticket kopen" button or link
        try:
            ticket_kopen_element = driver.find_element(By.XPATH, "//*[self::a or self::button][contains(., 'Ticket kopen')]")
            print("Tickets are available!")
            ticket_kopen_element.click()
            winsound.Beep(440, 2000)  # Play a beep sound for 2000 milliseconds (2 seconds)
            break  # Exit the loop after clicking the "Ticket kopen" element
        except NoSuchElementException:
            print("Tickets are not available at the moment. Checking again...")
            time.sleep(15)  # Wait for 15 seconds before rechecking
            driver.refresh()  # Refresh the page for the next check
        except ElementClickInterceptedException:
            print("The 'Ticket kopen' element was found but not clickable. It might be obscured by another element.")
            time.sleep(60)  # Wait for a bit before trying to click again

except KeyboardInterrupt:
    print("Script stopped by user.")
finally:
    driver.quit()
