import pandas as pd

s1 = pd.Series([10, 20, 30, 40])
s2 = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])

print(s1)
print(s2)


marks=pd.Series([85,65,90],index=['maths','physics','chemistry'])
print(marks['maths'])
print(marks[['physics','chemistry']])


scores=pd.Series([45,55,65,78,90,94])
passed=scores[scores>60]
print(passed)


data=pd.Series([10,None,30,None])
print(data.isnull())
print(data.fillna(0))

names=pd.Series(['alice','Bob','CAT'])
print(names.str.lower())
print(names.str.contains('A'))