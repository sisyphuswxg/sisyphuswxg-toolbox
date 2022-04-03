## 建造者模式

建造者模式将一个复杂对象的构造过程与其表现分离，这样，同一个构造过程可用于创建多个不同的表现。

Demo1:
对象有多个部分组成。

```python
class PersonBuilder():
    def BuildHead(self):
        pass

    def BuildBody(self):
        pass

    def BuildArm(self):
        pass

    def BuildLeg(self):
        pass


class PersonFatBuilder(PersonBuilder):

    type = 'Fat Baby'

    def BuildHead(self):
        print(f"head of {self.type}")

    def BuildBody(self):
        print(f"body of {self.type}")

    def BuildArm(self):
        print(f"arm of {self.type}")

    def BuildLeg(self):
        print(f"leg of {self.type}")


class PersonThinBuilder(PersonBuilder):

    type = 'Thin Boy'

    def BuildHead(self):
        print(f"head of {self.type}")

    def BuildBody(self):
        print(f"head of {self.type}")

    def BuildArm(self):
        print(f"head of {self.type}")

    def BuildLeg(self):
        print(f"head of {self.type}")


class PersonDirector():

    def __init__(self, builder):
        self.builder = builder

    def CreatePereson(self):
        self.builder.BuildHead()
        self.builder.BuildBody()
        self.builder.BuildArm()
        self.builder.BuildLeg()


def main():
    thin_builder = PersonThinBuilder()
    direct1 = PersonDirector(thin_builder)
    direct1.CreatePereson()

    print("-" * 20)
    fat_builder = PersonFatBuilder()
    direct2 = PersonDirector(fat_builder)
    direct2.CreatePereson()


if __name__ == '__main__':
    main()

    
# 运行结果：
head of Thin Boy
head of Thin Boy
head of Thin Boy
head of Thin Boy
--------------------
head of Fat Baby
body of Fat Baby
arm of Fat Baby
leg of Fat Baby
```


Demo2：
对象的创建经过多个不同的步骤，这些步骤也需要遵从特定的顺序。

```python
from enum import Enum

import time


PizzaProgress   = Enum('PizzaProgress', 'queued preparation baking ready')
PizzaDough      = Enum('PizzaDough', 'thin thick')  # dough: 生面图
PizzaSauce      = Enum('PizzaSauce', 'tomato creme_fraiche')
PizzaTopping    = Enum('PizzaTopping', 'mozzarella double_mozzarella bacon ham mushrooms red_onion oregano')


STEP_DELAY = 3


class Pizza:

    def __init__(self, name):
        self.name = name
        self.dough = None
        self.sauce = None
        self.topping = []

    def __str__(self):
        return self.name

    def prepare_dough(self, dough):
        self.dough = dough
        print('preparing the {} dough of your {}...'.format(self.dough.name, self))
        time.sleep(STEP_DELAY)
        print('done with the {} dough'.format(self.dough.name))


class MargaritaBuilder:

    def __init__(self):
        self.pizza = Pizza('margarita')
        self.progress = PizzaProgress.queued
        self.baking_time = 5      # in seconds for the sake of the example

    def prepare_dough(self):
        self.progress = PizzaProgress.preparation
        self.pizza.prepare_dough(PizzaDough.thin)

    def add_sauce(self):
        print('adding the tomato sauce to your margarita...')
        self.pizza.sauce = PizzaSauce.tomato
        time.sleep(STEP_DELAY)
        print('done with the tomato sauce')

    def add_topping(self):
        print('adding the topping (double mozzarella， oregano) to your margarita')
        self.pizza.topping.append([i for i in (PizzaTopping.double_mozzarella, PizzaTopping.oregano)])
        time.sleep(STEP_DELAY)
        print('done with the topping (double mozzarrella， oregano)')

    def bake(self):
        self.progress = PizzaProgress.baking
        print('baking your margarita for {} seconds'.format(self.baking_time))
        time.sleep(self.baking_time)
        self.progress = PizzaProgress.ready
        print('your margarita is ready')


class CreamyBaconBuilder:

    def __init__(self):
        self.pizza = Pizza('creamy bacon')
        self.progress = PizzaProgress.queued
        self.baking_time = 7      # in seconds for the sake of the example

    def prepare_dough(self):
       self.progress = PizzaProgress.preparation
       self.pizza.prepare_dough(PizzaDough.thick)

    def add_sauce(self):
        print('adding the crème fraîche sauce to your creamy bacon')
        self.pizza.sauce = PizzaSauce.creme_fraiche
        time.sleep(STEP_DELAY)
        print('done with the crème fraîche sauce')

    def add_topping(self):
        print('adding the topping (mozzarella， bacon， ham， mushrooms， red onion， oregano) to your creamy bacon')
        self.pizza.topping.append([t for t in (PizzaTopping.mozzarella,
            PizzaTopping.bacon, PizzaTopping.ham, PizzaTopping.mushrooms,
            PizzaTopping.red_onion, PizzaTopping.oregano)])
        time.sleep(STEP_DELAY)
        print('done with the topping (mozzarella， bacon， ham， mushrooms， red onion， oregano)')

    def bake(self):
        self.progress = PizzaProgress.baking
        print('baking your creamy bacon for {} seconds'.format(self.baking_time))
        time.sleep(self.baking_time)
        self.progress = PizzaProgress.ready
        print('your creamy bacon is ready')


class Waiter:
    def __init__(self):
        self.builder = None

    def construct_pizza(self, builder):
        self.builder = builder
        # calling method~~ cool!
        [step() for step in (builder.prepare_dough, builder.add_sauce, builder.add_topping, builder.bake)]

    @property
    def pizza(self):
        return self.builder.pizza


def validate_style(builders):
    try:
        pizza_style = input("What pizza would you like, [m]argarita or [c]reamy bacon? ")
        builder = builders[pizza_style]()
        valid_input = True
    except KeyError as err:
        print('Sorry, only margarita (key m) and creamy bacon (key c) are available')
        return (False, None)
    return (True, builder)


def main():
    builders = dict(m=MargaritaBuilder, c=CreamyBaconBuilder)
    valid_input = False
    while not valid_input:
        valid_input, builder = validate_style(builders)
    print()
    waiter = Waiter()
    waiter.construct_pizza(builder)
    pizza = waiter.pizza
    print()
    print('Enjoy your {}!'.format(pizza))


if __name__ == '__main__':
    main()


# 运行结果：
What pizza would you like, [m]argarita or [c]reamy bacon? m

preparing the thin dough of your margarita...
done with the thin dough
adding the tomato sauce to your margarita...
done with the tomato sauce
adding the topping (double mozzarella， oregano) to your margarita
done with the topping (double mozzarrella， oregano)
baking your margarita for 5 seconds
your margarita is ready

Enjoy your margarita!
```


### 其他使用场景

- django-widgy   生成HTML页面
- django-query-builder    生成动态的SQL查询
