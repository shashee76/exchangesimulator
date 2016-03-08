__author__ = 'nandi_000'

import Order

class Ordermanager:
    def __init__(self):
        self.Orders = []
        self.Order_Id_Count = 0
        self.Order_Book = {}

    def insertOrder(self, new_order ):
        self.Order_Id_Count += 1
        new_order.Order_Id = self.Order_Id_Count
        self.Orders.append( new_order )
