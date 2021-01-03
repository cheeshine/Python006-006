#!/usr/bin/env python
import socket

HOST = 'localhost'
PORT = 10001


def echo_client(file_path):
    ''' Echo Server 的 Client 端 '''

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))

    with open(file_path, 'rb') as f:

        for line in f:
            # 发送数据到服务端
            s.sendall(line)

    s.close()


if __name__ == '__main__':
    file_path = r'/home/zhixiang/workspace2021/jike_python/Python006-006/week02/NOTE.md'
    echo_client(file_path)
