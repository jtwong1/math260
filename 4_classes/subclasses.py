#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 20:44:34 2020

@author: jtwong
"""


class Pet:
    def __init__(self, name, noise):
        self.name = name
        self.noise = noise

    def annoy(self):
        print(self.noise*10)


class Fish(Pet):
    def swim():
        return


class Cat(Pet):
    def __init__(self, name):
        super().__init__(name, "meow")
        self.lives = 9

    def knock_over(obj):
        obj.destroy()


class Dog(Pet):
    def __init__self__(name):
        super().__init__(name, "woof")

    def fetch(obj):
        return obj
