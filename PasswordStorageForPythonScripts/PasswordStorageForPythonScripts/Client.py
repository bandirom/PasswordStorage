import zmq
import pickle

class SuperCacher:
    def __init__(self, ip, port):
        self.Ip = ip
        self.Port = port
        self.__Connect()

    def __Connect(self):
        context = zmq.Context()
        self.socket = context.socket(zmq.REQ)
        try:
            self.socket.connect('tcp://' + self.Ip + ':' + str(self.Port))
        except:
            print("Cannot get access to ZMQ server")
            print('Please, check is ZMQ server script running?')
        finally:
            print(f"IP: {self.Ip}, Port: {self.Port}")

    def get(self, key):
        self.socket.send(pickle.dumps(('get', key, None)))
        return pickle.loads(self.socket.recv())

    def set(self, key, data):
        self.socket.send(pickle.dumps(('set', key, data)))
        return self.socket.recv() == b'ok'


if __name__ == '__main__':
    cacher = SuperCacher('127.0.0.1', 4000)
    cacher.set('key', 'value')
    cacher.set('first', False)
    print(cacher.get('key'))
    print(cacher.get('first'))