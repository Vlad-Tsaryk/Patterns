import copy


class Test1:
    def __init__(self):
        self.parent = None

    def set_parent(self, parent):
        self.parent = parent


class Test2:

    def __init__(self, number, test_list, ref):
        self.number = number
        self.test_list = test_list
        self.ref = ref

    def __copy__(self):

        test_list = copy.copy(self.test_list)
        ref = copy.copy(self.ref)

        new = self.__class__(
            self.number, test_list, ref
        )
        new.__dict__.update(self.__dict__)

        return new

    def __deepcopy__(self, memo=None):
        if memo is None:
            memo = {}

        test_list = copy.deepcopy(self.test_list, memo)
        ref = copy.deepcopy(self.ref, memo)

        new = self.__class__(
            self.number, test_list, ref
        )
        new.__dict__ = copy.deepcopy(self.__dict__, memo)

        return new


if __name__ == "__main__":

    test_list = [1, {1, 2, 3}, [1, 2, 3]]
    ref = Test1()
    component = Test2(23, test_list, ref)
    ref.set_parent(component)
    copied_component = copy.copy(component)

    copied_component.test_list.append("another object")
    print(copied_component.test_list)
    deep_copied_component = copy.deepcopy(component)
    deep_copied_component.test_list.append("one more object")
    print(deep_copied_component.test_list)
    copied_component.test_list.append("another object")
    print(copied_component.test_list)
    print(deep_copied_component.test_list)


