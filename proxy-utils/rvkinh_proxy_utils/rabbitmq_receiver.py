import threading
import pika
from rvkinh_proxy_message_protocol import RabbitmqConfig


class RabbitmqReceiver:
    def __init__(self, rabbitmq_config: RabbitmqConfig, channel_name: str, debug: bool = False):
        self.rabbitmq_config = rabbitmq_config
        self.channel_name = channel_name
        self.message = None
        self.message_event = threading.Event()
        self.debug = debug

    def callback(self, channel, method, properties, body) -> None:
        # If the event is still not completed
        if not self.message_event.is_set():
            channel_name = method.routing_key
            if self.debug:
                print('RabbitmqReceiver.callback(): Started on channel [' + channel_name + ']')
            message = str(body.decode())
            channel.basic_ack(delivery_tag=method.delivery_tag)

            # If valid message was found - save it and emit the event
            if message is not None:
                if self.debug:
                    print('RabbitmqReceiver.callback(): Valid message found on channel [' + channel_name + ']')
                self.message = message
                self.message_event.set()

            if self.debug:
                print('RabbitmqReceiver.callback(): Ended on channel [' + channel_name + ']')

    def receive(self, timeout_in_seconds: float = 5.0) -> str:
        credentials = pika.PlainCredentials(self.rabbitmq_config.username, self.rabbitmq_config.password)
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.rabbitmq_config.host, port=self.rabbitmq_config.port, credentials=credentials))
        channel = connection.channel()
        channel.queue_declare(queue=self.channel_name)
        channel.basic_consume(queue=self.channel_name, auto_ack=False, on_message_callback=self.callback)

        # Start listener in a separate thread
        thread = threading.Thread(target=channel.start_consuming, args=[])
        thread.start()
        print('RabbitmqReceiver.receive(): Channel ' + str(self.channel_name) + ' started listener in new thread')

        # Wait till the results are obtained
        self.message_event.wait(timeout_in_seconds)

        # Gracefully kill channel
        try:
            channel.stop_consuming()
            connection.close()
        except:
            pass
        finally:
            thread.join(1)
        print('RabbitmqReceiver.receive(): Channel ' + str(self.channel_name) + ' ended listener, and closed thread')

        # Return message
        return self.message
