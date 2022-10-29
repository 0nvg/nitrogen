import ctypes
import string
import os
import time
USE_WEBHOOK = True
time.sleep(3)
os.system('cls' if os.name == 'nt' else 'clear')
try:
    from discord_webhook import DiscordWebhook
except ImportError:
    input(
        f"Disccord Webhook modülünü indirmek için '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install discord_webhook yazın'\nWebhook kullanmak istemiyorsanız bu uyarıyı görmezden gelebilir ve enter basabilirsiniz.")
    USE_WEBHOOK = False
try:
    import requests
except ImportError:
    input(
        f"Request modülünü indirmek için '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install requests yazın'\nEnter basarak programı kapatabilirsiniz.")
    exit()
try:
    import numpy
except ImportError:
    input(
        f"Num.py modülünü indirmek için '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install numpy yazın'\nEnter basarak programı kapatabilirsiniz.")
    exit()
url = "https://github.com"
try:
    response = requests.get(url)
    print("İnternetiniz kontrol ediliyor...")
    time.sleep(.4)
except requests.exceptions.ConnectionError:
    input("İnternete bağlı değilsiniz.\nEnter basarak programı kapatabilirsiniz.")
    exit()
class NitroGen:
    def __init__(self):
        self.fileName = "kodlar.txt"
    def main(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        if os.name == "nt":
            print("")
            ctypes.windll.kernel32.SetConsoleTitleW(
                "NITROGEN - aeg#0001 - 0nvg/nitrogen")
        else:
            print(f'\33]0;Nitro Generator and Checker - Made by Drillenissen#4268\a',
                  end='', flush=True)

        print("""    ▄████████    ▄████████    ▄██████▄     ▄████████    ▄████████ ███▄▄▄▄   
  ███    ███   ███    ███   ███    ███   ███    ███   ███    ███ ███▀▀▀██▄ 
  ███    ███   ███    █▀    ███    █▀    ███    █▀    ███    ███ ███   ███ 
  ███    ███  ▄███▄▄▄      ▄███         ▄███▄▄▄       ███    ███ ███   ███ 
▀███████████ ▀▀███▀▀▀     ▀▀███ ████▄  ▀▀███▀▀▀     ▀███████████ ███   ███ 
  ███    ███   ███    █▄    ███    ███   ███    █▄    ███    ███ ███   ███ 
  ███    ███   ███    ███   ███    ███   ███    ███   ███    ███ ███   ███ 
  ███    █▀    ██████████   ████████▀    ██████████   ███    █▀   ▀█   █▀  
                                                        """)
        time.sleep(2)
        self.slowType(
            "\nKaç tane kod üretilsin: ", .02, newLine = False)
        try:
            num = int(input(''))
        except ValueError:
            input("Bir sayı girmediniz.\nEnter basarak programı kapatabilirsiniz.")
            exit()
        if USE_WEBHOOK:
            self.slowType(
                "Webhook kullanacaksanız token linkini atın, kullanmayacaksanız enter basabilirsiniz: ", .02, newLine = False)
            url = input('')
            webhook = url if url != "" else None
            if webhook is not None:
                DiscordWebhook(
                        url = url,
                        content = f"**Nitrogen bağlandı** :white_check_mark:\nGeçerli kodları buraya atacağım.\nDiscord: `aeg#0001`\nGithub: https://github.com/0nvg"
                    ).execute()
        valid = []
        invalid = 0
        chars = []
        chars[:0] = string.ascii_letters + string.digits
        c = numpy.random.choice(chars, size=[num, 16])
        for s in c:
            try:
                code = ''.join(x for x in s)
                url = f"https://discord.gift/{code}"
                result = self.quickChecker(url, webhook)
                if result:
                    valid.append(url)
                else:
                    invalid += 1
            except KeyboardInterrupt:
                print("\nProgram kullanıcı tarafından durduruldu.")
                break
            except Exception as e:
                print(f" Error | {url} ")
            if os.name == "nt":
                ctypes.windll.kernel32.SetConsoleTitleW(
                    f"0nvg/nitrogen - {len(valid)} GEÇERLİ | {invalid} GEÇERSİZ - aeg#0001")
                print("")
            else:
                print(
                    f'\33]0;0nvg/nitrogen - {len(valid)} GEÇERLİ | {invalid} GEÇERSİZ - aeg#0001"\a', end='', flush=True)
        print(f"""
Sonuç:
 {len(valid)} geçerli
 {invalid} geçersiz
 Çalışan kodlar: {', '.join(valid)}""")
        input("\n Programı kapatmak için herhangi bir tuşa basabiliriniz.")
        [input(i) for i in range(1, 0, -1)]
    def slowType(self, text: str, speed: float, newLine=True):
        for i in text:
            print(i, end = "", flush=True)
            time.sleep(speed)
        if newLine:
            print()
    def quickChecker(self, nitro: str, notify = None):
        url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"
        response = requests.get(url)
        if response.status_code == 200:
            print(f" Valid | {nitro} ", flush = True,
                  end="" if os.name == 'nt' else "\n")
            with open("kodlar.txt", "w") as file:
                file.write(nitro)
            if notify is not None:
                DiscordWebhook(
                    url = url,
                    content = f"@everyone \n{nitro}"
                ).execute()
            return True
        else:
            print(f"Invalid | {nitro} ", flush = True,
                  end = "" if os.name == 'nt' else "\n")
            return False
if __name__ == '__main__':
    Gen = NitroGen()
    Gen.main()
