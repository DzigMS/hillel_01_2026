from datetime import datetime

from playwright.sync_api import expect

from model import BasePage, AutomationPracticeFormPage


class AutomationPracticeFormStep:

    def __init__(self, page: AutomationPracticeFormPage):
        self._page = page

    def set_gender_radio(self, gender):
        expect(self._page._male_gender_radio).not_to_be_checked()
        expect(self._page._female_gender_radio).not_to_be_checked()
        expect(self._page._other_gender_radio).not_to_be_checked()

        self._page.set_gender_radio(gender)

        if gender == 'Male':
            expect(self._page._male_gender_radio).to_be_checked()
            expect(self._page._female_gender_radio).not_to_be_checked()
            expect(self._page._other_gender_radio).not_to_be_checked()
        elif gender == 'Female':
            expect(self._page._female_gender_radio).to_be_checked()
            expect(self._page._male_gender_radio).not_to_be_checked()
            expect(self._page._other_gender_radio).not_to_be_checked()
        else:
            expect(self._page._other_gender_radio).to_be_checked()
            expect(self._page._female_gender_radio).not_to_be_checked()
            expect(self._page._male_gender_radio).not_to_be_checked()

    def set_hobbies(self, hobbies):
        for h in hobbies:
            self._page.set_hobby(h)
            expect(self._page.get_hobby(h)).to_be_checked()

    def submit_form(self):
        self._page.click_submit_button()

    def set_state(self):
        self._page.set_state()

    def fill_number(self, number):
        self._page.set_number(str(number))

    def fill_names_fields(self, f_name, l_name):
        self._page.set_first_name(f_name)
        self._page.set_last_name(l_name)

    def set_dob(self, date: datetime):
        self._page.set_dob(date.strftime("%d %b %Y"))

    def set_email(self, mail):
        self._page.set_email(mail)