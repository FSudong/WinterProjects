
from StockManage import Product
from StockManage import Stock

def addFun(s):
    print("请输入产品id：")
    id = input()
    print("请输入产品price：")
    price = input()
    print("请输入产品num：")
    num = input()
    p = Product.Product(id, price, num)
    s.addProduct(p)



if __name__ == '__main__':
    s = Stock.Stock([])
    while True:
        print("请选择功能序号：")
        print("1、添加产品； 2、计算仓库总价值； 3、退出")
        fun = input()
        # switch = {
        #     "1":addFun(s),
        #     "2":s.calValue(),
        #     "3":exit(0)
        # }
        if fun == "1":
            addFun(s)
        elif fun == "2":
            print("总价值：",s.calValue())
        elif fun == "3":
            exit(0)
