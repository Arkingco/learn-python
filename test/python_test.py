# class Rectangle:
#     count = 0  # 클래스 변수

#     # 초기자(initializer)
#     def __init__(self, width, height):
#         # self.* : 인스턴스변수
#         self.width = width
#         self.height = height
#         Rectangle.count += 1

#     # 메서드
#     def calcArea(self):
#         area = self.width * self.height
#         return area


class CustomClass:
    # 생성자로 객체생성을 호출받으면 먼저 __new__ 를 호출하여 객체를 생성할당하고, __new__ 메소드가 __init__메소드를
    # 호출하여 객체에서 사용할 초기값들을 초기화하게됩니다.
    # 간혹 여러 자료들을 보면.. __init__ 메소드를 생성자로 소개하는 경우가 있는데, 그렇지 않습니다.

    # 자료 https://stackoverflow.com/questions/6578487/init-as-a-constructor

    # 일반적으로 파이썬에서 클래스를 만들 시 __init__ 메소드만 오버라이딩하여 객체초기화에만 이용합니다.
    def __init__(self, param):
        print(param)


class Flight:
    def __init__(self, number):
        self._number = number
        super().__init__()

    def number(self):
        return self._number


f = Flight(10)
print(f.number())












