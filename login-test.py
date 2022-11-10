from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re

# Load the Chrome Driver
driver = webdriver.Chrome('./chromedriver')

# Load the bioskoponline.com page
driver.get('http://bioskoponline.com')
print('========================================')

# Credential
email = 'regy888@gmail.com'
phoneNumber = '081809172223'
password = 'Regy1234'

# Check the credential, as the password input only shows when the Nomor Ponsel / Email filled correctly.
# Phone Number must be started by 0 and minimum length is 10
def validateCredential():
    validPhoneNumber = bool(re.search('^0', phoneNumber)) & (len(phoneNumber) > 9)
    emailCompile = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    validEmail = bool(re.fullmatch(emailCompile, email))
    result = []

    if validPhoneNumber:

        result.append('Phone number is valid')
    else:
        result.append('Phone number is invalid') 

    if validEmail:
        result.append( 'Email is valid')
    else:
        result.append('Email is invalid') 

    if len(password) != 0:
        result.append('Password is valid') 
    else:
        result.append('Password is null') 
    
    print( ', '.join(result))
    return result
validateCredential()

# Find the 'Masuk' button with the limit 30 seconds to load and click once it found.
try: 
    loginButton = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="__layout"]/div/div[2]/div/div/div/button[3]/span'))
        )
    print('Masuk button found') 
except:
    print('Masuk button not found')
    driver.quit()
finally:
    loginElem = driver.find_element(by='xpath', value='//*[@id="__layout"]/div/div[2]/div/div/div/button[3]/span')
    loginElem.click()

# Select to login method
def loginViaGoogle():
    # Find and click Google button
    print('Login via Google')
    try: 
        # Looking for Google button
        googleButton = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="__layout"]/div/div[5]/div[2]/div/div[2]/button[1]'))
            )
        print('Google button found')
    except:
        # If the Google button not found
        print('Google button not found')
        driver.quit()
    finally:
        # Select the Google button and click it
        googleButtonElem = driver.find_element(by='xpath', value='//*[@id="__layout"]/div/div[5]/div[2]/div/div[2]/button[1]')
        googleButtonElem.click()

        # Print the current URL. This should be redirected to Google Auth page. 
        currentURL = driver.current_url
        print('Current URL: ' + currentURL)

def loginViaFacebook():
    # Find and click Google button
    print('Login via Facebook')
    try: 
        # Looking for Google button
        facebookButton = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="__layout"]/div/div[5]/div[2]/div/div[2]/button[2]'))
            )
        print('Google button found')
    except:
        # If the Google button not found
        print('Google button not found')
        driver.quit()
    finally:
        # Select the Google button and click it
        facebookButtonElem = driver.find_element(by='xpath', value='//*[@id="__layout"]/div/div[5]/div[2]/div/div[2]/button[2]')
        facebookButtonElem.click()

        # Print the current URL. This should be redirected to Facebook Auth page. 
        currentURL = driver.current_url
        print('Current URL: ' + currentURL)

def loginByPhoneEmail():    
    # Wait the modal to appear for 3 seconds. Find the email and password input,then fill them.
    try: 
        emailPhoneInput = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="__layout"]/div/div[5]/div[2]/div/form/div/div/input'))
            )
        print('Nomor ponsel / email input found')
    except:
        print('Nomor ponsel / email input not found')
        driver.quit()
    finally:
        emailPhoneElem = driver.find_element(by='xpath', value='//*[@id="__layout"]/div/div[5]/div[2]/div/form/div/div/input')
        emailPhoneElem.send_keys(email)

    # Find the password input, once Nomor ponsel / email input correctly 
    try: 
        passInput = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="__layout"]/div/div[5]/div[2]/div/form/div[2]/div/label/div[2]/input'))
            )
        print('Password input found')
    except:
        print('Password input not found')
        driver.quit()
    finally:
        passElem = driver.find_element(by='xpath', value='//*[@id="__layout"]/div/div[5]/div[2]/div/form/div[2]/div/label/div[2]/input')
        passElem.send_keys(password)

    # Find the Submit button 
    try: 
        submitButton = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="__layout"]/div/div[5]/div[2]/div/form/button'))
            )
        print('Submit button found')
    except:
        print('Submit button not found')
        driver.quit()
    finally:
        submitElem = driver.find_element(by='xpath', value='//*[@id="__layout"]/div/div[5]/div[2]/div/form/button')
        submitElem.click()

    # See the login result by checking the toast message
    try: 
        toastMessage = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='toasted custom-toast toasted-primary default']"))
            )
        print('Toast message found')

        toastMessageContent = driver.find_element(by='xpath', value="//div[@class='toasted custom-toast toasted-primary default']")
        print('Message: ' + toastMessageContent.text)
    except:
        print('Toast message not found')
        errMessage = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="__layout"]/div/div[5]/div[2]/div/div[4]/div/div[1]'))
            )

        toastMessageContent = driver.find_element(by='xpath', value='//*[@id="__layout"]/div/div[5]/div[2]/div/div[4]/div/div[1]')
        print('Message: ' + toastMessageContent.text)

# Execute the login process
# loginByPhoneEmail()
# loginViaFacebook()
# loginViaFacebook
