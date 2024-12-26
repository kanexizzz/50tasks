def enemy(x):
    result = []
    a = ['Jack', 'Boris', "Daniel"]
    for i in x:
        if i not in a:
            result.append(i)
    return (result)
print(enemy(['Daniel', 'Jack', "John", 'Boris', "Henry"]))