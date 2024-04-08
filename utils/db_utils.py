from pymongo import MongoClient
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import pymongo
import yaml

def LoadConfig(file_path):
    with open(file_path, 'r') as stream:
        try:
            config = yaml.safe_load(stream)
            return config
        except yaml.YAMLError as exc:
            print(exc)
            return None

# def ConnectToMongodb():
#     config = LoadConfig("config.yml")
#     if config is None:
#         return None

#     try:
#         host = config['mongodb']['host']
#         port = config['mongodb']['port']
#         username = config['mongodb']['username']
#         password = config['mongodb']['password']
#         # Construct connection string
#         connection_string = f"mongodb://{username}:{password}@{host}:{port}/"
#         database_name = config['mongodb']['database_name']
#         return MongoClient(connection_string)[database_name]
#     except KeyError as e:
#         print(f"Configuration error: {e} key is missing.")
#         return None
    # except pymongo.errors.ConnectionFailure as e:
    #     print("Could not connect to MongoDB: %s" % e)
    #     return None


def ConnectToScyllaDB():
    # auth_provider = PlainTextAuthProvider(username='your_username', password='your_password')
    # cluster = Cluster(['127.0.0.1'], auth_provider=auth_provider)
    cluster = Cluster(['127.0.0.1'])
    session = cluster.connect()
    session.set_keyspace('db')

    return session