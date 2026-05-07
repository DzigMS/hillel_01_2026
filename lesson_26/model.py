from abc import ABC

from playwright.sync_api import Page, expect


class BasePage(ABC):
    URL = 'https://demoqa.com/'
    def __init__(self, page):
        self._page = page

    def navigate(self):
        self._page.goto(self.URL)


class TextBoxPage(BasePage):
    URL = 'https://demoqa.com/text-box'

    def __init__(self, page):
        super().__init__(page)


class AutomationPracticeFormPage(BasePage):
    URL = 'https://demoqa.com/automation-practice-form'

    def __init__(self, page):
        super().__init__(page)
        self._first_name_input = page.locator('css=#firstName')
        self._last_name_input = page.locator('css=#lastName')
        self._email_input = page.locator('css=#userEmail')
        self._DOB = page.locator('css=#dateOfBirthInput')
        self._submit_button = page.get_by_role('button', name='submit')
        self._current_address = page.locator('css=#currentAddress')
        self._state = page.locator('css=#react-select-3-input')
        self._userNumber = page.locator('css=#userNumber')

        self._male_gender_radio = page.get_by_role('radio', name='Male', exact=True)
        self._female_gender_radio = page.get_by_role('radio', name='Female')
        self._other_gender_radio = page.get_by_role('radio', name='Other')

        self._sport_hobby_checkbox = page.locator('css=#hobbies-checkbox-1')
        self._reading_hobby_checkbox = page.locator('css=#hobbies-checkbox-2')
        self._music_hobby_checkbox = page.locator('css=#hobbies-checkbox-3')

    def set_dob(self, dob):
        self._DOB.fill(dob)

    def set_number(self, number):
        self._userNumber.fill(number)

    def set_email(self, email):
        self._email_input.fill(email)

    def set_first_name(self, first_name):
        self._first_name_input.fill(first_name)

    def set_last_name(self, last_name):
        self._last_name_input.fill(last_name)
        self._last_name_input.screenshot()

    def set_state(self):
        self._state.scroll_into_view_if_needed()
        self._state.click()
        self._page.get_by_role("option", name="NCR").click()
        # self._state.select_option('NCR')
        # self._state.find_by_value('NCR').click()


    def set_gender_radio(self, radio_name='Male'):
        # if radio_name == 'Male':
        #     self._male_gender_radio.click()
        # elif radio_name == 'Female':
        #     self._female_gender_radio.click()
        # else:
        #     self._other_gender_radio.click()
        self._page.get_by_role('radio', name=radio_name, exact=True).click()

    def get_hobby(self, hobby):
        if 'Sports' == hobby:
            return self._sport_hobby_checkbox
        elif 'Music' == hobby:
            return self._music_hobby_checkbox
        else:
            return self._reading_hobby_checkbox

    def set_hobby(self, hobby):
        if 'Sports' == hobby:
            self._sport_hobby_checkbox.set_checked(True)
            # self._sport_hobby_checkbox.check()
        elif 'Music' == hobby:
            self._music_hobby_checkbox.set_checked(True)
            # self._music_hobby_checkbox.check()
        else:
            self._reading_hobby_checkbox.set_checked(True)

    def click_submit_button(self):
        self._submit_button.click()

class DynamicPropertiesPage(BasePage):
    URL = 'https://demoqa.com/dynamic-properties'

    def __init__(self, page: Page):
        super().__init__(page)
        self._enabled_after_5_seconds_button = page.locator('css=#enableAfter')
        self._color_change_button = page.locator('css=#colorChange')
        self._visible_after_button = page.locator('css=#visibleAfter')
        self._random_id = page.locator('xpath=//*[@class="text-center"]/following-sibling::p')

    # def navigate(self):
    #     self._page.goto(self.URL)

    def get_random_id_text(self):
        return self._random_id.text_content()

    def is_visible_after_button(self):
        return self._visible_after_button.is_visible()

    def is_enabled_after_button(self):
        return self._enabled_after_5_seconds_button.is_enabled()