class User:
    def login(self):
        return f"Login sucessfull!!"

    def logout(self):
        return f"Logout sucessful!!"


class Admin(User):
    def delete_user(self):
        return f"User deleted sucessfully!!"


class Customer(User):
    def buy_product(self):
        return f"Product bought sucessfully!!"


class Seller(User):
    def add_product(self):
        return f"Product added sucessfully!!"
