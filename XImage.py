class XImage:

    def __init__(self, name, url):
        self.name = name
        self.url = url

    def __str__(self):
        return 'XImage<{} {}>'.format(self.name, self.url)

    def getName(self):
        return self.name

    def getUrl(self):
        return self.url

    def showInfo(self):
        for attr, value in self.__dict__.items():
            print(attr+': '+str(value))

class UnsplashXImage(XImage):

    def __init__(self, name, url, created_at, updated_at, promoted_at, width, height, description):
        super().__init__(name, url)
        self.created_at = created_at
        self.updated_at = updated_at
        self.promoted_at = promoted_at
        self.width = width
        self.height = height
        self.description = description

