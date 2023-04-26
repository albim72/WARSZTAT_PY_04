class Specjalna:
    def __init__(self,x):
        self.x=x
        print("instancja została utworzona!")

    def __call__(self):
        print(f"4-krotność x: {4*self.x}")
        print("instancja wołana poprzez specjalną metodę call!")


ob = Specjalna(45)
print(ob)
ob()
