#!/usr/bin/env python3

#antuor:Alan



class Item(object):         #产品的父类
    def __init__(self, unq_id, name, price, qty):
        self.unq_id = unq_id
        self.product_name = name
        self.price = price
        self.qty = qty


class Cart(object):      #购物车
    def __init__(self):         #定义空字典
        self.content = dict()

    def update(self, item):
        if item.unq_id not in self.content:
            self.content.update({item.unq_id: item})
            return
        for k, v in self.content.get(item.unq_id).iteritems():
            if k == 'unq_id':
                continue
            elif k == 'qty':
                total_qty = v.qty + item.qty
                if total_qty:
                    v.qty = total_qty
                    continue
                self.remove_item(k)
            else:
                v[k] = item[k]

    def get_total(self):
        return sum([v.price * v.qty for _, v in self.content.items()])   #列表推导

    def get_num_items(self):
        return sum([v.qty for _, v in self.content.items()])

    def remove_item(self, key):
        self.content.pop(key)


if __name__ == '__main__':
    item1 = Item(1, "Banana", 6., 1)   #优化
    item2 = Item(2, "Eggs", 2., 5)
    item3 = Item(3, "Donut", 1., 5)
    cart = Cart()
    cart.update(item1)
    cart.update(item2)
    cart.update(item3)
    print ("You have %i items in your cart for a total of $%.02f" % (cart.get_num_items(), cart.get_total()))
    cart.remove_item(2)      #购物车编辑
    print ("You have %i items in your cart for a total of $%.02f" % (cart.get_num_items(), cart.get_total()))