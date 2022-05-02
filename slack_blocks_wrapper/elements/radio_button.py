def radio_button_group_element(
        action_id: str,
        options: list,
        initial_option: object = None,
        confirm: object = None,
        focus_on_load: bool = False
):
    """
    Works with block types: `Section`, `Actions`, `Input` \n
    A radio button group that allows a user to choose one item from a list of
    possible options.

    Radio buttons are supported in the following app surfaces:
       `Home tabs`, `Modals`, `Messages`

    Args:
        action_id (str): The action_id of the block.
        options (list): A list of options for the radio button group.
        initial_option (object): The initial option that is selected.
        confirm (object): Confirmation dialog that appears when a user selects an option.
        focus_on_load (bool):Indicates whether the element will be set to auto focus within the `view object`.

    Returns:
        dict: A radio button group element.
    Ref: https://api.slack.com/reference/block-kit/block-elements#radio_button_group
    """
    if not action_id:
        raise Exception('Action ID is required')
    if not options:
        raise Exception('Options are required')
    node = {
        "type": "radio_button_group",
        "action_id": action_id,
        "options": options
    }
    if initial_option:
        node['initial_option'] = initial_option
    if confirm:
        node['confirm'] = confirm
    if focus_on_load:
        node['focus_on_load'] = focus_on_load
    return node
