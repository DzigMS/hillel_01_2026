from time import sleep
from playwright.sync_api import sync_playwright, expect

from steps import AutomationPracticeFormStep
from model import DynamicPropertiesPage, AutomationPracticeFormPage

# url = "https://demoqa.com/buttons"
url = "https://ithillel.ua/"


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, channel='chrome')
    context = browser.new_context()
    context.tracing.start()
    context.tracing.stop()
    sleep(3)
    page = browser.new_page()
    # page.screenshot()
    # page.route()

    form_page = AutomationPracticeFormPage(page)
    form_page.navigate()

    step = AutomationPracticeFormStep(form_page)
    step.set_gender_radio('Male')
    step.set_hobbies(['Music', 'Sports'])



    # sleep(3)
    # page.goto(url)
    # print(page.title())
    # sleep(3)
    # coaches = page.locator("css=#coachesSection")
    # coaches.scroll_into_view_if_needed()
    sleep(3)
    browser.close()