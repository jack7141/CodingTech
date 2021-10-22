from datetime import date
'''
* boiler-plate id, name, birth가 3번씩이나 사용되면서 코드 작성시 불편이 많아진다.
class User:
    def __init__(self, id: str, name: str, birth: date) -> None:
        self.id = id
        self.name = name
        self.birth = birth



# 이 방식으로 Print를 찍었을 경우 필드값이 나타나지 않아서 불편하다.
user = User(id=1, name='steve', birth=date(1992, 9, 24))
print(user) #<__main__.User object at 0x000001B21B2A3130>
'''

# 위의 문제를 해결하기 위해서 __repr__() method를 추가하여 필드값이 모두 출력되도록 출력형태를 변경
class User:
    '''
    User Class 
    * 테스트를 위한 user class
    '''
    def __init__(self, id: str, name: str, birth: date) -> None:
        '''
        * boiler-plate id, name, birth가 3번씩이나 사용되면서 코드 작성시 불편이 많아진다.
        '''
        self.id = id
        self.name = name
        self.birth = birth

    def fun(self, x: int) -> int:
        '''
        * fun : 테스트용 함수
        x는 테스트용 인자를 받는다.
        '''
        return x

    def __repr__(self) -> str:
        '''
        *!r 값은 입력받은 값을 표시해준다. 입력받은 값만 따음표로 표시해줌
        다른 수정자를 사용하면 포맷되기 전에 값을 변환할 수 있습니다. '!a'는 ascii()를, '!s'는 str()을, '!r'는 repr()을 적용합니다.:
        https://docs.python.org/ko/3/tutorial/inputoutput.html
        '''
        return (self.__class__.__qualname__ + f"(id={self.id!r}, name={self.name!r}, "
            f"birth={self.birth!r})") 

    def __eq__(self, o: object) -> bool:
        if o.__class__ == self.__class__:
            # 입력받는 클래스와 현재 클래스의 필드값들이 모두 같을때 True
            return (self.id, self.name, self.birth) == (o.id, o.name, o.birth)

        return NotImplemented
    

user = User(id=1, name='steve', birth=date(1992, 9, 24))
user2 = User(id=1, name='steve', birth=date(1992, 9, 24))
print(user == user2)

# 위와 같이 클래스를 디버깅하는데 생각보다 많은 코드가 필요하다.