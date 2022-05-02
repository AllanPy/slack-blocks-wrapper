def checkbox_element(
        options: list,
        action_id: str,
        initial_options: list = None,
        confirm: dict = None,
        focus_on_load: bool = False
):
    """
    Works with block types: `Section`, `Actions`, `Input`
    A checkbox group that allows a user to choose multiple items from a list of possible options.
    Checkboxes are only supported in the following app surfaces: `Home tabs`, `Modals`, `Messages`

    Args:
        options (list): A list of options that can be selected by the user.
        action_id (str): The action_id of the block.
        initial_options (list, optional): A list of options that are selected when the checkbox is loaded. Defaults to None.
        confirm (dict, optional): A dictionary containing the following fields:
        focus_on_load (bool, optional): If true, the checkbox will be focused when the block is loaded. Defaults to False.
    """
    node = {
        "type": "checkboxes",
        "action_id": action_id,
        "options": options,
        "focus_on_load": focus_on_load
    }
    if initial_options:
        node["initial_options"] = initial_options
    if confirm:
        node["confirm"] = confirm
    return node
