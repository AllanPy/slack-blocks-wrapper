from slack_blocks_wrapper.section import text_node, TextType


def input_block_node(
        label: str,
        element: dict,
        dispatch_action: str = None,
        block_id: str = None,
        hint: str = None,
        optional: bool = False,
):
    """
    Available in surfaces: `Modals`, `Messages`, `Home tabs`

    A block that collects information from users - it can hold a plain-text
input element, a checkbox element, a radio button element, a select menu
element, a multi-select menu element, or a datepicker.

Read slack guides to collecting input in modals or in Home tabs to learn how
input blocks pass information to your app.

    Args:
    label (str): A label that appears above an input element in the form of a
                text object that must have type of plain_text.
    element (dict): The element of the input block.
    dispatch_action (str): The action to be dispatched when the input block is
        submitted.
    block_id (str): The ID of the input block.
    hint (str): A hint to be displayed below the input block.
    optional (bool): Whether the input block is optional.

    Returns:
        dict: The input block node.
    Example:
        >>> from slack_blocks_wrapper.input import input_block_node
        >>> from slack_blocks_wrapper.elements import plain_text_input_element
        >>> input_block_node(
        ...     label='What is your name?',
        ...     element=plain_text_input_element(placeholder="Enter your name", action_id="enter_name"),
        ...     dispatch_action='enter_name',
        ...     block_id='enter_name',
        ...     hint='This is a hint',
        ...     optional=False,
        ... )
        {
            "type": "input",
            "label": {
                "type": "plain_text",
                "text": "What is your name?",
                "emoji": True
            },
            "block_id": "enter_name",
            "element": {
                "type": "plain_text_input",
                "action_id": "enter_name",
                "placeholder": {
                    "type": "plain_text",
                    "text": "Enter your name",
                    "emoji": True
                }
            },
    Can view more here:
    """
    if not element:
        raise ValueError("element is required")
    node = {
        "type": "input",
        "label": text_node(label, TextType.PLAIN_TEXT),
        "element": element
    }
    if dispatch_action:
        node["dispatch_action"] = dispatch_action
    if hint:
        node["hint"] = text_node(hint, TextType.PLAIN_TEXT)
    if optional:
        node["optional"] = optional
    if block_id:
        node["block_id"] = block_id
    return node
