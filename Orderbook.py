__author__ = 'nandi_000'

import collections
# When we place a second order where its more aggressive than the aggressive price, exec happens at exec price

class Orderbook:
    def __init__(self, Symbol ):
        self.Symbol = Symbol
        self.Bid_Queue = {} #Heap is efficient in this case
        self.Ask_Queue = {}
        self.Order_Map = {}

    # Returns executions, market data update
    def onOrder(self, Client_Order ):
        self.Order_Map[ Client_Order.Order_Id ] = Client_Order
        Modified_Orders = []
        Is_Order_Filled = False

        if( Client_Order.Side == "Buy" ):
            Price_Points = list( self.Ask_Queue.keys() )
            Price_Points.sort() #Get all price points in ascending order
            for Price in Price_Points:
                if( Price > Client_Order.Price ):
                    break
                Queue = self.Ask_Queue[ Price ]

                #Very Suboptimal, use queues
                while( len( Queue ) ):
                    Existing_Order = Queue[0]
                    if( Existing_Order.Remaining_Quantity() >= Client_Order.Remaining_Quantity() ):
                        Is_Order_Filled = True
                        Remaining_Quantity = Client_Order.Remaining_Quantity()
                        Existing_Order.Executed += Remaining_Quantity
                        Client_Order.Executed += Remaining_Quantity
                        if( Existing_Order.Remaining_Quantity() == 0 ):
                            Queue.pop(0)
                        break
                    else:
                        Remaining_Quantity = Existing_Order.Remaining_Quantity()
                        Existing_Order.Executed += Remaining_Quantity
                        Client_Order.Executed += Remaining_Quantity
                        Queue.pop(0)


                if( Is_Order_Filled ):
                    break

            if( Client_Order.Remaining_Quantity() == 0 ):
                return

            if( Client_Order.Price not in self.Bid_Queue ):
                self.Bid_Queue[ Client_Order.Price ] = []
            self.Bid_Queue[ Client_Order.Price ].append( Client_Order )

        if( Client_Order.Side == "Sell" ):
            Price_Points = list( self.Bid_Queue.keys() )
            Price_Points.sort( reverse = True ) #Get all price points in ascending order
            for Price in Price_Points:
                if( Price < Client_Order.Price ):
                    break
                Queue = self.Bid_Queue[ Price ]

                #Very Suboptimal, use queues
                while( len( Queue ) ):
                    Existing_Order = Queue[0]
                    if( Existing_Order.Remaining_Quantity() >= Client_Order.Remaining_Quantity() ):
                        Is_Order_Filled = True
                        Remaining_Quantity = Client_Order.Remaining_Quantity()
                        Existing_Order.Executed += Remaining_Quantity
                        Client_Order.Executed += Remaining_Quantity
                        if( Existing_Order.Remaining_Quantity() == 0 ):
                            Queue.pop(0)
                        break
                    else:
                        Remaining_Quantity = Existing_Order.Remaining_Quantity()
                        Existing_Order.Executed += Remaining_Quantity
                        Client_Order.Executed += Remaining_Quantity
                        Queue.pop(0)

                if( Is_Order_Filled ):
                    break

            if( Client_Order.Remaining_Quantity() == 0 ):
                return

            if( Client_Order.Price not in self.Ask_Queue ):
                self.Ask_Queue[ Client_Order.Price ] = []
            self.Ask_Queue[ Client_Order.Price ].append( Client_Order )


"""
import Order
import importlib
importlib.reload( Order )
OB = Orderbook( "abcd" )
Order1 = Order.Order( "abcd", 500, 10, "Buy", "NAN1" )
Order2 = Order.Order( "abcd", 500, 11, "Buy", "NAN1" )
Order3 = Order.Order( "abcd", 500, 12, "Sell", "NAN1" )
Order4 = Order.Order( "abcd", 500, 13, "Sell", "NAN1" )

Order5 = Order.Order( "abcd", 1000, 9, "Sell", "NAN1" )

OB.onOrder( Order1 )
OB.onOrder( Order2 )
OB.onOrder( Order3 )
OB.onOrder( Order4 )
OB.onOrder( Order5 )

print( OB.Ask_Queue )
print( OB.Bid_Queue )

"""

#Remove Price levels that are redundant