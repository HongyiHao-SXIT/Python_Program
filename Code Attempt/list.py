bicycles = ['trek', 'cannondale', 'redline', 'specialized']

print(bicycles[1])
print(bicycles[1].title())
print(bicycles[-1])

message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)

motorcycles = ['honda', 'yamaha', 'suzaki']
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

motorcycles.insert(0,'MoMo')
print(motorcycles[0])

del motorcycles[0]
print(motorcycles)

poped_motorcycles = motorcycles.pop()
print(poped_motorcycles)