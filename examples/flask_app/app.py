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
app = Flask(__name__)
bolt_app = App()
handler = SlackRequestHandler(bolt_app)


@bolt_app.command("/hello")
def hello(ack):
    print(block_element)
    ack(blocks=[block_element])


@app.route("/hello", methods=["POST"])
def welcome():
    return handler.handle(request)


@app.route("/slack/events", methods=["POST"])
def slack_events():
    return handler.handle(request)


# Only for local debug
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)
