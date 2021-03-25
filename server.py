from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import unquote
import re
from bandit import a

Cookie = "fghfghgdfhfdhdfhfdhery5eyh5jh67j677j6yh467h64uyh46jh6j467j6j6"

Tasks = ["Помыть собаку", "Поесть", "Купить тесто"]
Result = [" "]

class requestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.endswith('/mytasks'):
            #print(self.headers)
            self.send_response(200)
            self.send_header("content-type", "text/html")
            #self.send_header("set-Cookie", Cookie)
            self.end_headers()
            output = '<html><body>'
            output +='<h1>Список задач</h1>'

            for i in Tasks:

                output +='<h2>'+i+'</h2>'

            output += '<a class="btn-create-task" href="/new" a>Редактор Задач</a>'
            output += '<a class="btn-create-task" type="button">'
            output += '</body></html>'
            output += ' '
            output += '<a class="btn-create-task" href="/calculate" a>Кривой калькулятор</a>'
            output += '<a class="btn-create-task" type="button">'
            output += ' '
            output += '<a class="btn-create-task" href="/sqlinjection" a>SQL-injection</a>'
            output += '<a class="btn-create-task" type="button">'
            self.wfile.write(output.encode("cp1251"))

        if self.path.endswith('/new'):
            self.send_response(200)
            self.send_header("content-type", "text/html")
            #self.send_header("set-Cookie", Cookie)
            self.end_headers()
            output = '<html><body>'
            output += '<h1>Добавить задачу</h1>'

            output += '<form method="POST" action="/new" >'
            output += '<input name="task" placeholder="Добавить новую задачу">'
            output += '<input type="submit" value="Добавить новую задачу">'
            output += '</form>'
            output += '</body></html>'
            self.wfile.write(output.encode("cp1251"))

        if self.path.endswith('/sqlinjection'):
            self.send_response(200)
            self.send_header("content-type", "text/html")
            # self.send_header("set-Cookie", Cookie)
            self.end_headers()
            output = '<html><body>'
            output += '<h1>Выберите пользователя</h1>'

            output += '<form method="POST" action="/sqlinjection" >'
            output += '<input name="User" placeholder="Показать">'
            output += '<input type="submit" value="Показать пользователя">'
            output += '</form>'
            output += '</body></html>'
            self.wfile.write(output.encode("cp1251"))

        if self.path.endswith('/calculate'):
            self.send_response(200)
            self.send_header("content-type", "text/html")
            # self.send_header("set-Cookie", Cookie)
            self.end_headers()
            output = '<html><body>'
            output += '<h1>Сумма двух чисел</h1>'

            output += '<form method="POST" action="/calculate" >'
            output += '<input name="one" placeholder="Введите целое число">'
            output += '<input name="two" placeholder="Введите целое число">'
            output += '<input type="submit" value="Рассчитать">'
            output += '<h2>'+Result[-1]+'</h2>'
            output += '</form>'
            output += '</body></html>'
            self.wfile.write(output.encode("cp1251"))


        if self.path.endswith('/admin'):
            self.send_response(200)
            self.send_header("content-type", "text/html")
            # Session = self.headers.get('Session')
            # Cookie= self.headers.get('Cookie')
            # if isadnmin(Cookie, Session) = True
            self.end_headers()
            output = '<html><body>'
            output += '<h1>Добро пожаловать в админ панель, разработчик забыл раскоментить функцию проверки кук:( </h1>'

            output += '<input name="password" placeholder="Введите новый пароль">'
            output += '<input type="submit" value="Сменить">'
            output += '</form>'
            output += '</body></html>'
            self.wfile.write(output.encode("cp1251"))



    def do_POST(self):
        if self.path.endswith('/new'):
            print(self.headers)
            content_len = int(self.headers.get('content-length'))
            post_body = self.rfile.read(content_len)
            x = re.split("task=",(post_body.decode("utf-8")))
            print(x[-1])
            Tasks.append(unquote(x[-1]))
            self.send_response(301)
            self.send_header("content-type", "text/html")
            self.send_header("Location", "/mytasks")
            self.end_headers()

        if self.path.endswith('/sqlinjection'):
            content_len = int(self.headers.get('content-length'))
            post_body = self.rfile.read(content_len)
            x = re.split("User=", (post_body.decode("utf-8")))
            SQL = "select" + " "+ x[-1] +" " +  "from USERS"
            print(SQL)
            self.send_response(301)
            self.send_header("content-type", "text/html")
            self.send_header("Location", "/mytasks")
            self.end_headers()

        if self.path.endswith('/calculate'):
            content_len = int(self.headers.get('content-length'))
            post_body = self.rfile.read(content_len)
            x = (post_body.decode("utf-8"))
            x = re.split("&", x)
            one = unquote(re.split("one=", x[0])[-1])
            two = unquote(re.split("two=", x[1])[-1])
            print(one, two)
            self.send_response(301)
            self.send_header("content-type", "text/html")
            self.send_header("Location", "/calculate")
            self.end_headers()
            x =eval(one + " + " + two)
            Result.append('<h2>'+str(x)+'</h2>')
            # print(output)
            # self.sen






server_address = ("localhost", 8081)

httpd = HTTPServer(server_address, requestHandler)

httpd.serve_forever()
