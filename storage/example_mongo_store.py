from pbumongo import AbstractMongoStore
from pbu import JsonDocument


class Example(JsonDocument):
    """
    Object class representing a document in this database collection.
    """

    def __init__(self):
        super().__init__()
        self.field_a = None
        self.field_b = None

    def get_attribute_mapping(self) -> dict:
        return {
            "field_a": "fieldA",
            "field_b": "fieldB",
        }

    @staticmethod
    def from_json(json):
        """
        Method to de-serialise a row from a JSON object
        :param json: the JSON object represented as dictionary
        :return: a representation of a row object
        """
        result = Example()
        result.extract_system_fields(json)
        return result


class ExampleStore(AbstractMongoStore):
    """
    Database store representing a MongoDB collection
    """
    def __init__(self, mongo_url, mongo_db, collection_name):
        super().__init__(mongo_url, mongo_db, collection_name, Example, 1)

    def get_by_field_a(self, field_a_value):
        """
        Fetches all documents matching the provided field value for fieldA / field_a
        :param field_a_value: the query value to search for
        :return: a list of object instances of Example
        """
        return self.query({
            "fieldA": field_a_value,
        })
