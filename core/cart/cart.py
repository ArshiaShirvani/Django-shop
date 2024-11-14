from shop.models import ProductModel,ProductStatusType
from cart.models import CartModel,CartItemsModel

class CartSession:
    def __init__(self, session):
        self.session = session
        self._cart = self.session.setdefault("caer",
        {
            "items":[],
            "total_price":0,
            "total_items":0
        })

    def add_product(self,product_id):
        for item in self._cart["items"]:
            if product_id == item["product_id"]:
                item["quantity"] +=1
                break
        else:
            new_item = {
                "product_id":product_id,
                "quantity":1,
            }
            self._cart["items"].append(new_item)
        self.save()

    def get_cart_dict(self):
        return self._cart["items"]
    
    def get_total_quantity(self):
        # if you want return number of quantity in cart
        total_quantity = 0
        for item in self._cart["items"]:
            total_quantity += item["quantity"]
        return total_quantity

        # if you want return number of items in cart
        # total_items = 0
        # total_items = len(self._cart["items"])
        # return total_items

    def clear(self):
        self._cart = self.session["cart"] = {
            "items":[],
            "total_price": 0,
            "total_items": 0
        }
        self.save()

    def save(self):
        self.session.modified = True