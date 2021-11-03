from models.items import Item
from models.orders import *
from models.items import *
import datetime

item_1 = Item("A01", "MacBook Pro")
item_2 = Item("L15", '28" LED Screen')
item_3 = Item("P52", "Blutooth headset")
item_4 = Item("Z99", "USB hub")
item_5 = Item("I12", "iPhone 13")
item_6 = Item("K69", "wireless keyboard")

order_1_items = {
    item_1 : 10,
    item_2 : 2,
    item_6 : 2
}
order_2_items = {
    item_1 : 1,
    item_2 : 1,
    item_4 : 1,
    item_3 : 1,
    item_6 : 1
}
order_3_items = {
    item_5 : 1,
    item_3 : 1
}
order_4_items = {
    item_1 : 10,
    item_2 : 2,
    item_6 : 2,
    item_3 : 10
}


order_1 = Order("A867", "Stefano", datetime.date(2020, 1, 1), order_1_items)
order_2 = Order("D465", "Almas", datetime.date(2020, 3, 25), order_2_items)
order_3 = Order("G196", "Keith", datetime.date(2020, 5, 19), order_3_items)
order_4 = Order("Q902", "Roger", datetime.date(2020, 11, 3), order_4_items)

all_orders = [order_1, order_2, order_3, order_4]