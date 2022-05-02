def header_block_node(text: str, block_id: str):
    """
    Supported surfaces:  `Modals`, `Messages`, `Home tabs`
    A header is a plain-text block that displays in a larger, bold font.
    Use it to delineate between different groups of content in your app's surfaces.

    Args:
        text (str): The text to display in the header.
        block_id (str): The ID of the block.
    Example:
       >>> header_block_node("My header", "my_header")
    Returns a JSON object with format as follows:
    https://api.slack.com/reference/block-kit/blocks#header_examples
    """
    node = {
        "type": "header",
        "text": text
    }
    if block_id:
        node["block_id"] = block_id
    return node
