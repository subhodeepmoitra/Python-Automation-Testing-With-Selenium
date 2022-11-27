from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import time




##################### testing first product ###############################
def first_product():
    driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[1]/a/div").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click() #buy now
    driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[1]/div[3]/a").click() #move to cart
    driver.find_element(By.ID, "checkout").click() #check out
    # delevery details
    first_name = driver.find_element(By.ID, "first-name")
    first_name.send_keys("Tester1") #enter first name
    last_name = driver.find_element(By.ID, "last-name")
    last_name.send_keys("Tester1 Surname") #enter last name
    zip_code = driver.find_element(By.ID, "postal-code")
    zip_code.send_keys("712589") #enter zip code
    driver.find_element(By.ID, "continue").click() #click on continue button
    driver.execute_script("window.scrollTo(0, 1000)")
    driver.find_element(By.ID, "finish").click() #finishing one order
    driver.execute_script("window.scrollTo(0,1000)")
    driver.find_element(By.ID,"back-to-products").click()
    print("Back to Home Page...")
    ############################ one order completed ######################################
    ############################### home page top left drop down #########################################
    driver.find_element(By.ID, "react-burger-menu-btn").click() #click on menu bar
    driver.find_element(By.ID, "about_sidebar_link").click() #click on about bar
    driver.execute_script("window.scrollTo(0,1000)")
    # time.sleep(20)
    # driver.find_element(By.ID, "onetrust-accept-btn-handler").click()
    # time.sleep(20)
    # driver.find_element(By.XPATH, "/html/body/div/main/div[2]/div/button/svg/path").click()
    # time.sleep(20)
    driver.back()
    time.sleep(3)
    # driver.close()
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> First Product Buying Seccessful... <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")


########################## testing another product #################################
def second_product():
    driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/div/div/div[2]/div[2]/div[1]/a/div").click()
    driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/div/div[2]/button").click()
    driver.find_element(By. XPATH, "/html/body/div/div/div/div[1]/div[1]/div[3]/a").click
    driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[1]/div[3]/a").click()
    driver.find_element(By.ID, "checkout").click()
    
    fname = driver.find_element(By.ID, "first-name")
    fname.send_keys("Tester 1")
    lname = driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/form/div[1]/div[2]/input")
    lname.send_keys("Tester 1 last name")
    zcode = driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/form/div[1]/div[3]/input")
    zcode.send_keys("712581")
    driver.find_element(By.ID, "continue").click()


    driver.execute_script("window.scrollTo(0,1000)")
    driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/div[2]/div[8]/button[2]").click()
    

    driver.find_element(By.ID, "back-to-products").click()
    print("Back to home...")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>> Second product buying successful... <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")






start = time.ctime()
options = Options()
options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"
driver = webdriver.Firefox(options=options, executable_path=r"C:\Users\subho\OneDrive\Documents\automation_codes\geckodriver.exe")
driver.get('https://www.saucedemo.com/')
# time.sleep(10)
driver.maximize_window()
# time.sleep(3)
username = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div[1]/div/form/div[1]/input")
username.send_keys("standard_user")
# time.sleep(1)
password = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div[1]/div/form/div[2]/input")
password.send_keys("secret_sauce")
# time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div[1]/div/form/input").click()
# time.sleep(1)


first_product()
second_product()



driver.close()
print("Test Successfully Executed...")
end_time = time.ctime()
print("Start time ", start)
print("End time ", end_time)