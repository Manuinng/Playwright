from playwright.sync_api import Page

class Logout:
    def __init__(self, page:Page):
        self.page = page
        self.openMenu = page.locator("#react-burger-menu-btn")
        self.LogOutButton = page.locator("#logout_sidebar_link")

    def logOut(self):
        self.openMenu.click()
        self.LogOutButton.click()