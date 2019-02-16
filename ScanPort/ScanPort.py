import sys
import socket
'''
    端口扫描器——输入某个ip地址和端口区间，程序会逐个尝试区间内的端口，如果能成功连接的话就将该端口标记为open。
'''

def get_ip_status(ip, port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server.connect((ip, port))
        print('{0} port {1} is open'.format(ip, port))
    except Exception as err:
        print('{0} port {1} is not open'.format(ip, port))
    finally:
        server.close()


if __name__ == '__main__':
    host = sys.argv[1]
    for port in range(20, 100):
        get_ip_status(host, port)