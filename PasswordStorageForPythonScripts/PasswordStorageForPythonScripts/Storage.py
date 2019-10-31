import pickle, zmq, socket
from argparse import ArgumentParser
from getpass import getpass

Port = 4000

UserName = 'YourUserName' # Enter your username for connect to db

def parse_arguments():
    parser = ArgumentParser()
    parser.add_argument('-p', '--password', required=True, help="Password for connect to DB", action='store_true', dest='password',)
    args=parser.parse_args()
    if args.password:
        password = getpass()
    return password

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

def get_port():
    return Port

def run_daemon(p):
    memory = {}
    memory[UserName] = p
    Ip = get_ip()
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind('tcp://' + Ip + ':' + str(Port))
    print(f"IP: {Ip}, Port: {Port}")
    try:
        while True:
            try:
                command, key, data = pickle.loads(socket.recv())
                if command == 'set':
                    memory[key] = data
                    socket.send(b'ok')
                elif command == 'get':
                    result = memory.get(key, None)
                    socket.send(pickle.dumps(result))
            except Exception as e:
                print(e)
    except KeyboardInterrupt:
        print("Exit pressed Ctrl+C")           

if __name__ == '__main__':
    arg = parse_arguments()
    run_daemon(arg)