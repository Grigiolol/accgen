password = "NEZHA777X"  # <---Mude a senha

import requests, random, string, secmail, pyshorteners, names, json, os
from aminofix import Client
from bs4 import BeautifulSoup
from time import sleep
from aminofix.lib.util.helpers import deviceId
from aminofix.lib.util.exceptions import ActionNotAllowed, IncorrectVerificationCode, ServiceUnderMaintenance
from pyfiglet import figlet_format
from flask import Flask
import heroku3

abertura = figlet_format("a c c g e n  X\n       p t - b r")
print(abertura)

key_api_heroku = "7d4a347f-f3f0-47b8-b1f0-7f365aa03f05"
nome_aplicativo = "xmega"


# ===============Funções==================
def restart():
    heroku_conn = heroku3.from_key(key_api_heroku)
    botapp = heroku_conn.apps()[nome_aplicativo]
    botapp.restart()


def nome_aleatorio():
    nome = '𝕯𝐄𝐕𝐈𝐋𝐗'
    for i in names.get_first_name():
        nome += i
    return nome


def api(url):
    return requests.post("https://captcha-xmega11.herokuapp.com/", data={"text": url}).json()['captcha']


def deviceId():
    return deviceId()


def gerar_aleatorio(size=16, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def gerar_email():
    email = "devil-" + gerar_aleatorio() + "@wwjmp.com"
    return email


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


def encurtar_link(link):
    ps = pyshorteners.Shortener()
    return ps.tinyurl.short(fr"{link}")


def salvar(data):
    requests.post("https://XMEGA.ghosthanma.repl.co", data=data)


# ==================Gerador=============================
print("=" * 60)
print("                                  accgen X Heroku 24/7")
print("=" * 60)

app = Flask(__name__)


@app.route('/', methods=["POST", "GET"])
def home():
    while True:
        contador = 0
        try:
            with open("device.json", "w") as f:
                f.close()

            client = Client()
            email = gerar_email()
            nickname = nome_aleatorio() + '⁹⁹⁹'
            print(f"\nGerando email {email}")
            client.request_verify_code(email=email)
            link = encurtar_link(link_codigo(email))
            codigo = api(link)
            # codigo = input("[\033[1;37mCódigo\033[m]: ")
            # slk = api(link)

            device = deviceId()
            client.register(nickname, email, password, codigo, device)
            client.login(email=email, password=password)
            # client.join_community("83401311")  # <----- Sua cid da comunidade
            # img = urlopen(f"{link}").read()
            # open(f"G:/AMINO COINS/FOLLOW/bd_captcha/{codigo}.png", "wb").write(img)

            contador += 1

            d = {
                "email": str(email),
                "password": str(password),
                "device": str(device)
            }

            j = json.dumps(d)
            data = {'data': j}
            salvar(data)
            print("Conta salva!")

        except ActionNotAllowed:
            # print("\n[\033[1;31mAtenção\033[m] \033[1;33mLimite de contas criadas atingido, mude o VPN!\033[m")
            restart()

        except IncorrectVerificationCode:
            # print("\n[\033[1;31mAtenção\033[m] \033[1;33mVocê digitou o código errado, reinicie o script!\033[m")
            restart()

        except ServiceUnderMaintenance:
            # print("\n[\033[1;31mAtenção\033[m] \033[1;33mParece que o serviço está em manutenção, tente mais tarde!")
            restart()

        except:
            # print("\n[\033[1;31mAtenção\033[m] \033[1;33mErro desconhecido, tente reiniciar o script!")
            restart()


def main():
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)


if __name__ == "__main__":
    home()
