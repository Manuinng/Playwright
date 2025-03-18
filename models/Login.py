from playwright.sync_api import Page

class Login:
    def __init__(self, page:Page):
        self.page = page
        self.username = page.locator("#user-name")
        self.password = page.locator("#password")
        self.LogInButton = page.locator("#login-button")

    def logIn(self):
        self.username.fill("standard_user")
        self.password.fill("secret_sauce")
        self.LogInButton.click()
        try:
            self.page.locator("#inventory_container").first.wait_for(state="visible", timeout=5000)
            print("Ingreso Exitoso")
        except Exception:
            print("Error en el inicio de sesión")