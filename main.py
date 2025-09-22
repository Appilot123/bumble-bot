from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up the Chrome WebDriver
driver = webdriver.Chrome(executable_path='/path/to/chromedriver')

def login_bumble():
    driver.get("https://bumble.com")
    time.sleep(2)
    
    # Login steps
    # Adjust based on how the login process works (Google login, Facebook, etc.)
    login_button = driver.find_element(By.XPATH, '//*[@id="login-button"]')  # Change this as per actual button
    login_button.click()
    
    # Wait for manual login or automate the login (e.g., using Google/Facebook login)
    print("Please log in to your Bumble account manually!")
    time.sleep(10)  # Wait for the user to login

def swipe_right():
    time.sleep(2)
    
    # Find the swipe right button (this might change depending on your interface)
    right_swipe_button = driver.find_element(By.XPATH, '//*[@id="swipe-right-button"]')  # Change XPath
    right_swipe_button.click()
    print("Swiped Right!")
    
def send_message():
    time.sleep(3)
    
    # Example: Find a match and send a message
    message_button = driver.find_element(By.XPATH, '//*[@id="message-button"]')  # Change XPath
    message_button.click()
    
    message_box = driver.find_element(By.XPATH, '//*[@id="message-input"]')  # Change XPath
    message_box.send_keys("Hey! How's it going?")
    message_box.send_keys(Keys.RETURN)  # Send message
    print("Message Sent!")

def main():
    login_bumble()
    
    # Automate swiping and messaging loop
    while True:
        swipe_right()
        send_message()
        time.sleep(5)  # Pause between swipes/messages

if __name__ == "__main__":
    main()
