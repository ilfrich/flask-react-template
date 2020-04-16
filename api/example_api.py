from flask import jsonify, request
from pbu import list_to_json
from storage.example_mongo_store import Example

# TODO: this is just an example. You should delete this file and remove it from the `runner.py` as well


def register_endpoints(app, stores):

    # extract stores for API endpoints (mongo_example is just for illustration)
    example_store = stores["mongo_example"]

    @app.route("/api/examples", methods=["GET"])
    def get_examples():
        return jsonify(list_to_json(example_store.get_all()))

    @app.route("/api/examples", methods=["POST"])
    def create_example():
        body = request.get_json()
        instance = Example.from_json(body)
        example_store.create(instance)
