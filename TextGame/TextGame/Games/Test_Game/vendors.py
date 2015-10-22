#forcechange
from .items import *

dh_vendor_001 ={
    "name":"Travelling Merchant",                  # Name displayed for the vendor
    "description":"A bearded man, a worn cart and items that may have seen the best days long ago",           # Description printed for the vendor
    "stock_items":[dh_sword_002],           # (List of item dictionary variables) e.g. [sword_001] Items the vendor has for sale 
    "acquired_items":[]        # (List of item dictionary variables) e.g. [sword_001] Items the player sells are stored here, they are still re-purchasable but only upon asking to view them to keep the shopping menu tidy. (Do not place items in here)
    }