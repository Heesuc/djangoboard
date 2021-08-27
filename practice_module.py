class Calculator:
    def class_sum(self, a, b):
        result = a + b
        #print("%s님 %s + %s = %s입니다." % (self.name, a, b, result))
        return result
    
    def fun1(self):
        print("self 이해를 위한 테스트")
    
    def __init__(self, name="default"):
        self.name  = name