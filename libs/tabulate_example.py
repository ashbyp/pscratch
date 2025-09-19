from tabulate import tabulate

table = [['foo', 10], ['bar', 20], ['baz', 30]]

print(tabulate(table, headers=['name', 'age']))

