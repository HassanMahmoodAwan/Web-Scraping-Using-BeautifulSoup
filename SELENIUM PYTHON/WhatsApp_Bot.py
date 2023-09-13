import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def user_chat(name_user):
    chat_new = browser.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div/div[2]/div/div')
    chat_new.click()

    user_chat = browser.find_element(By.XPATH, '//div[@class="_3u328"] copyable-text-selectable-text')
    user_chat.send_keys(name_user)

    time.sleep(2)

    try:
        user = browser.find_element(By.XPATH, '//span[@title="{}"]', format(name_user))
        user.click()

    except Exception as e:
        print(f"User {name_user} not in your Contacts")
    except Exception as e:
        browser.close()
        print(e)  # Let see what happens
        sys.exit()



if __name__ == '__main__':
    chrome_option = webdriver.ChromeOptions()
    chrome_option.add_experimental_option("detach", True)

    browser = webdriver.Chrome(options=chrome_option)
    browser.get("http://web.whatsapp.com")
    time.sleep(20)

    name_list = ["Home"]
    for name_user in name_list:
        #user_chat(userName)

        try:
            user = browser.find_element(By.XPATH, '//span[@title="{}"]'.format(name_user))
            user.click()
        except Exception as e:
            print(e)

        box_message = browser.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]')
        box_message.send_keys("Hi, Its a Computertized whatApp Bot generated Message for Bussiness Automation Testing.")

        #time.sleep(2)
        box_message = browser.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button')
        box_message.click()
        #time.sleep(5)

    browser.close()



