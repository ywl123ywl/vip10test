

class washer():


    def wash(self):
        print(f'haier洗衣机的宽度是{self.width}')
        print(f'haier洗衣机的高度是{self.height}')


haier = washer()

haier.width = 500
haier.height = 800

haier.wash()