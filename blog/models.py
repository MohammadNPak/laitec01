from django.db import models

# Create your models here.

# class Post()


class Father:
  def __init__(self,name,age) -> None:
      self.name=name
      self.age=age

  def say_hello(self):
    print(f"hi i'm {self.name}")


class Child(Father):
  def walk(self):
    print("I'm walking ")


