from typing import List

from slack_blocks_wrapper.section import text_node, TextType


def multiconversations_select_element(placeholder: str, action_id: str):
    """
    Works with block types: `Section`, `Input` \n
    This multi-select menu will populate its options with a list of public and
     private channels, DMs, and MPIMs visible to the current user in the active
      workspace

    Args:
        placeholder (str): The placeholder text to be displayed in the input
        action_id (str): The action id of the input

    Returns:
        dict: The multi-conversations-select menu
    Ref: https://api.slack.com/reference/block-kit/block-elements#conversation_multi_select
    """
    return {
        "type": "multi_conversations_select",
        "placeholder": text_node(
            placeholder,
            TextType.PLAIN_TEXT, emoji=True
        ),
        "action_id": action_id
    }


def multistatic_select_element(
        placeholder: str,
        options: list,
        action_id: str,
        option_groups: list = None,
        initial_options: str = None,
        confirm: dict = None,
        max_selected_items: int = None,
        focus_on_load: bool = False
):
    """
    Works with block types: `Section`, `Input` \n
    This is the simplest form of select menu, with a static list of options
    passed in when defining the element.

    Args:
        placeholder (str): The placeholder text to be displayed in the input
        options (list): The list of options to be displayed in the select menu
        action_id (str): The action id of the input
        option_groups (list): The list of option groups to be displayed in the select menu
        initial_options (str): The initial options to be selected in the select menu
        confirm (dict): The confirm object to be displayed in the select menu
        max_selected_items (int): The maximum number of items that can be selected in the select menu
        focus_on_load (bool): Whether the select menu should be focused when it loads

    Returns:
        dict: The multi-static-select menu

    Ref: https://api.slack.com/reference/block-kit/block-elements#static_multi_select
    """
    if options and option_groups:
        raise ValueError(
            "`options` and `option_groups` cannot be used together")
    node = {
        "type": "multi_static_select",
        "placeholder": text_node(placeholder, TextType.PLAIN_TEXT),
        "options": options,
        "action_id": action_id
    }
    if option_groups:
        node["option_groups"] = option_groups
    if initial_options:
        node["initial_options"] = initial_options
    if confirm:
        node["confirm"] = confirm
    if type(max_selected_items) == int and max_selected_items > 0:
        node["max_selected_items"] = max_selected_items
    if focus_on_load:
        node["focus_on_load"] = focus_on_load
    return node


def multiexternal_select_element(
        placeholder: str,
        action_id: str,
        min_query_length: int = None,
        initial_options: str = None,
        confirm: dict = None,
        max_selected_items: int = None,
        focus_on_load: bool = False
):
    """
    Works with block types: `Section`,`Input`
    This menu will load its options from an external data source, allowing for
    a dynamic list of options.

    Args:
        placeholder (str): The placeholder text to be displayed in the input
        action_id (str): The action id of the input
        min_query_length (int): The minimum number of characters a user must type before a search is performed
        initial_options (str): The initial options to be selected in the select menu
        confirm (dict): The confirm object to be displayed in the select menu
        max_selected_items (int): The maximum number of items that can be selected in the select menu
        focus_on_load (bool): Whether the select menu should be focused when it loads

    Returns:
        dict: The multi-external-select menu

    Ref: https://api.slack.com/reference/block-kit/block-elements#external_multi_select
    """
    node = {
        "type": "multi_external_select",
        "placeholder": text_node(placeholder, TextType.PLAIN_TEXT),
        "action_id": action_id
    }
    if min_query_length:
        node["min_query_length"] = min_query_length
    if initial_options:
        node["initial_options"] = initial_options
    if confirm:
        node["confirm"] = confirm
    if type(max_selected_items) == int and max_selected_items > 0:
        node["max_selected_items"] = max_selected_items
    if focus_on_load:
        node["focus_on_load"] = focus_on_load
    return node


def multiuser_select_element(
        placeholder: str,
        action_id: str,
        initial_users: List[str] = None,
        confirm: dict = None,
        max_selected_items: int = None,
        focus_on_load: bool = False
):
    """
    Works with block types: `Section`,`Input`
    This multi-select menu will populate its options with a list of Slack users
     visible to the current user in the active workspace.

    Args:
        placeholder (str): The placeholder text to be displayed in the input
        action_id (str): The action id of the input
        initial_users (List[str]): The initial users to be selected in the select menu
        confirm (dict): The confirm object to be displayed in the select menu
        max_selected_items (int): The maximum number of items that can be selected in the select menu
        focus_on_load (bool): Whether the select menu should be focused when it loads

    Returns:
        dict: The multi-user-select menu

    Ref: https://api.slack.com/reference/block-kit/block-elements#multi_users_select
    """
    if not placeholder:
        raise ValueError("Placeholder is required")
    if not action_id:
        raise ValueError("Action ID is required")
    node = {
        "type": "multi_users_select",
        "placeholder": text_node(placeholder, TextType.PLAIN_TEXT),
        "action_id": action_id
    }
    if initial_users:
        node["initial_users"] = initial_users
    if confirm:
        node["confirm"] = confirm
    if type(max_selected_items) == int and max_selected_items > 0:
        node["max_selected_items"] = max_selected_items
    if focus_on_load:
        node["focus_on_load"] = focus_on_load
    return node


def multichannels_select_element(
        placeholder: str,
        action_id: str,
        initial_channels: List[str] = None,
        confirm: dict = None,
        max_selected_items: int = None,
        focus_on_load: bool = False
):
    """
    Works with block types: `Section`,`Input` \n
    This multi-select menu will populate its options with a list of public
     channels visible to the current user in the active workspace.

    Args:
        placeholder (str): The placeholder text to be displayed in the input
        action_id (str): The action id of the input
        initial_channels (List[str]): The initial channels to be selected in the select menu
        confirm (dict): The confirm object to be displayed in the select menu
        max_selected_items (int): The maximum number of items that can be selected in the select menu
        focus_on_load (bool): Whether the select menu should be focused when it loads

    Returns:
        dict: The multi-channels-select menu

    Ref: https://api.slack.com/reference/block-kit/block-elements#multi_channels_select
    """
    if not placeholder:
        raise ValueError("Placeholder is required")
    if not action_id:
        raise ValueError("Action ID is required")
    node = {
        "type": "multi_channels_select",
        "placeholder": text_node(placeholder, TextType.PLAIN_TEXT),
        "action_id": action_id
    }
    if initial_channels:
        node["initial_channels"] = initial_channels
    if confirm:
        node["confirm"] = confirm
    if type(max_selected_items) == int and max_selected_items > 0:
        node["max_selected_items"] = max_selected_items
    if focus_on_load:
        node["focus_on_load"] = focus_on_load
    return node
