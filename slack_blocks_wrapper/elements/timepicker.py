from slack_blocks_wrapper.section import text_node, TextType


def timepicker_element(
        placeholder: str,
        action_id: str,
        initial_time: str = None,
        confirm: object = None,
        focus_on_load: bool = False
):
    if not placeholder:
        raise ValueError("Placeholder is required")
    if not action_id:
        raise ValueError("Action ID is required")
    node = {
        "type": "timepicker",
        "placeholder": text_node(placeholder, TextType.PLAIN_TEXT),
        "action_id": action_id
    }
    if initial_time:
        node["initial_time"] = initial_time
    if confirm:
        node["confirm"] = confirm
    if focus_on_load:
        node["focus_on_load"] = focus_on_load
    return node
