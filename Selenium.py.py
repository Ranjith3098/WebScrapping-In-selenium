from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time

driver = webdriver.Chrome()

url = #give the url 

driver.get(url)

web = WebDriverWait(driver, 30)

route_pg_clik =web.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div/div[5]/div[3]/div/div/div/div/div/div/ul/li[9]/ul/li[4]/a")))
route_pg_clik.click()

list_of_url = []

while True:
    try:
        selector = '.pflist-itemdetails'
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, selector)))

        ul_element = driver.find_elements(By.CSS_SELECTOR, selector)

        for i in ul_element:
            ele = i.find_element(By.TAG_NAME, 'a')
            link = ele.get_attribute('href')
            list_of_url.append(link)
        
        for_next_page = driver.find_element(By.CLASS_NAME,'next')
        for_next_page.click()
    
    except Exception as e:
        print('system: next page not found')
        break



print(list_of_url)

list_of_data = []
try:
    for i in list_of_url:
        driver.get(i)
        selector = '.pfdetailitem-subelement'
        data_tag = driver.find_elements(By.CSS_SELECTOR, selector)
        title = driver.find_element(By.CLASS_NAME, 'pf-item-title-text')
        head = title.text
        list_of_data.append([head])
        for i in data_tag:
            data_txt = i.text.split('\n')
            list_of_data.append(data_txt)
    print('data taking process complete')
        
except Exception as e:
    print('system: some Error')

# df = pd.DataFrame(list_of_data, columns=['Listing Type', 'QCCI Membership Number', 'PO Box', 'Phone'])

df = pd.DataFrame(list_of_data)

print(df)

excel_filename = 'transport.xlsx'
df.to_excel(excel_filename, index= False, header=False)

print('Chrome Closed')

driver.quit()
    






