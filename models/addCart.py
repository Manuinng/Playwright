from playwright.sync_api import Page
import time
class addCart:
    def __init__(self, page:Page):
        self.page = page
        self.addButton = page.locator("#add-to-cart-sauce-labs-bolt-t-shirt")
        self.cart = page.locator(".shopping_cart_link")

    def addProduct(self):
        self.addButton.click()

    def productCart(self):
        self.cart.click()
        if self.page.locator(".inventory_item_name",has_text="Sauce Labs Bolt T-Shirt").is_visible():
            print("Producto agregado")
        else:
            print("No hay productos en el carrito")