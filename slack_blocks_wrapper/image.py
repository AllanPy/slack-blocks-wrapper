from .elements.text import text_element, TextType


def image_block_node(
        image_url: str,
        alt_text: str,
        title: str,
        block_id: str
):
    """
    Supported surfaces: `Modals`, `Messages`, `Home tabs`

    A simple image block, designed to make those cat photos really pop.

    :param image_url: The URL of the image.
    :param alt_text: The alt text of the image.
    :param title: The title of the image.
    :param block_id: A string acting as a unique identifier for a block.
                    If not specified, one will be generated.
    :return: A block node for an image.

    Example:
        Returned JSON is similar to the following example:
      https://api.slack.com/reference/block-kit/blocks#image_example
    """
    return {
        "type": "image",
        "block_id": block_id,
        "image_url": image_url,
        "alt_text": alt_text,
        "title": text_element(title, TextType.PLAIN_TEXT)
    }
