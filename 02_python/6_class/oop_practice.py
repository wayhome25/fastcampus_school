# -*- coding: utf-8 -*-

class Employee(object):
    raise_amount = 1.1  # 1 연봉 인상율 클래스 변수

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first.lower() + '.' + last.lower() + '@schoolofweb.net'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    def full_name(self):
        return '{} {}'.format(self.first, self.last)

    def get_pay(self):
        return '현재 "{}"의 연봉은 "{}"입니다.'.format(self.full_name(), self.pay)


emp_1 = Employee('Sanghee', 'Lee', 50000)
emp_2 = Employee('Minjung', 'Kim', 60000)

# 연봉 인상 전
print(emp_1.get_pay())
print(emp_2.get_pay())

# 연봉 인상
emp_1.apply_raise()
emp_2.apply_raise()

# 연봉 인상 후
print(emp_1.get_pay())
print(emp_2.get_pay())