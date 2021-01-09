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
