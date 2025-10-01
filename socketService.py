import socket

if __name__ == '__main__':
  # 创建服务端套接字对象
  tcp_server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
  # 绑定IP地址和端口号
  # 如果bind中的参数第一个ip地址元素设置为""，默认为本机ip地址

  tcp_server_socket.bind(('',8080))
  # 设置监听128：代表服务端等待队列连接的最大数量
  tcp_server_socket.listen(128)
  # 等待接受客户端的连接请求accept阻塞等待返回一个用以和客户端通socket,客户端的地址
  conn_socket,ip_port=tcp_server_socket.accept()
  print("客户端地址：",ip_port)
  # 接收数据
  recv_data=conn_socket.recv(1024)
  print("接收到的数据：",recv_data.decode())
  #发送数据
  conn_socket.send("客户端您的数据我收到了".encode())
  print(tcp_server_socket)
  # 关闭套接字
  conn_socket.close()
  # tcp_server_socket.close() 服务端一般不关闭

  """
  设置端口号复用：
      当服务端关闭时，端口号不会立即释放，而是要等待一两分钟
      1.端口号复用
      2.更改一个新的端口号
  """
  """
  参数1：当前的Socket对象
  参数2：Reuse Address端口号重用
  参数3：True表示成立，False不成立
  """
  tcp_server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,True)