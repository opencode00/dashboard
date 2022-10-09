from selenium.webdriver  import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def cines(lugar=None):
    url = 'https://yelmocines.es/cartelera/santa-cruz-tenerife'
    opts = Options()
    opts.add_argument('--headless')
    driver = Chrome(options=opts)
    driver.get(url)
    driver.implicitly_wait(6)
    if (lugar == 'meridiano'):
        titles = driver.find_elements(By.CSS_SELECTOR,'div[data-cinema=meridiano] h3 > a ')
    else:
        titles = driver.find_elements(By.CSS_SELECTOR,'div[data-cinema=la-villa-de-orotava] h3 > a ')
    print(lugar)
    data = []
    for i in titles:
        # print(f'<href="{i.get_attribute("href")}" target=_blank>{i.get_attribute("innerHTML")}</a>')
        data.append(f'<a href="{i.get_attribute("href")}" target=_blank>{i.get_attribute("innerHTML")}</a>')

    return data
