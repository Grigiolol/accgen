import aminofix as amino
import json, random, string
import requests, heroku3, secmail
from bs4 import BeautifulSoup
from time import sleep

key = "4bec1140-7843-414f-bc59-69afcb4f8b5b"
nickname = "𝐀𝐗𝐋777𝐗"
app_name = "xznv"
url = "https://AXC01.darkhanma1.repl.co"
password = "NERO777X"


def gerar_aleatorio(size=16, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def deviceId():
    return requests.get(https://cynical.gg/device).text.upper()


def restart():
    heroku_conn = heroku3.from_key(key)
    botapp = heroku_conn.apps()[app_name]
    botapp.restart()


def send(data):
    requests.post(f"{url}/save", data=data)


def codee(link):
    d = {"text": link}
    p = requests.post("https://testes0827.herokuapp.com", data=d)
    return p.json()["captcha"]


def link_codigo(email):
  try:
    mail = secmail.SecMail()
    sleep(3)
    inbox = mail.get_messages(email)
    for Id in inbox.id:
      msg = mail.read_message(email=email, id=Id).htmlBody
      bs = BeautifulSoup(msg, 'html.parser')
      images = bs.find_all('a')[0]
      url = (images['href'])
      if url is not None:
        return url
  except:
    pass
  

def gerar_email():
    email = "xnezha-" + gerar_aleatorio() + "@wwjmp.com"
    return email


for i in range(3):
    dev = deviceId()
    client = amino.Client(dev)
    # dev=client.device_id
    email = gerar_email()
    print(email)
    client.request_verify_code(email=email)
    link = link_codigo(email)
    code = codee(link)


    try:
        client.register(email=email, password=password, nickname=nickname, verificationCode=code, deviceId=dev)
        # sub.send_message(chatId=chatId,message="Criada")
        d = {}
        d["email"] = str(email)
        d["password"] = str(password)
        d["device"] = str(dev)
        t = json.dumps(d)
        data = {"data": t}
        send(data)
    except Exception as l:
        print(l)
        pass

restart()
