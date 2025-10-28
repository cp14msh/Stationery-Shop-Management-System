class shop_management:
    def __init__(self):
        self.products = []
        self.sold =[]
    
    def inventory(self,name):

        for _ in self.products:

            if _["name"] == name:

                print(f"{_["inventory"]} {_["name"]} is avaiable.")
                return
            
        print(f"{_["name"]} is not avaiable!")
            

    
    def add_product(self, name, price, profit, inventory):

        for product in self.products:

            if product["name"] == name:

                product["inventory"] += inventory  
                print("You had already this product and your inventory updated!")

                return

        self.products.append({"name": name, "price" : price, "profit":profit, "inventory" : inventory})
        print("product added.")
    
    def sell_product(self,name,how_many):

        for _ in self.products:

            if _["name"] == name:

                if _["inventory"] >= how_many :

                    count = _["inventory"] 
                    _["inventory"] = count - how_many

                    if _["inventory"] <= 1:

                        print(f"!!Alert!!, you have only {_["inventory"]} of {name}")
                
                else :
                    print(f"You don't have {how_many} {name} in your inventory, You only have {_["inventory"] } in your inventory")
                    return

            
        for i in self.sold:

            if i["name"] == name:

                count_sell = i["How_many"]
                i["How_many"] = count_sell + how_many
                return

        for j in self.products:

            if j["name"] == name:

                self.sold.append({"name" : name , "price" : j["price"] , "How_many": how_many , "profit" : j["profit"]})

    def Report_of_the_day(self):
        sold_day = 0

        for _ in self.sold:

            sold_day = sold_day + (_["price"] * _["How_many"])

        print(f"You sold {sold_day} dollars today.")
        profit_day = 0

        for _ in self.sold:

            profit_day = _["profit"] * _["How_many"]  

        print(f"You made {profit_day} dollars profit today.")


    def the_product_of_day(self):
        top = self.sold[0]["How_many"]

        for _ in self.sold:

            if _["How_many"] >= top:

                top = _["How_many"]
                name_top = _["name"]
            
        print(f"{name_top} has been the best-selling.")