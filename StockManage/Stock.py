from StockManage import Product

class Stock:

    productList = []
    allvalue = 0.0
    def __init__(self, list):
        if len(list) == 0:
            self.productList = []
        self.productList = list

    def addProduct(self, product):
        self.productList.append(product)

    def calValue(self):
        if len(self.productList) == 0:
            return 0.0
        value = 0.0
        for item in self.productList:
            value = value + float(item.price) * float(item.num)
        self.allvalue = value
        return value