import src.builder as builder
from flask import Flask

app = Flask(__name__)

@app.route("/api/plan")
def hello_world() -> None:
    markdown: str = builder.build()

    return markdown
