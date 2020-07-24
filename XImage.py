class XImage:

    def __init__(self, url: str):
        self.url = url

    def __str__(self):
        return 'XImage<{} {}>'.format(self.name, self.url)

    def getName(self):
        """Class inherit this class must implement this method. 
        This method returns a `str` which is Ximage's name includes `name` and `extension`.
        @example:\n
        picture.jgp"""
        pass

    def getUrl(self):
        return self.url

    def showInfo(self):
        for attr, value in self.__dict__.items():
            print(attr+': '+str(value))

class UnsplashXImage(XImage):
    NAME = 'unsplash'

    def __init__(self, url, id_ ,created_at=None, updated_at=None, promoted_at=None, width=None, height=None, description=None):
        super().__init__(url)
        self.id_ = id_
        self.created_at = created_at
        self.updated_at = updated_at
        self.promoted_at = promoted_at
        self.width = width
        self.height = height
        self.description = description

    def getName(self):
        return UnsplashXImage.NAME + '-' + self.id_ + '.jpg'

class GratisographyXImage(XImage):
    NAME = 'gratisography'
    # PATTERN = 'https://gratisography.com/wp-content/uploads/2019/08/gratisography-hairless-cat-800x525.jpg'

    def __init__(self, url):
        super().__init__(url)
        self.size = self.size()
        self.year_create = self.url[5]
        self.month_create = self.url[6]

    def getName(self):
        return self.url.split('/')[7]

    def size(self):
        return self.url.split('/')[7].split('-')[2].split('.')[0].split('x')

    

        

a = UnsplashXImage('uohnha.kpj')
print(a.name)
