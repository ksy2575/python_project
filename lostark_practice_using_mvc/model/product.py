
class Product:

    def __init__(self, name, curr_price=-1, bundle=1):
        self.name = name
        self.curr_price = curr_price
        self.bundle = bundle

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_curr_price(self):
        return self.curr_price

    def set_curr_price(self, curr_price):
        self.name = curr_price

    def get_bundle(self):
        return self.bundle

    def set_bundle(self, bundle):
        self.name = bundle
