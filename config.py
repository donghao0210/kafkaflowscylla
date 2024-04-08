import os

TIMER = 300 # In Sec, 300 seconds = 5 minutes

# Debug =  true will show debug messages
DEBUG = True

#for Mongo Db, Unused.
NUM_MONGO_PROCESSES = 4

BATCH_SIZE = 300

TOPICS = ['topic1', 'topic2', 'topic3', 'topic4', 'topic5', 'topic6']


TOPIC_TABLE_MAPPING = {
    'topic1': 'db_table_1',
    'topic2': 'db_table_2',
    'topic3': 'db_table_3',
    'topic4': 'db_table_4',
    'topic5': 'db_table_5',
    'topic6': 'db_table_6'
}
