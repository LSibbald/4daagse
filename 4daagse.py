from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
import time
import winsound

options = Options()
options.use_chromium = True
edge_driver_path = r"C:\Users\lsibbald\msedgedriver.exe"
service = Service(executable_path=edge_driver_path)
driver = webdriver.Edge(service=service, options=options)

url = "https://atleta.cc/e/zRLhVgiDSdOK/resale"

try:
    while True:
        driver.get(url)
        time.sleep(5)  # Allow time for the page to fully load
        
        page_source = driver.page_source
        if "Burger individueel" in page_source and "Ticket kopen" in page_source:
            print("Tickets are available!")
            winsound.Beep(440, 2000)  # Play a beep sound for 2000 milliseconds (2 seconds)
            break  # Exit the loop if both conditions are met
        else:
            print("Tickets are not available at the moment. Checking again...")
            time.sleep(15)  # Wait for 15sec before rechecking
except KeyboardInterrupt:
    print("Script stopped by user.")
finally:
    driver.quit()
