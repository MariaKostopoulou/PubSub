# Pub/Sub System Project

Hello! 👋 Welcome to the **Pub/Sub System** project! This project is a simple implementation of a Publish-Subscribe (Pub/Sub) system, inspired by technologies like Apache Kafka and RabbitMQ. It includes three main components: the **Publisher**, **Subscriber**, and **Broker**, with shared utilities in a common module.

## Overview

In a Publish-Subscribe system, Publishers send messages on certain topics, and Subscribers listen for messages on the topics they are interested in. The Broker acts as an intermediary, routing messages from Publishers to the appropriate Subscribers based on their subscriptions.

### Components:

- **Publisher**: The Publisher is responsible for producing messages and sending them to the Broker. Each message is associated with a specific topic.
  
- **Subscriber**: The Subscriber connects to the Broker and subscribes to one or more topics. When messages are published on these topics, the Subscriber receives them.

- **Broker**: The Broker is the central component that manages all communication. It keeps track of which Subscribers are subscribed to which topics, and ensures that messages from Publishers are forwarded to the relevant Subscribers.

- **Common Module**: This module contains shared functions and utilities used by both Publishers and Subscribers to communicate efficiently with the Broker.


## Note

These files are meant to showcase how to set up a simple architecture with a Publisher, a Subscriber, and a Broker using sockets in Python. 
