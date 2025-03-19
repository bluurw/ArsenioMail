from playwright.sync_api import sync_playwright
from time import sleep

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)  # Run visible for debugging
    page = browser.new_page()

    page.goto("https://app.tuta.com/signup#subscription")
    page.wait_for_load_state("networkidle")
    
    button = page.locator("div.button-min-height:nth-child(5) > button:nth-child(1)")
    if (button.count() == 1):
            button.click()
            sleep(3)

            input_term_1 = page.locator("div.dialog-contentButtonsBottom:nth-child(2) > div:nth-child(1) > label:nth-child(1) > input:nth-child(1)")
            input_term_2 = page.locator("div.click:nth-child(2) > label:nth-child(1) > input:nth-child(1)")
            
            input_term_1.click()
            input_term_2.click()
            
            sleep(1.5)
            
            input_ok_button = page.locator("button.b") # ok button
            input_ok_button.click()

            sleep(1.5)

            # CADASTRO
            form_input_email = page.locator(".right")
            form_input_email.fill("diguiDimDigo")

            sleep(2) # esperar a verificacao do email

            form_input_password = page.locator("#signup-account-dialog > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)")
            form_input_password.fill("Kias3@**")

            from_input_repeat_password = page.locator("div.text-field:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)")
            from_input_repeat_password.fill("Kias3@**")


            input_term_data_1 = page.locator("div.pt:nth-child(3) > label:nth-child(1) > input:nth-child(1)")
            input_term_data_1.click()
            input_term_data_2 = page.locator("div.pt:nth-child(6) > label:nth-child(1) > input:nth-child(1)")
            input_term_data_2.click()

            sleep(15)
            input_next_button = page.locator("div.mt-l:nth-child(7) > button:nth-child(1)")
            input_next_button.click()

    
    sleep(5)
    page.screenshot(path="example-teste.png")
    browser.close()

    '''
    # Locate all matching elements
    buttons = page.locator("a#signup-button")
    print(f"Found {buttons.count()} matching elements.")

    # Try interacting with the second button
    second_button = buttons.nth(1)  # Adjust index as needed
    second_button.scroll_into_view_if_needed()
    second_button.wait_for(state="visible", timeout=60000)
    second_button.click()
    '''