from playwright.sync_api import Page

class NumeralRefPage:

    def __init__(self, page: Page):
        self.page = page

    def numeral_ref(self, inputnumber):
        url = "https://www.knowtheromans.com/roman-numerals/"
        self.page.goto(url)
        self.page.fill("#convertnumeralinput", str(inputnumber))
        outputnumber = self.page.inner_html("#numeralsout").strip("\n")
        return str(outputnumber)
