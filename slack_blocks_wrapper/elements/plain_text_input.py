from typing import Literal


def plain_text_input_element(
        action_id: str,
        placeholder: str,
        initial_value: str = None,
        multiline: bool = False,
        min_length: int = None,
        trigger_actions_on: Literal[
            'on_enter_pressed', 'on_character_entered'
        ] = None,
        max_length: int = None,
        focus_on_load: bool = False,
):
    """
    Works with block types: `Input`
    A plain-text input, similar to the HTML <input> tag, creates a field where
     a user can enter freeform data. It can appear as a single-line field or a
     larger text area using the multiline flag.
     Plain-text input elements are supported in the following app surfaces:
    `Home tabs`, `Messages`, `Modals`

    Args:
        action_id(str): An identifier for the input value when the parent modal
                        is submitted
        placeholder(str): A placeholder text that appears in the input before
            the user enters a value.
        initial_value(str): The initial value for the input.
        multiline(bool): Whether the input supports multiple lines of
            text.
        min_length(int): The minimum length of the input value.
        max_length(int): The maximum length of the input value.
        focus_on_load(bool): Whether the input should be focused when
            the app loads.
        trigger_actions_on(str): What actions should dispatch the payload.
                Can be `on_enter_pressed` or `on_character_entered`

    Returns:
        dict: A plain-text input block
    Ref: https://api.slack.com/reference/block-kit/block-elements#input
    """
    if not action_id:
        raise Exception('action_id is required')
    node = {
        "type": "plain_text_input",
        "action_id": action_id,
        "placeholder": placeholder,
    }
    if initial_value:
        node['initial_value'] = initial_value
    if multiline:
        node['multiline'] = multiline
    if min_length:
        node['min_length'] = min_length
    if max_length:
        node['max_length'] = max_length
    if trigger_actions_on:
        node['dispatch_action_config'] = {
            'trigger_actions_on': trigger_actions_on
        }
    if focus_on_load:
        node['focus_on_load'] = focus_on_load
    return node
