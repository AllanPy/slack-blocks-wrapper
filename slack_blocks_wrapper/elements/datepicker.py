import re

from .text import text_element, TextType


def datepicker_element(
        action_id: str,
        initial_date: str = None,
        placeholder: str = None,
        confirm: dict = None,
        focus_on_load: bool = False,
):
    node = {
        "type": "datepicker",
        "action_id": action_id,
        "focus_on_load": focus_on_load
    }
    if initial_date and re.search(
            "((?:19|20)\\d\\d)-(0?[1-9]|1[012])-([12][0-9]|3[01]|0?[1-9])",
            initial_date):
        node["initial_date"] = initial_date
    else:
        raise ValueError("`initial_date` must be a valid date")
    if placeholder:
        node["placeholder"] = text_element(placeholder, TextType.PLAIN_TEXT)
    if confirm:
        node["confirm"] = confirm
    return node
