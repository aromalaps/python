import json
#loads
s='{"name":"abc","age":22}'
e=json.loads(s)
print(type(e))
print(e)

#dumps

d={"name":"abc","age":22}
l=[1,2,3]
t=('a','b','c')
s={1,2,3,4}
a=json.dumps(d)
b=json.dumps(l)
c=json.dumps(t)
d=json.dumps(list(s))
print(d)
print(l)
print(t)
print(d)
print(type(d))
print(type(l))
print(type(t))
print(type(d))