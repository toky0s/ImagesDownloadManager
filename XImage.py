from urllib.request import urlretrieve

class XImage:

    def __init__(self, name, url, info={}):
        self.name = name
        self.url = url
        self.info = info

    def __str__(self):
        return 'XImage<{} {}>'.format(self.name, self.url)

    def getName(self):
        return self.name

    def getUrl(self):
        return self.url

    def getInfo(self):
        return self.info
