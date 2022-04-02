## 原型模式

是用于创建重复的对象，同时又能保证性能。这种类型的设计模式属于创建型模式，它提供了一种创建对象的最佳方式。
本质就是克隆对象，在对象初始化操作比较复杂的情况下，很实用，能大大降低耗时，提高性能，因为"不用重新初始化对象，而是动态地获得对象运行时的状态"。

创建对象的克隆，其最简单的形式就是一个 clone()函数，接受一个对象作为输入参数，返回输入对象的一个副本。
拷贝分为深拷贝和浅拷贝，使用python内置的copy模块实现。
- 深拷贝（deep copy）:对对象实例中字段引用的对象也进行拷贝。
- 浅拷贝（Shallow Copy）:指对象的字段被拷贝，而字段引用的对象不会被拷贝，拷贝的对象和源对象只是名称相同，但是他们共用一个实体。
深拷贝的优点是对象之间互不影响，但是会耗费资源，创建比较耗时；如果不会修改对象可以使用浅拷贝，更加节省资源和创建时间。


Demo1:
```python
import copy


class Book:

    def __init__(self, name, authors, price):
        self.name = name
        self.authors = authors
        self.price = price

    def clone(self, **kwargs):
        book_copy = self.__class__(self.name, self.authors[:], self.price)
        book_copy.__dict__.update(**kwargs)
        return book_copy


book = Book('hello', ['tom', 'jim'], 10)
print(book.__dict__)

book2 = book.clone(name='world', price=20)
print(book2.__dict__)

book3 = copy.deepcopy(book)
book3.name = 'english'
book3.price = 10.5
print(book3.__dict__)


# 运行结果：
{'name': 'hello', 'authors': ['tom', 'jim'], 'price': 10}
{'name': 'world', 'authors': ['tom', 'jim'], 'price': 20}
{'name': 'english', 'authors': ['tom', 'jim'], 'price': 10.5}
```

Demo2:

简历类Resume继承抽象原型的clone和deepclone方法，实现对简历类的复制；
简历类引用工作经历类，可以在复制简历类的同时修改局部属性；

obj3是obj1的深拷贝，修改后不影响obj1； 
obj2是obj1的浅拷贝，修改了引用内容，影响到obj1；

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-

from copy import copy, deepcopy


class Prototype(object):

    def clone(self):
        pass

    def deep_clone(self):
        pass


class WorkExperience(object):

    def __init__(self):
        self.timearea = ''
        self.company = ''

    def set_workexperience(self, timearea, company):
        self.timearea = timearea
        self.company = company


class Resume(Prototype):

    def __init__(self,name):
        self.name = name
        self.workexperience = WorkExperience()

    def set_personinfo(self,sex,age):
        self.sex = sex
        self.age = age

    def set_workexperience(self,timearea, company):
        self.workexperience.set_workexperience(timearea, company)

    def display(self):
        print(self.name)
        print(self.sex, self.age)
        print('工作经历', self.workexperience.timearea, self.workexperience.company)

    def clone(self):
        return copy(self)

    def deep_clone(self):
        return deepcopy(self)


if __name__ == '__main__':
    obj1 = Resume('andy')
    # 浅拷贝对象
    obj2 = obj1.clone()
    # 深拷贝对象
    obj3 = obj1.deep_clone()

    obj1.set_personinfo('男', 20)
    obj1.set_workexperience('2010-2015','AA')

    obj2.set_personinfo('男', 30)
    obj2.set_workexperience('2010-2020','BB')  # 修改浅拷贝的对象工作经历

    obj3.set_personinfo('男', 40)
    obj3.set_workexperience('2020-2022','CCC')  # 修改深拷贝的对象的工作经历


    obj1.display()
    print()
    obj2.display()
    print()
    obj3.display()


## 运行结果：
andy
男 20
工作经历 2010-2020 BB

andy
男 30
工作经历 2010-2020 BB

andy
男 40
工作经历 2020-2022 CCC
```