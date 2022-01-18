from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import json


def wait_for_alert_and_accept(browser, time_to_wait):
    WebDriverWait(browser, time_to_wait).until(EC.alert_is_present())
    alert = browser.switch_to.alert
    alert.accept()


def wait_for_element_be_located(browser, time_to_wait, by_element, element_id):
    if by_element == "CLASS_NAME":
        return WebDriverWait(browser, time_to_wait).until(EC.visibility_of_element_located((By.CLASS_NAME, element_id)))
    elif by_element == "XPATH":
        return WebDriverWait(browser, time_to_wait).until(EC.visibility_of_element_located((By.XPATH, element_id)))
    elif by_element == "ID":
        return WebDriverWait(browser, time_to_wait).until(EC.visibility_of_element_located((By.ID, element_id)))
    elif by_element == "CSS_SELECTOR":
        return WebDriverWait(browser, time_to_wait).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, element_id)))


def convert_string_to_dict_from_file(list_of_lines_from_txt):
    final_dictionary = {}
    for single_line in list_of_lines_from_txt:
        # change single quotes to double
        updated_str_line = single_line.replace("'", '"')
        final_dictionary.update(json.loads(updated_str_line))
    return final_dictionary
