from login_sys import login_sys
from display_products import display_table

products= [{"name":"water","price":80.0,"quantity":1500},
          {"name":"soda","price":130.0,"quantity":1500},
          {"name":"chips","price":200,"quantity":1500},
]
if __name__ == '__main__':
    login_sys()

    display_table(products)
