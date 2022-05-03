from enum import Enum


class TextType(Enum):
    PLAIN_TEXT = "plain_text"
    MARKDOWN_TEXT = "mrkdwn"


def text_element(
        text: str,
        text_type: TextType,
        emoji: bool = True,
        verbatim: bool = False,
        value: str = None
):
    """
    Summary: A slack block text node \n
    Args:
        text (str): The text to display
        text_type (TextType): The text type whether plain text or markdown
        emoji (bool): Whether to display emojis or not
        verbatim (bool): Whether to display verbatim or not
        value (str): The value to be passed down the app
    """
    if (
            text_type.value != TextType.PLAIN_TEXT.value
            and text_type.value != TextType.MARKDOWN_TEXT.value
    ):
        raise ValueError("text_type must be `plain_text` or `mrkdwn`")
    node = {
        "text": {
            "type": text_type.value,
            "text": text,
            "emoji": emoji
        }
    }
    if value is not None:
        node["value"] = value
    if text_type == TextType.MARKDOWN_TEXT.value:
        node.pop("emoji")
    if verbatim:
        node['text']['verbatim'] = True
    return node
