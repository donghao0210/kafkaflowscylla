import json
import time
from queue import Empty
from config import TOPIC_TABLE_MAPPING, BATCH_SIZE, TIMER
from utils.db_utils import ConnectToScyllaDB
from utils.message_utils import MessageFilter
from utils.debug_utils import debug_print
from utils.log_utils import logger, insertion_logger
from cassandra.query import BatchStatement
from contextlib import contextmanager

def get_data_from_queue(queue):
    topic, data = queue.get(timeout=0.5)
    table_name = TOPIC_TABLE_MAPPING.get(topic, 'default_table_name')
    debug_print("Got data from queue: ", topic)
    logger.info(f"Got data from queue: {topic}")
    return table_name, json.loads(data)

def ProcessPayload(table_name, data):
    # data = json.loads(data)
    # after_data = data["payload"]["after"]
    # source_data = data["payload"]["source"]
    # Add timestamp column to the data
    # after_data["timestamp"] = time.time()
    #combine the data from the payload
    # after_data.update(source_data)
    debug_print("Processing payload for table: ", table_name)
    # This is an insert operation
    # columns = ", ".join(after_data.keys())
    columns = ", ".join(data.keys())
    # placeholders = ", ".join("%s" for _ in data)
    placeholders = ", ".join("?" for _ in data)
    query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
    args = list(data.values())
    return query, args

def InsertIntoScylla(queue):
    session = ConnectToScyllaDB()
    batch = BatchStatement()
    start_time = time.time()
    
    while True:
        try:
            table_name, data = get_data_from_queue(queue)
            # data = json.loads(data)
            query, args = ProcessPayload(table_name, data)
            # Prepare the statement and add it to the batch
            prepared_stmt = session.prepare(query)
            # Bind arguments with proper encoding for Chinese characters
            bound_stmt = prepared_stmt.bind(args)
            # Bind arguments with proper encoding for Chinese characters
            bound_stmt.encoding = "utf-8"
            debug_print(f"Bound statement: {bound_stmt}")
            batch.add(bound_stmt)
            # If the batch has reached a certain size or the time limit has been reached, execute it and start a new batch
            if len(batch) >= BATCH_SIZE or time.time() - start_time >= TIMER:  # Set BATCH_SIZE and TIME_LIMIT to suitable values
                session.execute(batch)
                insertion_logger.info(f"Inserted data into ScyllaDB")
                batch = BatchStatement()
                start_time = time.time()

        except Empty:
            continue
        except Exception as e:
            logger.error(f"Error while executing query: {e}")
            debug_print(f"Error while executing query: {e}")

        # Execute any remaining statements in the batch
        if len(batch) > 0:
            session.execute(batch)

@contextmanager
def get_session():
    session = ConnectToScyllaDB()
    try:
        yield session
    finally:
        session.shutdown()