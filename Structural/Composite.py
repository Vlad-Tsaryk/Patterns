from abc import ABC, abstractmethod


class IProduct(ABC):
    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_cost(self) -> float:
        pass


class Product(IProduct):
    def __init__(self, name, cost):
        self.__name = name
        self.__cost = cost

    def get_name(self):
        return self.__name

    def get_cost(self) -> float:
        return self.__cost


class CompoundProduct(IProduct):

    def __init__(self, name):
        self.__name = name
        self.__product = []

    def get_name(self):
        return self.__name

    def add_product(self, product: IProduct):
        self.__product.append(product)

    def remove_product(self, product: IProduct):
        self.__product.remove(product)

    def get_cost(self) -> float:
        i = 0
        for prod in self.__product:
            i += prod.get_cost()
        return i


# class Order(IProduct):
#
#     def __init__(self, name):
#         self.__name = name
#         self.__product_list = []
#
#     def add_product(self, product: IProduct):
#         self.__product_list.append(product)
#
#     def get_name(self):
#         return self.__name
#
#     def get_cost(self) -> None:
#         i = 0
#         for prod in self.__product_list:
#             i += prod.get_cost()
#         print(f'Order price: {i}')


if __name__ == '__main__':
    cheese = CompoundProduct('Сыр')
    cheese.add_product(Product('Молоко', 12.3))
    cheese.add_product(Product('Соль', 1.5))
    cheese.add_product(Product('Закваска', 5.1))
    cheese.add_product(Product('Специи', 2))
    print(cheese.get_cost())
    apple = Product('Яблоко', 5.3)
    print(apple.get_cost())
    # order1 = Order('Заказ 1')
    # order1.add_product(cheese)
    # order1.add_product(apple)
    # order1.get_cost()
