import re
from os import makedirs
from time import sleep

from playwright.sync_api import sync_playwright, Browser, BrowserContext

from utils.structs import Job

user_data_dir = 'userDataDir'
makedirs(user_data_dir, exist_ok=True)

search_url = f'https://www.linkedin.com/jobs/search/' \
             f'?keywords=mailchimp' \
             f'&refresh=true' \
             f'&location=Canada' \
             f'&start=0'


def parse_one_job(html_snippet: str):
    pass


def parse_all_jobs(html_whole_page: str) -> list[Job]:
    jobs = []

    for html_snippet in re.findall(r'', html_whole_page):
        jobs.append(parse_one_job(html_snippet))


def apply_to_one_job(job: Job):
    pass


def apply_to_all_jobs():
    """
    Continuous fx.
    playwright._impl._api_types.TimeoutError:
    :return:
    """
    while True:
        current_html = page.content()
        for job in parse_all_jobs(current_html):
            apply_to_one_job(job)
        sleep(60)


with sync_playwright() as p:
    context: BrowserContext = p.firefox.launch_persistent_context(
        user_data_dir=user_data_dir,
        headless=False,
        no_viewport=True
    )

    page = context.pages[0]
    page.goto(search_url, timeout=0)
    sleep(10)
    with open('a.html', 'w', encoding='utf-8') as file:
        file.write(page.content())
    print('wrote page to file')
    sleep(600)
    # start applying to jobs on my behalf. If failed job application, note and put away. Like, if timeout thing happens
    apply_to_all_jobs()
