# el ordem de ejecución de las clases
class A:
   pass

class F:
    def hablar(self):
        print("Hola desde F")

class B(A):
    pass

class C(F):
    pass

# class D(B,C):
#     def hablar(self):
#         print("Hola desde D")

class D(B, C):
    pass

d = D()
d.hablar()
print(D.mro()) # imprime la orden de ejecucion