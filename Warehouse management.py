from datetime import datetime


class a_warehouse:
    def __init__(self ,product_name ,product_code ,number_of_goods ,unit_price_of_goods ,expiration_date_of_the_product):
        self.name = product_name
        self.code = product_code
        self.number = number_of_goods
        self.price = unit_price_of_goods
        self.data = expiration_date_of_the_product
        self.warehouse = {}
    
    def arrival_of_goods(self):
        if self.name not in self.warehouse:
            self.warehouse[self.name] = []
        self.warehouse[self.name].append([self.code, self.number, self.price, self.data])
        return self.warehouse
    
    def Product_removal(self, search_method, search_value):
        for key in list(self.warehouse.keys()):
            for item in self.warehouse[key]:
                if (search_method == 'code' and item[0] == search_value) or \
                   (search_method == 'name' and key == search_value):
                    self.warehouse[key].remove(item)
                    if len(self.warehouse[key]) == 0:
                        del self.warehouse[key]
                    print(f"Product with {search_method} = {search_value} removed.")
                    return
        print('Product not found.')

    def Warehouse_information(self):
        print(f'Warehouse information :\n{self.warehouse}')

    def Product_search(self, search_method, search_value):
        results = []
        for key in self.warehouse:
            for item in self.warehouse[key]:
                if (search_method == 'code' and item[0] == search_value) or \
                   (search_method == 'name' and key == search_value):
                    results.append({key: item})
        if results:
            print('Found products:', results)
        else:
            print('No products found.')

    def Calculate_the_total_value_of_the_warehouse(self):
        values = {}
        for key in list(self.warehouse.keys()):
            for item in self.warehouse[key]:
                value = item[1] * item[2]
                values[key] = value
        print(f'Value of available goods :\n{values}')

    def product_management(self):
        for key in list(self.warehouse.keys()):
            for item in self.warehouse[key]:
                target_date = datetime.strptime(item[3], "%Y-%m-%d")
                now = datetime.now()
                difference = target_date - now
                difference_now = str(difference)
                difference = difference_now[0:2]
                if int(difference) < 30:
                    print(key ,'The expiration date of this product is less than 30 days.')
                else :
                    print('The expiration date of your product is more than 30 days.')
                if item[1] < 10 :
                    print(key ,'This product is in stock for less than 10 items.')
                else:
                    print('The number of your items is allowed (above 10)')
                
product1 = a_warehouse('Apple', 'A001', 50, 0.5, '2025-06-10')
product1.arrival_of_goods()

product2 = a_warehouse('Banana', 'B002', 20, 0.3, '2025-05-15')
product2.arrival_of_goods()

product3 = a_warehouse('Orange', 'O003', 8, 0.4, '2025-05-20')
product3.arrival_of_goods()

product4 = a_warehouse('Grapes', 'G004', 15, 2.0, '2025-07-01')
product4.arrival_of_goods()

product5 = a_warehouse('Mango', 'M005', 12, 1.5, '2025-05-25')
product5.arrival_of_goods()

product6 = a_warehouse('Pineapple', 'P006', 5, 3.0, '2025-05-30')
product6.arrival_of_goods()

product7 = a_warehouse('Strawberry', 'S007', 18, 0.8, '2025-05-12')
product7.arrival_of_goods()

product8 = a_warehouse('Watermelon', 'W008', 25, 4.0, '2025-07-15')
product8.arrival_of_goods()
product9 = a_warehouse('Cherry', 'C009', 7, 2.5, '2025-05-18')
product9.arrival_of_goods()

product10 = a_warehouse('Peach', 'P010', 30, 1.2, '2025-06-05')
product10.arrival_of_goods()

product1.Product_search('name', 'Apple')
product2.Product_removal('code', 'B002')
product3.Warehouse_information()
product4.Calculate_the_total_value_of_the_warehouse()
product5.product_management()  



