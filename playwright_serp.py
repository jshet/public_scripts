from playwright.sync_api import Playwright, sync_playwright, expect
from time import sleep
from random import randint
import json
import os

# --- put your inputs in scratchpad ---
from scratchpad import query_list


queries = query_list
output_dir = "scratch"

def act_natural():
    sleep(randint(1,5))

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    #----------------------

    all_queries = queries
    all_links = {}

    for next_query in all_queries:
        try:
            output_file = os.path.join(output_dir, f'{next_query.replace(" ","_")}.csv')
            with open(output_file, "w") as f:
                f.write("site,url\n")
            sites = {}
            links = []
            q = next_query.replace(" ","+")
            url = f"https://duckduckgo.com/?q={q}&hps=1&start=1&ia=web"

            page.goto(url)

            try:
                for i in range(5):
                    page.get_by_role("link", name="More results").click()
                    act_natural()
            except Exception as ex:
                print(ex)

            all_results = page.get_by_test_id("result-title-a")
            result_count = all_results.count()
            for i in range(result_count):
                r = all_results.nth(i)
                a = r.get_attribute("href")
                if "duckduckgo" not in a:
                    links.append(a)

            for a in links:
                site = a.split("//")[1].split("/")[0]
                if "www" in site:
                    site = site.split("www.")[1]
                if site not in sites:
                    sites[site] = a           

            with open(output_file, "a") as f_out:
                for s, r in sites.items():
                    f_out.write(f'{s},{r}\n')
                
            all_links[next_query] = links
        except Exception as ex:
            context.close()
            browser.close()
            print(ex)
        
        sleep(randint(10,30))

    with open('search_results.json', 'w') as f:
        json.dump(all_links, f)

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
