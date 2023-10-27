import datetime as dt
import requests
import json

hora_inicio = dt.datetime.now()
hora_igual = dt.datetime.now()


def comparar(var1, var2):
    if var1 == var2:
        return "são iguais"
    else:
        return "são diferentes"

def post(var1, hora_fim):
    API_ENDPOINT = "http://localhost:3000/dados"
    API_KEY = "b&&$2WoZ)1cuTEE@s2o"
    dados = {
        'key': API_KEY,
        'var': var1,
        'hora': hora_fim
    }
    r = requests.post(url=API_ENDPOINT, data=dados)
    pastebin_url = r.text
    return "The pastebin URL is:%s" % pastebin_url

while True:
    hora_fim = hora_inicio + dt.timedelta(seconds=10)
    if hora_igual.ctime() == hora_fim.ctime():
        print(comparar(var1, var2))
        hora_inicio = dt.datetime.now()
        print(post(var1, hora_fim))
    else:
        hora_igual = dt.datetime.now()
        # print(".", hora_inicio, hora_fim, hora_i
