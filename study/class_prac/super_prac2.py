#!/usr/bin/env python
# coding=utf-8

"""
使用父亲 super的例子
python2的例子


"""
__metaclass__ = type  # 使用新式类

import json


class Person:
    def __init__(self):
        self.height = 160

    def about(self, name):
        print("{} is about {}".format(name, self.height))


class Girl(Person):
    def __init__(self):
        # 下面，显示调用父类的init方法,  self.height=160 . 参数第一个是当前子类的类名字，第二个是 self 。
        super(Girl, self).__init__()
        self.breast = 90

    def about(self, name):
        print("{} is a hot girl, she is about {}, and her breast is {}".format(name, self.height, self.breast))
        #去person里面找about
        super(Girl, self).about(name)
        #调用父类的方法


if __name__ == "__main__":
    cang = Girl()
    #打印super的所使用的类顺序
    print(Girl.mro())
    cang.about("wangguniang")
