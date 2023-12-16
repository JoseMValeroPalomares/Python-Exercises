import random
import urllib3
from io import BytesIO
from time import sleep
from PIL import Image
from requests_html import HTMLSession
from Speak_and_Listen import speak, hear_me
urllib3.disable_warnings()


def hear_price_and_get_number():
    while True:
        try:
            price = hear_me()
            price = price.replace(" €", "").replace(",", ".").replace(" con ", ".").replace("$", "")\


            final_price = float(price)
            return final_price
        except ValueError:
            speak("No te he entendido, repite")


def get_categories(session):
    main_site = session.get("https://tiendamia.com/ec/")
    categories = main_site.html.find("#level_4")

    list_categories = []
    for a in range(len(categories)):
        list_categories.append(categories[a].text.split("\n")[0])

    sorteo = []
    while len(sorteo) < 5:
        sorteo1 = list_categories[random.randint(0, len(list_categories))]
        if sorteo1 not in sorteo:
            sorteo.append(sorteo1)

    tr = []
    for categ in sorteo:
        b = categories[list_categories.index(categ)]
        tr.append(b)

    print("Las categorias que se juegan son {}".format(tr))
    return tr


def get_random_product_attributes(session, categories):

    category = random.choice(categories)

    # Escogiendo una categoria al azar y extrayendo el link
    url = list(category.absolute_links)[0]
    product_page = session.get(url)
    print(url)
    # Escoger un link al azar
    # Buscando un producto al azar
    products = product_page.html.find(".item.span3")
    product = random.choice(products)
    # Extrayendo nombre, precio e imagen
    image_src = product.find(".product-image", first=True).html.split("src=").pop(-1).replace('"', '').\
        replace("/>\n</a", "").replace(">", "")
    image_src = image_src
    product_name = product.text.split("\n")[0]
    product_price = float(product.find(".dollar_price.notranslate.price-tachado", first=True).text.replace("U$S ", ""))
    print(product_name)
    return image_src, product_price, product_name


def play_game(session, categories):
    image_src, product_price, product_name = get_random_product_attributes(session, categories)
    speak("El nombre del producto es {}".format(product_name))
    get_image(session, image_src)
    sleep(2)
    speak("Turno del jugador 1")
    sleep(2)
    speak("Cuanto crees que vale?")
    user_guess_1 = hear_price_and_get_number()
    speak("Turno del jugador 2")
    sleep(2)
    speak("Cuanto crees que vale?")
    user_guess_2 = hear_price_and_get_number()

    delta_1 = abs(user_guess_2 - product_price)
    delta_2 = abs(user_guess_1 - product_price)

    puntaje_1 = 0
    puntaje_2 = 0

    if delta_2 > delta_1:
        puntaje_2 += 5
    else:
        puntaje_1 += 5

    speak("El precio es {}".format(product_price))
    return puntaje_1, puntaje_2


def get_image(session, image_scr):
    img_downloaded = session.get(image_scr, verify=False)
    image = Image.open(BytesIO(img_downloaded.content))
    image.show()


def rounds(session, categories):
    puntaje_1t = 0
    puntaje_2t = 0

    for a in range(3):
        puntaje_1, puntaje_2 = play_game(session, categories)
        puntaje_1t += puntaje_1
        puntaje_2t += puntaje_2
        input("Presione Enter para continuar...")

    print("El puntaje del jugador 1 es {} y del jugador 2 es {}".format(puntaje_1t, puntaje_2t))
    return puntaje_1t, puntaje_2t


def main():
    session = HTMLSession()

    speak("Bienvenido al precio justo, intentaremos adivinar los precios de algunos componentes")

    categories = get_categories(session)

    puntaje_1t, puntaje_2t = rounds(session, categories)

    if puntaje_1t > puntaje_2t:
        print("El jugador 1 ha ganado!")
    else:
        print("El jugador 2 ha ganado!")


if __name__ == "__main__":
    main()