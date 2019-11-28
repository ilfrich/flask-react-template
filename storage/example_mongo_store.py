from pbu import AbstractMongoStore


class Example:
    """
    Object class representing a document in this database collection.
    """

    def __init__(self):
        self.field_a = None
        self.field_b = None
        self.id = None

    def to_json(self):
        """
        Serialises the current instance into JSON
        :return: a dictionary containing the fields and values of this instance
        """
        result = {}
        if self.field_a is not None:
            result["fieldA"] = self.field_a
        if self.field_b is not None:
            result["fieldB"] = self.field_b
        if self.id is not None:
            result["_id"] = self.id
        return result

    @staticmethod
    def from_json(json):
        """
        Method to de-serialise a row from a JSON object
        :param json: the JSON object represented as dictionary
        :return: a representation of a row object
        """
        result = Example()
        if "fieldA" in json:
            result.field_a = json["fieldA"]
        if "fieldB" in json:
            result.field_b = json["fieldB"]
        if "_id" in json:
            result.id = json["_id"]
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
