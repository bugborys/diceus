from typing import List

from selenium.webdriver.remote.webelement import WebElement

from libs.ui.pages.locators.locators_page_open_positions import POSITION_TITLE, POSITION_DEPARTMENT, POSITION_LOCATION


def is_job_card_has_required_info(card: WebElement, position: str, department: str, location: str) -> (bool, List[str]):
    errors = []

    try:
        position_element = card.find_element(*POSITION_TITLE)
        department_element = card.find_element(*POSITION_DEPARTMENT)
        location_element = card.find_element(*POSITION_LOCATION)
    except Exception as e:
        return False, [f"Failed to extract one or more elements: {e}"]

    if position not in position_element.text:
        errors.append(f"Position: expected to contain '{position}', got '{position_element.text}'")
    if department != department_element.text:
        errors.append(f"Department: expected '{department}', got '{department_element.text}'")
    if location != location_element.text:
        errors.append(f"Location: expected '{location}', got '{location_element.text}'")

    return len(errors) == 0, errors

def is_all_job_cards_has_required_info(cards: List[WebElement], position: str, department: str, location: str) -> (bool, str):
    errors_summary = []

    for i, card in enumerate(cards, start=1):
        result, errors = is_job_card_has_required_info(card, position, department, location)
        if not result:
            header = f'Card #{i} failed:'
            entry = '\n'.join([f'    {e}' for e in errors])
            errors_summary.append(f'{header}\n{entry}')

    if errors_summary:
        return False, '\n\n'.join(errors_summary)
    return True, ''
