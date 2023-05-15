


class Member:
    def __init__(self, fullname):
        self.fullname = fullname

    def print_info(self):
        print(f"Hello {self.fullname}")
        raise NotImplementedError('Derived class must implement this method')


class VipMember(Member):
    def print_info(self):
        print(f"Hello {self.fullname}")

member1 = VipMember('john liman')
member1.print_info()