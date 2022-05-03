from typing import Literal
from .text import text_element, TextType


def button_element(
        text: str,
        action_id: str,
        style: Literal["primary", "danger", "link"],
        value: str = "",
        url: str = None,
        accessibility_label: str = None,
        confirm: dict = None
):
    if style not in ["danger", "primary", None]:
        raise ValueError("style must be `primary` or `danger`")
    node = {
        "type": "button",
        **text_element(text, TextType.PLAIN_TEXT),
        "value": value,
        "action_id": action_id,
        "style": style
    }
    if style is None or style == "link":
        node.pop("style")
    if style == "link":
        node["url"] = url
    if accessibility_label is not None:
        node["accessibility_label"] = accessibility_label
    if confirm is not None:
        node["confirm"] = confirm
    return node
