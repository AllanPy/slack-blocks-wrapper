def context(elements: list, block_id: str):
    """
    Summary: Available in surfaces: `Modals`, `Messages` `Home tabs` \n
    Args:
    elements: An array of image elements and text objects. Max length: `10`\n
    block_id: A string acting as a unique identifier for a block. If not
        specified, one will be generated. Maximum length for this field is
        255 characters. block_id should be unique for each message and each
        iteration of a message. If a message is updated, use a new block_id.
        Displays message context, which can include both images and text.

    Example:
        >>> context(
        elements=[
        image_element(
        'https://image.freepik.com/free-photo/red-drawing-pin_1156-445.jpg',
        alt_text='Red pin',
        ),
        text_element('This is a message with a red pin', is_plain_text=True),
        ],
        block_id='block_id'
        )
    Gives you output similar to the JSON object here:
    https://api.slack.com/reference/block-kit/blocks#context_examples
    """
    return {
        "type": "context",
        "elements": elements,
        "block_id": block_id
    }
