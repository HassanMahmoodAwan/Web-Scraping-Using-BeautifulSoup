from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import csv


class one():
    def __int__(self, title, price):
        self.title = title
        self.price = price


class two():
    def data(self, name):
        count = 1
        page = 1
        addPage = 10
        maximum = 100

        List = list()

        url = "https://www.amazon.com/s?k=" + name + "&page=" + str(page)

        my_options = Options()
        my_options.headless = False
        my_options.add_experimental_option("detach", True)

        my_browser = webdriver.Chrome(ChromeDriverManager().install(), options=my_options)
        my_browser.maximize_window()
        my_browser.get(url)
        my_browser.set_page_load_timeout(12)


        while True:
          try:
            if addPage * page > maximum:
                break
            if count > addPage:
                count = 1
                page = page + 1

            title_path = '//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div['+ str(count) + ']/div/div/div/div/div/div/div/div[2]/div/div/div[1]/h2'
            Title = my_browser.find_element(By.XPATH, title_path)
            Title_text = Title.get_attribute("innerHTML").splitlines()[0]
            Title.click()

            price_path = '//*[@id="priceblock_ourprice"'
            Price = my_browser.find_element(By.XPATH, price_path)
            price_text = Price.get_attribute("innerHTML")

            url = "https://www.amazon.com/s?k=iphone+14"
            my_browser.get(url)
            my_browser.set_page_load_timeout(12)

            my_info = one(Title_text, price_text)
            List.append(my_info)
            count = count + 1
          except Exception as e:
              print("Exception on the count ", count, e)

              if addPage * page > maximum:
                  break
              if count > addPage:
                  count = 1
                  page = page + 1

              url = "https://www.amazon.com/s?k=iphone+14"
              my_browser.get(url)
              my_browser.set_page_load_timeout(12)


        my_browser.close()
        return List


my_func = two()
with open("one.csv", 'w', newline='', encoding='utf-8') as csvfile:
    data = csv.writer(csvfile, delimiter = ";", quotechar = '"', quoting = csv.QUOTE_MINIMAL)
    for article in my_func.data("iphone 14"):
        data.writerow([article.title, article.price])






