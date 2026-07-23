class Page:
    def __init__(self, val):
        self.prevP = None
        self.val = val
        self.nextP = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.homepage = Page(homepage)
        self.currentpage = self.homepage

    def visit(self, url: str) -> None:
        newpage = Page(url)
        self.currentpage.nextP = newpage
        newpage.prevP = self.currentpage

        self.currentpage = newpage

    def back(self, steps: int) -> str:
        currPage = self.currentpage
        i = 0
        while currPage:
            validPage = currPage
            if i == steps:
                self.currentpage = currPage
                return currPage.val
            currPage = currPage.prevP
            i += 1
        self.currentpage = validPage
        return validPage.val

    def forward(self, steps: int) -> str:
        currPage = self.currentpage
        i = 0
        while currPage:
            validPage = currPage
            if i == steps:
                self.currentpage = currPage
                return currPage.val
            currPage = currPage.nextP
            i += 1
        self.currentpage = validPage
        return validPage.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)