class Person():
    def __init__(self, given_name):
        self.name = given_name

if __name__ == '__main__':
    p1 = Person("Joe")
    print(p1)                     # <__main__.Person object at 0x0000021EC664B358>
    print(p1.__class__.__name__)  # Person
    print(p1.name)                # Joe

    p2 = Person("Jane")
    print(p2)                     # <__main__.Person object at 0x0000021EC664B470>
    print(p2.name)                # Jane

    p1.name = "Joseph"
    print(p1)                     # <__main__.Person object at 0x0000021EC664B358>
    print(p1.name)                # Josheph
