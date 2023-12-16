from asyncio import sleep

from requests_html import HTMLSession, AsyncHTMLSession

url = "https://www.pccomponentes.com/zotac-gaming-geforce-rtx-3060-twin-edge-lhr-12gb-gddr6"
url_coolmod = "https://www.coolmod.com/msi-gf65-thin-10ue-035xes-i5-10200h-rtx-3060-max-q-16gb-512gb-nvme-freedos-156-144hz-portatil-precio"

def stock():

    session = HTMLSession()
    hay_stock = False
    while hay_stock == False:
        r = session.get(url)
        buy_zone = r.html.find("#btnsWishAddBuy")
        if len(buy_zone) > 0:
            print("Hay stock")
            hay_stock = True
            return hay_stock
        else:
            print("Sigue sin haber stock")

        sleep(30)

def stock_2():
    pass



def main():
    x=stock()
    print(x)
if __name__ == "__main__":
    main()

