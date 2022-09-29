from playwright.sync_api import sync_playwright

def main(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url)
        page.wait_for_timeout(5000)
        data = []    
        # titles = page.query_selector_all('header > h3 > a')
        titles = page.query_selector_all('article > figure > a ')       
        for title in titles:
            # print(title.evaluate("item => item.innerText"))
            img = title.evaluate("item => item.innerHTML")
            link = title.evaluate("item => item.href")
            data.append(f"<a href={link}>{img}</a>")

        return data

def orotava():
    return main('https://yelmocines.es/cartelera/santa-cruz-tenerife/la-villa-de-orotava')

def meridiano():
    return main('https://yelmocines.es/cartelera/santa-cruz-tenerife/meridiano')


if __name__ == '__main__':
    orotava()