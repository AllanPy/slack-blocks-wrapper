from typing import List, Literal

from .text import text_element, TextType


def user_select_element(
        placeholder: str,
        action_id: str,
        initial_user: str = None
):
    node = {
        "type": "users_select",
        "placeholder": text_element(placeholder, TextType.PLAIN_TEXT),
        "action_id": action_id
    }
    if initial_user is not None:
        node["initial_user"] = initial_user
    return node


def static_select_element(
        placeholder: str,
        action_id: str,
        options: list = None,
        option_groups: list = None,
        initial_option: str = None,
        confirm: dict = None,
        focus_on_load: bool = False
):
    if not action_id:
        raise ValueError("action_id is required")
    if not options and not option_groups:
        raise ValueError("options or option_groups is required")
    if options and option_groups:
        raise ValueError("options and option_groups cannot be used together")
    node = {
        "type": "static_select",
        "placeholder": text_element(placeholder, TextType.PLAIN_TEXT),
        "action_id": action_id
    }
    if options and not option_groups:
        node["options"] = options
    if option_groups and not options:
        node["option_groups"] = option_groups
    if initial_option:
        node["initial_option"] = initial_option
    if confirm:
        node["confirm"] = confirm
    if focus_on_load:
        node["focus_on_load"] = True
    return node


def external_select_element(
        placeholder: str,
        action_id: str,
        min_query_length: int = None,
        initial_option: str = None,
        confirm: dict = None,
        focus_on_load: bool = False
):
    if not placeholder:
        raise ValueError("placeholder is required")
    if not action_id:
        raise ValueError("action_id is required")
    node = {
        "type": "external_select",
        "placeholder": text_element(placeholder, TextType.PLAIN_TEXT),
        "action_id": action_id
    }
    if min_query_length:
        node["min_query_length"] = min_query_length
    if initial_option:
        node["initial_option"] = initial_option
    if confirm:
        node["confirm"] = confirm
    if focus_on_load:
        node["focus_on_load"] = True
    return node


def conversations_select_element(
        placeholder: str,
        action_id: str,
        initial_conversation: str = None,
        default_to_current_conversation: bool = False,
        confirm: dict = None,
        focus_on_load: bool = False,
        response_url_enabled: bool = False,
        filter: str = None,
):
    if not placeholder:
        raise ValueError("placeholder is required")
    if not action_id:
        raise ValueError("action_id is required")
    node = {
        "type": "conversations_select",
        "placeholder": text_element(placeholder, TextType.PLAIN_TEXT),
        "action_id": action_id
    }
    if initial_conversation is not None:
        node["initial_conversation"] = initial_conversation
    if default_to_current_conversation:
        node["default_to_current_conversation"] = True
    if confirm:
        node["confirm"] = confirm
    if focus_on_load:
        node["focus_on_load"] = True
    if response_url_enabled:
        node["response_url_enabled"] = True
    if filter:
        node["filter"] = filter
    return node


def channels_select_element(
        placeholder: str,
        action_id: str,
        initial_channel: str = None,
        confirm: dict = None,
        response_url_enabled: bool = False,
        focus_on_load: bool = False
):
    if not placeholder:
        raise ValueError("placeholder is required")
    if not action_id:
        raise ValueError("action_id is required")
    node = {
        "type": "channels_select",
        "placeholder": text_element(placeholder, TextType.PLAIN_TEXT),
        "action_id": action_id
    }
    if initial_channel is not None:
        node["initial_channel"] = initial_channel
    if confirm:
        node["confirm"] = confirm
    if focus_on_load:
        node["focus_on_load"] = True
    if response_url_enabled:
        node["response_url_enabled"] = True
    return node


def filtered_conversations_select(
        placeholder: str,
        action_id: str,
        conversations: List[Literal['im', 'mpim', 'private', 'public']] = None,
        exclude_bot_users: bool = False,
        exclude_external_shared_channels: bool = False,
        initial_conversation: str = None,
        default_to_current_conversation: bool = False,
        response_url_enabled: bool = False,
        focus_on_load: bool = False,
        confirm_text: str = None,
):
    """
    Creates a select action that will filter the conversations to be
    displayed in the list. \n

    Args:
        placeholder: The placeholder text to display in the select menu.
        action_id: The action id of the select action.
        conversations(optional): A list of conversation types to filter the list to.
        exclude_bot_users(optional): Whether to exclude bot users from the list.
        exclude_external_shared_channels(optional): Whether to exclude external shared channels from the list.
        initial_conversation(optional): The initial conversation to select.
        default_to_current_conversation(optional): Whether to default to the current conversation.
        response_url_enabled(optional): Whether to enable response URL. Only works for input elements in modals
        focus_on_load(optional): Whether to focus on the input element on load.
        confirm_text(optional): The text to display in the confirmation dialog.

    Returns:
        A filtered conversations select action.
    """
    if conversations and conversations not in [
        'im', 'mpim', 'private', 'public'
    ]:
        raise ValueError(f'conversations must be one of: im, mpim, private, '
                         f'public')
    node = {
        "type": "conversations_select",
        "placeholder": placeholder,
        "filter": {
            "include": conversations,
            "exclude_bot_users": exclude_bot_users,
            "exclude_external_shared_channels": (
                exclude_external_shared_channels
            ),
        },
        "initial_conversation": initial_conversation,
        "default_to_current_conversation": default_to_current_conversation,
        "response_url_enabled": response_url_enabled,
        "focus_on_load": focus_on_load,
        "action_id": action_id,
        "confirm": text_element(confirm_text, TextType.PLAIN_TEXT)
    }
    if (
        not conversations and not exclude_bot_users
        and not exclude_external_shared_channels
    ):
        node.pop('filter')
    if not initial_conversation:
        node.pop('initial_conversation')
    if not confirm_text:
        node.pop('confirm')
    return node
