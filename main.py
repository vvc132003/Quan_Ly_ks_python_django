# file user.py
class User:
  nation = 'VietNam'
  def __init__(self, name, age, gender, occupation):
    self.name = name
    self.age = age
    self.gender = gender
    self.occupation = occupation

  # Các hàm buy, search là những hàm phương thức.
  def buy(self, item):
    print('you bought {}'.format(item))

  def search(self, term):
    print('you search: {}'.format(term))
# file item.py
class Item:
    def __init__(self, item_id, item_name, item_price):
        self.item_id = item_id
        self.item_price = item_price
        self.item_name = item_name
# file order.py

class Order:
    def __init__(self, user, item, item_quant):
        self.user = user
        self.item = item
        self.item_quant = item_quant

    def cost(self):
        value = self.item_quant*self.item.item_price
        return value

if __name__ == '__main__':
    user = User(name='Pham Dinh Khanh', age=27, gender='male', occupation='AI Engineer')
    item = Item(item_id='123', item_name='keo vuốt tóc', item_price=50.000)
    order = Order(user=user, item=item, item_quant=2)
    total_cost = order.cost()
    print(f"{user.name} mua {item.item_name} với mã {item.item_id} với số lượng {order.item_quant} và giá mỗi cái là {item.item_price} giá tong là: {total_cost}")



