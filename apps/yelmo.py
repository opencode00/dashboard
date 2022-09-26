from playwright.sync_api import sync_playwright

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto('https://yelmocines.es/cartelera/santa-cruz-tenerife')
        page.wait_for_timeout(5000)

        # titles = page.query_selector_all('header > h3 > a')
        titles = page.query_selector_all('article > figure > a ')       
        for title in titles:
            # print(title.evaluate("item => item.innerText"))
            print(title.evaluate("item => item.innerHTML"))
            print(title.evaluate("item => item.href"))

if __name__ == '__main__':
    main()