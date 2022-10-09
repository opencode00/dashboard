from selenium.webdriver  import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def cines():
    url = 'https://yelmocines.es/cartelera/santa-cruz-tenerife'
    opts = Options()
    opts.add_argument('--headless')
    driver = Chrome(options=opts)
    driver.get(url)
    driver.implicitly_wait(5)
    lmeridiano = driver.find_elements(By.CSS_SELECTOR,'div[data-cinema=meridiano] h3 > a ')
    lorotava = driver.find_elements(By.CSS_SELECTOR,'div[data-cinema=la-villa-de-orotava] h3 > a ')
    meridiano = []
    orotava = []
    for i in lmeridiano:
        # print(f'<href="{i.get_attribute("href")}" target=_blank>{i.get_attribute("innerHTML")}</a>')
        meridiano.append(f'<a href="{i.get_attribute("href")}" target=_blank>{i.get_attribute("innerHTML")}</a>')

    for i in lorotava:
        # print(f'<href="{i.get_attribute("href")}" target=_blank>{i.get_attribute("innerHTML")}</a>')
        orotava.append(f'<a href="{i.get_attribute("href")}" target=_blank>{i.get_attribute("innerHTML")}</a>')

    return meridiano,orotava

if __name__ == '__main__':
    print(cines()[0])
    print("---------------")
    print(cines()[1])