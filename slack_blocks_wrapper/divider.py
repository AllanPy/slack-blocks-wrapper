def divider_node(block_id: str = None):
    """
    Available surfaces: `Modals` `Messages` `Home tabs`
    This is a content divider like an <hr>, to split up different blocks inside a message.
     The divider block is nice and neat, requiring only a `type`.

    Args: block_id (str): [optional] The unique identifier for this block.
    One will be generated automatically if not specified.

    Call to this function returns a dict with the following structure:
       {
          "type": "divider"
    }
    """
    node = {
        "type": "divider"
    }
    if block_id is not None:
        node["block_id"] = block_id
    return node
