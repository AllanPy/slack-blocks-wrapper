from typing import Literal

from ..elements import (
    user_select_element as _user_select,
    multistatic_select_element as _multistatic_select,
    multiconversations_select_element as _multiconversations_select,
    button_element as _button,
    image_element as _image,
    datepicker_element as _datepicker,
    checkbox_element as _checkbox,
    overflow_menu as _overflow_menu_element,
    text_element as _text_element,
    TextType
)


SECTION_TYPE = {"type": "section"}


def plain_text(emoji: bool, text: str, accessory: dict = None):
    """
    Summary: A plain text section \n
    Args:
        emoji (bool): Whether to display emojis or not
        text (str): The text to display
        accessory (dict): The accessory to display
    Returns:
        dict: a plain text section dictionary
    """
    return {
        **SECTION_TYPE,
        **_text_element(text, TextType.PLAIN_TEXT, emoji),
        **{"accessory": accessory}
    }


def markdown_text(text: str, accessory: dict = None):
    """
    Summary: A markdown text section \n
    Args:
        text (str): The text to display
        accessory (dict): The accessory to display
    Returns:
        dict: a markdown text section dictionary
    """
    return {**SECTION_TYPE, **_text_element(text, TextType.MARKDOWN_TEXT),
            **{"accessory": accessory}}


def text_fields(fields: list):
    """
    Summary: A text fields section \n
    Args:
        fields (list): The fields to display
    Returns:
        dict: a text fields section dictionary
    """
    return {**SECTION_TYPE, **{"fields": fields}}


def users_select(text: str, action_id: str, is_plain_text: bool = False):
    return {
        **SECTION_TYPE,
        **_text_element(
            text, TextType.PLAIN_TEXT
            if is_plain_text else TextType.MARKDOWN_TEXT
        ),
        **{"accessory": _user_select(text, action_id)}
    }


def multi_static_select(text: str, options: list, action_id: str):
    """
    Summary: A multi static select section \n
    Args:
        text (str): The text to display
        options (list): The options to display
        action_id (str): The action id
    Returns:
        dict: a multi static select section dictionary
    """
    return {
        **SECTION_TYPE,
        **_text_element(text, TextType.PLAIN_TEXT),
        **{"accessory": _multistatic_select(text, options, action_id)}
    }


def multi_conversations_select(
        text: str,
        action_id: str,
        is_plain_text: bool = False
):
    """
    Summary: A multi conversations select section \n
    Args:
        text (str): The text to display
        action_id (str): The action id
        is_plain_text (bool): Whether to display as plain text or not
    Returns:
        dict: a multi conversations select section dictionary
    """
    return {
        **SECTION_TYPE,
        **_text_element(
            text,
            TextType.PLAIN_TEXT if is_plain_text else TextType.MARKDOWN_TEXT
        ),
        **{"accessory": _multiconversations_select(text, action_id)}
    }


def button_section(
        text: str,
        action_id: str,
        style: Literal["primary", "danger"],
        value: str = None,
        url: str = None,
        accessibility_label: str = None,
        confirm: dict = None
):
    """
    Summary: A button section \n
    Args:
        text (str): The text to display on the button
        action_id (str): The action id
        style (str): The style of the button
        accessibility_label (str): The accessibility label
        confirm (dict): The confirm object
        url (str): The url to navigate to
        value (str): The value of the button
    Returns:
        dict: a button section dictionary
    """
    return {
        **SECTION_TYPE,
        **_text_element(text, TextType.PLAIN_TEXT),
        **{"accessory": _button(
            text, action_id, style, value, url, accessibility_label, confirm
        )}
    }


def image(
        text: str,
        image_url: str,
        alt_text: str,
        is_plain_text: bool = False
):
    """
    Summary: A image section \n
    Args:
        text (str): The text to display
        image_url (str): The image url
        alt_text (str): The alt text
        is_plain_text (bool): Whether to display as plain text or not
    Returns:
        dict: an image section dictionary
    """
    return {
        **SECTION_TYPE,
        **_text_element(
            text,
            TextType.PLAIN_TEXT if is_plain_text else TextType.MARKDOWN_TEXT
        ),
        **{"accessory": _image(image_url, alt_text)}
    }


def overflow_menu(
        text: str,
        options: list,
        action_id: str,
        is_plain_text: bool = False):
    """
    Summary: An overflow menu section \n
    Args:
        text (str): The text to display
        options (list): The options to display
        action_id (str): The action id
        is_plain_text (bool): Whether to display as plain text or not
    Returns:
        dict: an overflow menu section dictionary
    """
    return {
        **SECTION_TYPE,
        **_text_element(
            text,
            TextType.PLAIN_TEXT if is_plain_text else TextType.MARKDOWN_TEXT
        ),
        **{"accessory": _overflow_menu_element(options, action_id)}
    }


def datepicker(
        text: str,
        action_id: str,
        initial_date: str = None,
        placeholder: str = None,
        is_plain_text: bool = False
):
    """
    Summary: A datepicker section \n
    Args:
        text (str): The text to display
        action_id (str): The action id
        initial_date (str): The initial date
        placeholder (str): The placeholder
        is_plain_text (bool): Whether to display as plain text or not
    Returns:
        dict: a datepicker section dictionary
    """
    return {
        **SECTION_TYPE,
        **_text_element(
            text,
            TextType.PLAIN_TEXT if is_plain_text else TextType.MARKDOWN_TEXT
        ),
        **{"accessory": _datepicker(
            action_id, initial_date, placeholder
        )}
    }


def checkbox(
        text: str,
        options: list,
        is_plain_text: bool = False,
        action_id: str = None,
        initial_options: str = None,
        confirm: dict = None,
        focus_on_load: bool = False
):
    """
    Summary: A checkbox section \n
    Args:
        text (str): The text to display
        options (list): The options to display
        is_plain_text (bool): Whether to display as plain text or not,
        action_id (str): The action id
        initial_options (str): The initial options
        confirm (dict): The confirm object
        focus_on_load (bool): Whether to focus element on load or not
    Returns:
        dict: a checkbox section dictionary
    Example:
        >>> checkbox(
        text="Select your favorite color",
        options=[
        checkbox_option(text="Red", description="red color", value="red"),
        checkbox_option("Blue", "blue")
        ],
        is_plain_text=False
        )
    """
    return {
        **SECTION_TYPE,
        **_text_element(
            text,
            TextType.PLAIN_TEXT if is_plain_text else TextType.MARKDOWN_TEXT
        ),
        **{"accessory": _checkbox(
            options, action_id, initial_options, confirm, focus_on_load
        )}
    }
