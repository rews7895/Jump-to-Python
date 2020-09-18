# 클래스
# class : 똑같은 무엇인가를 계속해서 만들어 낼 수 있는 설계 도면
# object : 클래스로 만든 피조물로써, 객체마다 고유한 성격을 가진다.
# 즉 동일한 클래스로 만든 객체들은 서로 전혀 영향을 주지 않는다.
class Calculator:
    def __init__(self):
        self.result = 0
    
    def add(self, num):
        self.result += num
        return self.result

cal1 = Calculator()
cal2 = Calculator()

# print(cal1.add(3))
# print(cal1.add(4))
# print(cal2.add(3))
# print(cal2.add(7))

# 객체와 인스턴스의 차이
"""
클래스로 만든 객체를 인스턴스라고도 한다. 따라서 인스턴스라는 말은 특정 객체가 어떤 클래스의 객체인지를 관계 위주로 설명할 때 사용.
ex) a는 객체 / a는 Cookie의 인스턴스
"""
# self: 첫 번째 매개변수 self에는 setData메서드를 호출한 객체 a가 자동으로 전달.
# 파이썬 매서드의 첫 번째 매개변수 이름은 관례적으로 self를 사용한다. 객체를 호출할 때 호출한 객체 자신이 전달되기 때문. 
# self말고 다른 이름을 사용해도 상관없음.
class FourCal:
    def setData(self, first, second):
        self.first = first
        self.second = second
    # 더하기
    def add(self):
        result = self.first + self.second
        return result
    # 곱하기
    def mul(self):
        result = self.first * self.second
        return result
    # 빼기
    def sub(self):
        result = self.first - self.second
        return result
    # 나누기
    def div(self):
        result = self.first / self.second
        return result
     
a = FourCal()
a.setData(4, 2)
# print(type(a))
# print(a.first)
# print(a.second)
# print(a.add())
# print(a.mul())
# print(a.sub())
# print(a.div())

# 클래스로 만든 객체의 객체변수는 다른 객체의 객체변수에 상관없이 독립적인 값을 유지한다.

# 생성자(Constructor) : 객체가 생성될 때 자동으로 호출되는 메서드를 의미
# 초깃값을 설정해야 할 필요가 있을 때는 생성자를 구현하는 것이 안전한 방법.
class ConFourCal:
    # __init__ : 생성자로 인식되어 객체가 생성되는 시점에 자동으로 호출
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def setData(self, first, second):
        self.first = first
        self.second = second
    # 더하기
    def add(self):
        result = self.first + self.second
        return result
    # 곱하기
    def mul(self):
        result = self.first * self.second
        return result
    # 빼기
    def sub(self):
        result = self.first - self.second
        return result
    # 나누기
    def div(self):
        result = self.first / self.second
        return result

b = ConFourCal(4, 2)
# print(b.first)
# print(b.second)
# print(b.add())
# print(b.div())

# 클래스의 상속 : 어떤 클래스를 만들 때 다른 클래스의 기능을 물려받을 수 있게 만드는 것.
# 보통 상속은 기존 클래스를 변경하지 않고 기능을 추가하거나 기존 기능을 변경하려고 할 때 사용.
"""
class 클래스 이름(상속할 클래스 이름)
"""
class MoreFourCal(ConFourCal):
    def pow(self):
        result = self.first ** self.second
        return result

a = MoreFourCal(4, 2)
# print(a.add())
# print(a.pow())

# 매서드 오버라이딩
class SafeFourCal(ConFourCal):
    def div(self): # div매서드는 ConFourCal에 존재, 기존 것을 사용하여 second부분을 0인채 실행을 하면 ZeroDivisionError가 발생!
        if self.second == 0:
            return 0
        else:
            return self.first / self.second

a = SafeFourCal(4, 0)
# print(a.div())

# 클래스 변수 : 클래스 변수는 클래스 안에 함수를 선언하는 것과 마찬가지로 클래스 안에 변수를 선언하여 생성.
class Family:
    lastName = '김'

print(Family.lastName)
Family.lastName = '박'
print(Family.lastName)
