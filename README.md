# Slack Blocks Wrapper

Slack blocks wrapper is a python3 wrapper around the slack blocks framework. It provides a simple way to create and send blocks to slack.

## Installation

```bash
pip install slack-blocks-wrapper
```

Slack blocks wrapper has no dependencies outside python3. Currently, it is only supported and tested on python3.9.

## Usage

You can use the wrapper to create blocks in a few different ways.

Here's an example of a section with a multi-static select menu:

```python
from slack_blocks_wrapper import section, elements

multistatic_select_node = section.multi_static_select(
    text="Select a color",
    action_id="color_select",
    options=[
        elements.text_element(
            text="Red",
            text_type=elements.TextType.PLAIN_TEXT,
            value="red"
        ),
        elements.text_element(
            text="Green",
            text_type=elements.TextType.PLAIN_TEXT,
            value="green"
        ),
        elements.text_element(
            text="Blue",
            text_type=elements.TextType.PLAIN_TEXT,
            value="blue"
        )
    ]
)
```

You can use this element with the Bolt framework to create a multi-static select menu as follows:

```python
import logging
import os
from flask import Flask, request
from slack_bolt import App

from slack_bolt.adapter.flask import SlackRequestHandler
from slack_blocks_wrapper import section, elements

block_element = section.multi_static_select(
    text="Select a color",
    action_id="color_select",
    options=[
        elements.text_element(
            text="Red",
            text_type=elements.TextType.PLAIN_TEXT,
            value="red"
        ),
        elements.text_element(
            text="Green",
            text_type=section.TextType.PLAIN_TEXT,
            value="green"
        ),
        elements.text_element(
            text="Blue",
            text_type=section.TextType.PLAIN_TEXT,
            value="blue"
        )
    ]
)
app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)
bolt_app = App()
handler = SlackRequestHandler(bolt_app)


@bolt_app.command("/hello-world")
def hello(ack):
    ack(blocks=[block_element])

    
@app.route("/slack/events", methods=["POST"])
def slack_events():
    return handler.handle(request)


# Only for local debug
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 3000)))

```

Thus far, the following block kit builder elements are supported:

1. Section - All section elements are supported.
2. Actions - All action elements are supported.
3. Context - All context elements are supported.
4. Divider - All divider elements are supported.
5. Image - All image elements are supported.
6. Input - All input elements are supported.
7. Header - All header elements are supported.
8. Divider - All divider elements are supported.

Better documentation and implementation improvements are coming soon.
