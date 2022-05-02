def image_element(image_url: str, alt_text: str):
    """
    Works with block types: `Section`,`Context` \n
    An element to insert an image as part of a larger block of content.
    If you want a block with only an image in it, you're looking for the image block.

    Args:
        image_url (str): The URL of the image to display.
        alt_text (str): A text description of the image for visually impaired users.

    Returns:
        dict: A dictionary representation of an image element.
    """
    return {
        "type": "image",
        "image_url": image_url,
        "alt_text": alt_text
    }
