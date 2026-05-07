from time import sleep

import pytest

from data_model import PracticeFormUser
from steps import AutomationPracticeFormStep
from model import AutomationPracticeFormPage, DynamicPropertiesPage



def test_form(page):
    test_user = PracticeFormUser()
    print(test_user)

    form_page = AutomationPracticeFormPage(page)
    form_page.navigate()

    step = AutomationPracticeFormStep(form_page)
    step.fill_names_fields(test_user.first_name, test_user.last_name)
    step.set_email(test_user.email)
    step.fill_number(test_user.mobile)
    step.set_dob(test_user.dob)
    step.set_gender_radio(test_user.gender)
    step.set_hobbies(['Music', 'Sports'])
    step.set_state()

    step.submit_form()
    sleep(5)
