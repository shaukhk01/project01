class p:
    def __init__(self):
        self.a = 20
class b(p):
      def __init__(self):
          self.b = 30
          super().__init__()
          print(self.a)
          print(self.b)
o = b()
