from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from .models import Live_CPU
import time

def run_web_scraper():
    print("✅ Web scraper is running!")



    service = Service()
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    Live_CPU.objects.all().delete()




    urls='https://www.techpowerup.com/{}-specs/?f=mfgr'

    urlss= urls.format("cpu")
    print(urlss)
    driver.get(urlss)

    time.sleep(3)

    filter_element = driver.find_elements(By.CSS_SELECTOR, ".filter-options a")
    print("elments",filter_element)
    filter_names = []
    for element in filter_element:
        text = element.text.strip().split(' (')[0]

        print("value", text)
        if text:  # skip empty values
            filter_names.append(text)

    print("Found filters:", filter_names)

    print('Filters found')

    base_url = 'https://www.techpowerup.com/{}-specs/?f=mfgr_{}'
    all_cpus = []

    for manufacturer in filter_names:
        url = base_url.format("cpu",manufacturer)
        print("url",url)
        driver.get(url)
        time.sleep(5)

        soup = BeautifulSoup(driver.page_source, 'html.parser')
        table = soup.find("table", class_='items-desktop-table') 

        rows = table.find_all("tr")[1:]  # Skip header

        for row in rows:
            cols = [col.text.strip() for col in row.find_all("td")]
            for cpu in cols:
                Live_CPU.objects.get_or_create(name=cols[0],cpu_mark="NotUpdated", cores=int(cols[2].split("/")[0].strip()) ,socket=cols[4] ,tdp=int(cols[7].split()[0].strip()) )
            print("current data", cols)
            
    driver.quit()





