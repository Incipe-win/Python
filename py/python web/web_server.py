import socket
import re
import multiprocessing
from auto import Table


class WSGIServer(object):
    def __init__(self):
        # 1. 创建套接字
        self.tcp_server_socket = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM)
        self.tcp_server_socket.setsockopt(
            socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.number_lists = []

        # 2. 绑定
        self.tcp_server_socket.bind(("0.0.0.0", 3389))

        # 3. 变为监听套接字
        self.tcp_server_socket.listen(128)

    def service_client(self, new_socket):
        """为这个客户端返回数据"""

        # 1. 接收浏览器发送过来的请求 ，即http请求
        # GET / HTTP/1.1
        # .....
        request = new_socket.recv(1024).decode("utf-8")
        # print(">>>"*50)
        # print(request)

        request_lines = request.splitlines()
        print("")
        print(">"*20)
        print(request_lines)
        file_name = ""
        data = request_lines[-1]
        rule_id = r".*?=(.*?)&.*?"
        rule_passwd = r".*?&.*?=(.*?)$"
        number_id = re.findall(rule_id, data, re.M | re.S)
        passwd = re.findall(rule_passwd, data, re.M | re.S)
        self.number_lists.append(number_id)

        if len(number_id) and len(passwd):
            file_name = "/index.html"
            if number_id not in self.number_lists:
                print("*" * 20)
                print(number_id)
                print(passwd)
                table = Table(number_id, passwd)
                table.run()
                self.number_lists.remove(number_id)
            # p = multiprocessing.Process(target=table.run)
            # p.start()
        else:
            # GET /index.html HTTP/1.1
            # get post put del
            ret = re.match(r"[^/]+(/[^ ]*)", request_lines[0])
            if ret:
                file_name = ret.group(1)
                # print("*"*50, file_name)
                if file_name == "/":
                    file_name = "/index.html"

        # 2. 返回http格式的数据，给浏览器
        try:
            f = open("./static" + file_name, "rb")
        except:
            response = "HTTP/1.1 404 NOT FOUND\r\n"
            response += "\r\n"
            response += "------file not found-----"
            new_socket.send(response.encode("utf-8"))
        else:
            html_content = f.read()
            f.close()
            # 2.1 准备发送给浏览器的数据---header
            response = "HTTP/1.1 200 OK\r\n"
            response += "\r\n"
            # 2.2 准备发送给浏览器的数据---boy
            # response += "hahahhah"

            # 将response header发送给浏览器
            new_socket.send(response.encode("utf-8"))
            # 将response body发送给浏览器
            new_socket.send(html_content)

        # 关闭套接
        new_socket.close()

    def run_forever(self):
        """用来完成整体的控制"""

        while True:
            # 4. 等待新客户端的链接
            new_socket, client_addr = self.tcp_server_socket.accept()

            # 5. 为这个客户端服务
            p = multiprocessing.Process(
                target=self.service_client, args=(new_socket,))
            p.start()

            new_socket.close()

        # 关闭监听套接字
        self.tcp_server_socket.close()


def main():
    """控制整体，创建一个web 服务器对象，然后调用这个对象的run_forever方法运行"""
    wsgi_server = WSGIServer()
    wsgi_server.run_forever()


if __name__ == "__main__":
    main()