import random
from io import BytesIO

from requests_html import HTMLSession
from Speak_and_Listen import speak, hear_me
from PIL import Image

def hear_price_and_get_number():
    while True:
        try:
            price = hear_me()
            price = price.replace(" $", "").replace(",", ".").replace(" con ", ".")
            final_price = float(price)
            print(price)
            return final_price
        except ValueError:
            speak("No te he entendido, repite ")

def get_pccom_categories(session):
    main_site = session.get("https://www.coolmod.com/")
    categories = main_site.html.find("leftmenufamily")
    return categories

def get_random_product_atributtes(session,categories):
    category = random.choice(categories)
    while category.text == "Configurador de PCs":
        category = random.choice(categories)
    product_page = session.get(category.attrs["href"])
    products = product_page.html.find(".c-product-card_wrapper")

    product = random.choice(products)
    image_src = product.find(".c-product-card__image", first=True).attrs["src"]
    product_name = product.find(".c-product-card__tittle", first=True).text
    product_price = product.find(".c-product-card__prices-actual", first=True).text

    final_price = (float(product_price.replace("$", "").replace(",", ".")))

    return image_src,product_name,final_price


def show_image(session, image_src):
    img = session.get("htps:" + image_src)
    image = Image.open(BytesIO(img))
    image.show()


def main():
    session = HTMLSession()
    speak("Bienvenido al precio justo, vamos a intentar adivinar los precios de algunos productos")
    categories = get_pccom_categories()
    image_src, product_name, final_price = get_random_product_atributtes(session,categories)
    speak("El nombre del producto es {}, cuanto crees que vale?".format(product_name))
    show_image(session,image_src)
    print(product_name)
    user_guess = hear_price_and_get_number()
    speak("El precio era {}".format(final_price))


if __name__ == "__main__":
    get_random_product_atributtes()
    hear_price_and_get_number()