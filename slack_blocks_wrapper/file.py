def file_node(external_id: str, source: str, block_id: str = None):
    """
    Supported surfaces: `Messages`
    Displays a remote file. You can't add this block to app surfaces directly,
    but it will show up when retrieving messages that contain remote files.
    If you want to add remote files to messages, follow our guide.

    Args:
        external_id (str): The external unique ID of the file.
        source (str): The source of the file. Is always `remote`.
        block_id (str): The block ID of the file. Should be unique.
    """
    node = {
        "type": "file",
        "external_id": external_id,
        "source": source
    }
    if block_id:
        node["block_id"] = block_id
    return node
