from models.Login import Login
from models.addCart import addCart
from models.Logout import Logout
from playwright.sync_api import sync_playwright

URL = "https://www.saucedemo.com"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page =  browser.new_page()
    page.goto(URL, wait_until="domcontentloaded")

    #Inicio sesion
    login = Login(page)
    login.logIn()

    #Seleccion de producto y agregar carrito(comprobacion de producto en carrito)
    addcart = addCart(page)
    addcart.addProduct()
    addcart.productCart()

    #Cerrar Sesion
    logout = Logout(page)
    logout.logOut()

    browser.close()
