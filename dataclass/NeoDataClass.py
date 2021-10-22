from dataclasses import dataclass # 3.7부터 사용가능함
from datetime import date

# 데코레이터를 사용해 기존의 방식을 모두 취하면서 사용할 수 있음
# 만약 데이터 중 불변성이 보장되야하는 데이터가 존재할시, frozen 옵션을 사용하면된다.
#  또한 불변성을 주고싶은 데이터는 최하단에 있어야함
# (만약 처음준 값에서 수정하려하면 dataclasses.FrozenInstanceError: cannot assign to field 'name' 발생)
@dataclass(frozen=True)
class User:
    id: int
    birth: date
    name: str 


user = User(id=1, name='steve', birth=date(1992, 9, 24))
user2 = User(id=1, name='steve', birth=date(1992, 9, 24))
print(user)



# 참조
# https://www.daleseo.com/python-dataclasses/