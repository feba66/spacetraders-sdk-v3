from dataclasses import dataclass
from pydantic import BaseModel # not installed by default
from dacite import from_dict

@dataclass
class sub:
    d:int
    
@dataclass
class test:
    a:int
    b:int
    c:sub

class Test(BaseModel):
    a:int
    b:int
    c:sub

t = test(**{"a":1,"b":2,"c":{"d":3}})
print(t)
t1 = Test(**{"a":1,"b":2,"c":{"d":3}})
print(t1)

try:
    t2 = Test(1,2,sub(3))
    print(t2)
except Exception as e:
    print(f"t2 didnt work... {e}")
    
t3 = from_dict(test,{"a":1,"b":2,"c":{"d":3}})
print(t3)
t4 = test(1,2,sub(3))
print(t4)