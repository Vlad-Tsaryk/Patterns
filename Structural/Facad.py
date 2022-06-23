class Warehouse:
    def get_product(self):
        return 'Product received'


class Evaluation:
    def get_product_mark(self):
        return 'Product mark'


class Manager:

    def __init__(self, warehouse: Warehouse, evaluation: Evaluation):
        self.warehouse = warehouse or Warehouse()
        self.evaluation = evaluation or Evaluation()

    def get_product_info(self):
        result = ['Result:', self.warehouse.get_product(), self.evaluation.get_product_mark()]

        return "\n".join(result)


if __name__ == '__main__':
    w = Warehouse()
    e = Evaluation()
    m = Manager(w, e)
    print(m.get_product_info())
