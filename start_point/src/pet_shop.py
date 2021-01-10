# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name(list):
    name = list["name"]
    return name



def get_total_cash(list):
    sum = list["admin"]["total_cash"]
    return sum

   

def add_or_remove_cash(list, amount):
    list["admin"]["total_cash"] += amount   
    return amount


def get_pets_sold(list):
    sold = list["admin"]["pets_sold"]
    return sold


def increase_pets_sold(list, amount):
    list["admin"]["pets_sold"] += amount
    return amount


def get_stock_count(list):
    count = len(list["pets"])
    return count


def get_pets_by_breed(list, search_breed):
    count = []
    for pet in list["pets"]:
        if pet["breed"] == search_breed:
            count.append(pet)   
    return count


def find_pet_by_name(list, search_name):
    for pet in list["pets"]:
        if search_name == pet["name"]:
            return pet
        



def remove_pet_by_name(list, search_name):
    pet = find_pet_by_name(list, search_name)
    for pet in list["pets"]:
        if pet["name"] == search_name:
            list["pets"].pop(list["pets"].index(pet))



def add_pet_to_stock(list, new_pet):
    list["pets"].append(new_pet)



def get_customer_cash(list):
    cash = list["cash"]
    return cash


def remove_customer_cash(customer, amount):
    customer["cash"] = customer["cash"] - amount
    return customer["cash"]
    
    
def get_customer_pet_count(customer):
    count = len(customer["pets"])
    return count


def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)
    

    