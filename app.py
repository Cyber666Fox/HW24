import os
from dataclasses import dataclass
from typing import Optional, List

from flask import Flask, request, abort, Response
from utils import perform_query

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")


@app.route("/perform_query/")
def query() -> Response:
    cmd_1: Optional[str] = request.args.get("cmd_1")
    value_1: Optional[str] = request.args.get("val_1")
    file_name: Optional[str] = request.args.get("file_name")
    cmd_2: Optional[str] = request.args.get("cmd_2")
    value_2: Optional[str] = request.args.get("val_2")
    if not (cmd_1, value_1, file_name):
        abort(400)

    with open(rf"{DATA_DIR}/{file_name}") as file:
        res: List[str] = perform_query(str(cmd_1), str(value_1), file)
        if cmd_2 and value_2:
            res = perform_query(str(cmd_2), str(value_2), res)
    return app.response_class(res, content_type="text/plain")


if __name__ == "__main__":
    app.run(debug=True)
