__author__ = 'nandi_000'

from future.backports import datetime

import unittest
import time
import Order
import Orderbook

class testOrderbook(unittest.TestCase):
#check if the values for LT are valid

    def test_onOrder( self ):
        OB = Orderbook.Orderbook( "abcd" )
        Order1 = Order.Order( "abcd", 500, 10, "Buy", "NAN1" )
        Order2 = Order.Order( "abcd", 500, 11, "Buy", "NAN1" )
        Order3 = Order.Order( "abcd", 500, 12, "Sell", "NAN1" )
        Order4 = Order.Order( "abcd", 500, 13, "Sell", "NAN1" )
        Order5 = Order.Order( "abcd", 1000, 9, "Sell", "NAN1" )

        i = 0;
        for O in [ Order1, Order2, Order3, Order4, Order5 ]:
            O.Order_Id = i
            i += 1

        OB.onOrder( Order1 )
        OB.onOrder( Order2 )
        OB.onOrder( Order3 )
        OB.onOrder( Order4 )
        OB.onOrder( Order5 )

        self.assertEqual( OB.Bid_Queue, {10: [], 11: []} )
        self.assertEqual( len( OB.Ask_Queue ), 2 )
        self.assertEqual( len( OB.Ask_Queue[12] ), 1 )
        self.assertEqual( len( OB.Ask_Queue[13] ), 1 )

        self.assertEqual( len( OB.Updates ), 4 )

        OB = Orderbook.Orderbook( "abcd" )
        Order1 = Order.Order( "abcd", 500, 10, "Buy", "NAN1" )
        Order2 = Order.Order( "abcd", 500, 11, "Buy", "NAN1" )
        Order3 = Order.Order( "abcd", 500, 12, "Sell", "NAN1" )
        Order4 = Order.Order( "abcd", 500, 13, "Sell", "NAN1" )
        Order5 = Order.Order( "abcd", 1000, 14, "Buy", "NAN1" )

        i = 0;
        for O in [ Order1, Order2, Order3, Order4, Order5 ]:
            O.Order_Id = i
            i += 1

        OB.onOrder( Order1 )
        OB.onOrder( Order2 )
        OB.onOrder( Order3 )
        OB.onOrder( Order4 )
        OB.onOrder( Order5 )

        self.assertEqual( OB.Ask_Queue, {12: [], 13: []} )
        self.assertEqual( len( OB.Bid_Queue ), 2 )
        self.assertEqual( len( OB.Bid_Queue[10] ), 1 )
        self.assertEqual( len( OB.Bid_Queue[11] ), 1 )

        self.assertEqual( len( OB.Updates ), 4 )

if __name__ == '__main__':
    unittest.main()


