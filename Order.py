__author__ = 'nandi_000'

import json

class Order:
    attributes = [ "Symbol", "Side", "Quantity", "Price", "Sender_Id", "Order_Id", "Executed", "Executed_Notional" ]
    def __init__(self,
                 Symbol = "",
                 Quantity = 0,
                 Price = 0,
                 Side = "Buy",
                 Sender_Id = "",
                 Executed = 0 ):

        self.Symbol = Symbol
        self.Quantity = Quantity
        self.Price = Price
        self.Sender_Id = Sender_Id
        self.Order_Id = 0 # This should be set by the parent as per the order count it maintains
        self.Side = Side
        self.Executed = Executed
        self.Executed_Notional = 0

    def toJson(self):
        Map = {}

        for attr in self.attributes:
            Map[ attr ] = getattr( self, attr )

        return( json.dumps( Map ))

    def fromJson(self, Order_Json ):
        Map = json.loads( Order_Json )
        for attr in self.attributes:
            if( attr in Map ):
                setattr( self, attr, Map[ attr ] )

    def Remaining_Quantity(self):
        return( self.Quantity - self.Executed )


#a = Order()
#b = a.toJson()







