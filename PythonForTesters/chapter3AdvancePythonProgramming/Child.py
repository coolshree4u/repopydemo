from Parent import Parent


class Child(Parent):

    def __init__(self):
        print("This is child class Constructor")

    def metChild(self):
        print("This is Child class Method")
