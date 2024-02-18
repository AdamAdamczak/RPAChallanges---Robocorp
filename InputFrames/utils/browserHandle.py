import robocorp.browser as browser
import time 
URL = "https://rpachallenge.com/"
START_SELECTOR = "xpath=//button[contains(.,'Start')]"
def open_browser() -> browser.Page:
    browser.goto(URL)
    page = browser.page()
    page.locator(START_SELECTOR).wait_for()
    return page

def start_challenge(page: browser.Page) -> None:
    page.locator(START_SELECTOR).click()
    
    
def fill_forms(page: browser.Page,payload: dict):
    start_time = time.time()
    for label, value in payload.items():
        iteration_start_time = time.time()
        page.locator(f"xpath=//label[contains(.,'{label}')]/../input").fill(value=str(value))
        iteration_duration = time.time() - iteration_start_time
        print(f"Time taken to fill '{label}' field: {iteration_duration} seconds")
    submit_start_time = time.time()
    page.keyboard.press("Enter")
    submit_time = time.time() - submit_start_time
    print(f"Time taken to submit the form: {submit_time} seconds")
    print(f'Total time taken to fill the form: {time.time() - start_time} seconds')

    
def get_results(page: browser.Page) -> dict:
    results = page.locator(".message2").text_content()
    print(results)
    return {"results": results}