import socket

if __name__ == "__main__":
    # 创建客户端套接字对象
  tcp_client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # 和服务端套接字建立连接
    # 这里我们输入一个具体的IP
  tcp_client_socket.connect(('',8080))
    # 发送数据
  tcp_client_socket.send("您好".encode(encoding="utf-8"))
    # 接收数据recv阻塞等待数据的到来
  recv_data=tcp_client_socket.recv(1024)
  print(recv_data.decode(encoding="utf-8"))
    # 关闭客户端套接字
  tcp_client_socket.close()