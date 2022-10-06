# from playwright.sync_api import sync_playwright
# import pprint

# def cines(lugar):
#     with sync_playwright() as p:
#         url = 'https://yelmocines.es/cartelera/santa-cruz-tenerife'
#         browser = p.chromium.launch(headless=True)
#         page = browser.new_page()
#         page.goto(url)
#         page.wait_for_timeout(4000)
#         meridiano = []    
#         orotava = []
#         # titles = page.query_selector_all('header > h3 > a')
#         titles = page.query_selector_all('article > figure > a ')
#         cines = page.query_selector_all('span#detail-movie')
#         for i in range(len(titles)-1):
#             # print(title.evaluate("item => item.innerText"))
#             img = titles[i].evaluate("item => item.innerHTML")
#             link = titles[i].evaluate("item => item.href")
#             cine = cines[i].evaluate("item => item.dataset.list")
#             if cine == 'Cartelera-la-villa-de-orotava':
#                 orotava.append(f"<a href={link}>{img} ({cine})</a>")
#             else:
#                 meridiano.append(f"<a href={link}>{img} ({cine})</a>")
    
#     if lugar == 'meridiano':
#         return meridiano
    
#     return orotava


# if __name__ == '__main__':
#    pprint.pprint(cines('meridiano'))