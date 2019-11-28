from pbu import AbstractMysqlStore
from pkg_resources import resource_string

'''
SQL statements:
- NOTE: table names remain placeholders '{}' in the query and get replaced by the `run_invoke` or `run_query` method
'''
_GET_STATEMENT_FIELDS = "select id, field_a, field_b from {} "
_GET_BY_FIELD_A = "{} where field_a = %s".format(_GET_STATEMENT_FIELDS)
_CREATE_EXAMPLE = "insert into {} (field_a, field_b) values (%s, %s)"


class Example:
    """
    Object class representing rows in this database table.
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
            result["id"] = self.id
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
        if "id" in json:
            result.id = json["id"]
        return result


class ExampleStore(AbstractMysqlStore):
    """
    Store instance representing this database table
    """

    def __init__(self, connection, table_name):
        """
        Creates a new instance of this data store
        :param connection: the mysql connection
        :param table_name: the name of the database table to use
        """
        super().__init__(connection, table_name, Example)
        definition = resource_string("storage.resources.tables", "example.sql")
        self.check_exists(definition)

    def create(self, example):
        """
        Creates a new row in the table and returns the new ID (primary key) of the new row
        :param example: an instance of Example
        :return: a number representing the primary key of the newly created row
        """
        return self.run_invoke(_CREATE_EXAMPLE, (example.field_a, example.field_b))

    def get_by_field_a(self, field_a_value):
        """
        Runs a query against the database and returns the result with each row de-serialised into an Example instance
        :param field_a_value: the query value to search for
        :return: a list of Example instances
        """
        return self.run_query(_GET_BY_FIELD_A, (field_a_value, ), ExampleStore.extract_row)

    @staticmethod
    def extract_row(row):
        """
        De-serialises a MySQL row result into an object instance representing this row.
        :param row: a mysql row result (list)
        :return: an instance of the Example class representing a row
        """
        result = Example()
        result.id = row[0]
        result.field_a = row[1]
        result.field_b = row[2]
        return result
