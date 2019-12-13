from .utils.connection import Connection
from .reader import Reader
from .utils.protocol import Hello, Config, Snapshot


def upload_snapshot(address: str, reader: Reader):
    """
    This function receives thought details and server address and
    sends the thought to the server

    :param reader: the reader object used for reaching different fields of the snapshot
    :param address: the server's address for example: 127.0.0.1:8888x
    """
    ip, port = address.split(':')
    for thought in reader.thoughts:
        with Connection.connect(ip, int(port)) as connection:
            # print(reader)
            hello = Hello(reader.user)
            # print(hello.serialize())
            import io
            connection.send(hello.serialize())
            config = Config.deserialize(connection.receive())
            connection.send(thought.serialize(config.fields))