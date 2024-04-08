from multiprocessing import Process, Queue
from config import TOPICS, NUM_MONGO_PROCESSES
from kafka_consumer import KafkaConsumer
from scylladb_processor import InsertIntoScylla

def main():
    topics = TOPICS
    message_queue = Queue()

    kafka_process = Process(target=KafkaConsumer, args=(topics, message_queue))
    kafka_process.start()
    
    scylla_processes = []
    for _ in range(NUM_MONGO_PROCESSES):
        scylla_process = Process(target=InsertIntoScylla, args=(message_queue,))
        scylla_process.start()
        scylla_processes.append(scylla_process)

    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("KeyboardInterrupt received. Stopping processes...")
        kafka_process.terminate()
        for scylla_process in scylla_processes:
            scylla_process.terminate()
            scylla_process.join()

if __name__ == "__main__":
    main()
