# 作者
# NATURE
# 日期
# 2023/3/3 15:25
# 功能


class A1:
    # __slots__ = ['name', 'age']
    V = '类变量'

    def __init__(self):
        self.age = 24
        self.name = 123

    # 类方法需要使用@classmethod装饰器定义
    # 类方法的第一个参数用来绑定类，约定写为cls
    # 类和对象实例都可以调用类方法
    # 类方法不能访问此类创建的对象的属性
    @classmethod
    def get_v(cls):  # 此方法不是实例方法， 是类方法
        return cls.V

    # 静态方法需要使用 @staitcmethod装饰器定义
    # 静态方法与普通函数的定义相同，不需要传入self和cls
    # 静态方法只能凭借该类和实例来调用
    # 静态方法不能访问类变量和实例变量
    @staticmethod
    def myadd(a, b):
        return a + b

    def work(self):
        print('父类')


class B1(A1):
    """继承A1"""
    a = 1
    b = 2
    l = [1, 2]

    #
    def __init__(self):
        # super(B1, self).__init__()
        super().__init__()
        self.a = 3
        self.b = 4
        self.__c='私有属性'

    def work(self):
        print('子类')

    def __private_method(self):
        print('私有方法')

    def invoke_private(self):
        self.__private_method()



if __name__=="__main__":
    # 类方法调用
    print('类直接访问类方法', A1.get_v())  # 类直接访问类方法
    a = A1()
    print(a.__dict__)
    print('类实例访问类方法', a.get_v())  # 类实例访问类方法
    print('获取该实例的类访问类方法', a.__class__.get_v())  # 获取该实例的类访问类方法
    # 静态方法调用
    print('类实例访问静态方法',A1.myadd(100, 200))
    print('类对象获取类访问静态方法',a.__class__.myadd(100, 200))
    print('类对象访问静态方法',a.myadd(300, 400))

    # print(a.__slots__)
    # #类中定义__slots__变量后，类实例无该__dict__属性）
    # a.school='123' #类中已定义固定属性，不能出现其他属性


    b = B1()
    print(B1.__base__)
    b.work()
    super(B1, b).work()
    print(b.__dict__)
    print(B1.__mro__)
    print(B1.myadd(b.a,b.b))
    print(repr(b))
    b.invoke_private()
