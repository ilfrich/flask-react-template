from flask import Flask
# TODO: clean up unused imports
from pbu import Logger, MysqlConnection
from config import load_config, get_log_folder, get_mongodb_config, get_mysql_config
from storage.example_mongo_store import ExampleStore as ExampleMongoStore
from storage.example_mysql_store import ExampleStore as ExampleMysqlStore
import api.static_api as static_api
import api.example_api as example_api

if __name__ == "__main__":
    logger = Logger("MAIN", log_folder=get_log_folder())
    logger.info("==========================================")
    logger.info("           Starting application")
    logger.info("==========================================")

    # load config from .env file
    config = load_config()

    # ---- database and stores ----

    # create mysql connection (TODO: remove this block or uncomment)
    # host, db, username, password = get_mysql_config()
    # con = MysqlConnection(host, db, username, password)

    # fetch mongo config (TODO: remove this block or uncomment)
    mongo_url, mongo_db = get_mongodb_config()

    # initialise stores # TODO: add stores here and remove examples
    stores = {
        # "mysql_example": ExampleMysqlStore(connection=con, table_name="example"),
        "mongo_example": ExampleMongoStore(mongo_url=mongo_url, mongo_db=mongo_db, collection_name="examples"),
    }

    # create flask app
    app = Flask(__name__)
    # register endpoints
    static_api.register_endpoints(app)
    # TODO: replace this with your (multiple) API registrations
    example_api.register_endpoints(app, stores)

    # start flask app
    app.run(host='0.0.0.0', port=5555, debug=config["IS_DEBUG"])
