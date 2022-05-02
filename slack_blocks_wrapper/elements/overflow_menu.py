def overflow_menu_element(
        options: list,
        action_id: str,
        confirm: dict = None
):
    """
    Works with block types: `Section`, `Actions` \n
    This is like a cross between a button and a select menu - when a user
    clicks on this overflow button, they will be presented with a list of
    options to choose from. Unlike the select menu, there is no typeahead field,
    and the button always appears with an ellipsis ("…") rather than customisable text. \n

    As such, it is usually used if you want a more compact layout than a
     select menu, or to supply a list of less visually important actions after
     a row of buttons. You can also specify simple URL links as overflow menu
     options, instead of actions.

     Args:
        options (list): A list of options to be displayed in the overflow menu.
        action_id (str): The action id of the overflow menu.
        confirm (dict): Confirm object

    Returns:
        dict: The overflow menu object.

    Ref: https://api.slack.com/reference/block-kit/block-elements#overflow
    """
    if not action_id:
        raise Exception("action_id is required")
    if not options:
        raise Exception("options is required")
    node = {
        "type": "overflow",
        "action_id": action_id
    }
    if confirm:
        node["confirm"] = confirm
    if options:
        node["options"] = options
    return node
