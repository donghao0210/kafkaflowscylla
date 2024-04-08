# KafkaFlowDB

## Overview

 This is a Python application designed to consume messages from Kafka topics, process them, and then store the data into syclla database tables. It is particularly useful in scenarios where data streaming from Kafka to syclla database.

## Features

- **Kafka Message Consumption**: The application utilizes the `confluent_kafka` library to consume messages from Kafka topics efficiently.
- **Flexible Configuration**: The application is configurable via a `config.yml` file, allowing easy customization of Kafka connection settings and other parameters.

## Getting Started

1. **Setup**: Ensure that Python 3.11 or higher and Scylla DB are setup.
2. **Install Dependencies**: Install the required Python dependencies by running `pip install -r requirements.txt`.
3. **Configuration**: Update the `config.yml` file with your Kafka connection settings and other configuration parameters.
4. **Database Setup**: Docker compose `docker-compose.yml` to start your local scylla DB, then create tables according to your topics.
5. **Run the Application**: Execute the `main.py` script to start consuming messages from Kafka and storing them into Scylla database tables.

## Configuration

`config.yml` file contains the following configuration parameters:

`db_utils`: MySQL database connection settings, db's utilities

`constants.py` Includes Threshold limit config for the message in lines. Debug settings.

## Usage

```bash
python main.py
