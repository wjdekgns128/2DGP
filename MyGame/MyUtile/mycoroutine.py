class CoroutineObject:
    def __init__(self,fun):
        self.current = None
        self.NextFun = fun
    def Next(self):
        needToNext = True
        if (isinstance(self.current, WaitForSeconds)):
            if (not self.current.Satisfy()):
                needToNext = False
        if needToNext:
            try:
                self.current = next(self.NextFun)
            except:
                return False
        return True

class Coroutine:
    def __init__(self):
        self.CroList = []
    def __del__(self):
        self.CroList.clear()
    def StartCoroutine(self, fun):
        self.CroList.append(CoroutineObject(fun))
    def RunCoroutine(self):
        for CorObject in self.CroList:
            if (not CorObject.Next()):
                self.CroList.remove(CorObject)

    def AllStop(self):
        self.CroList.clear()
class WaitForSeconds:
    def __init__(self,time):
        self.current = 0
        self.time = time
    def Satisfy(self):
        self.current = self.current + 0.016
        return self.current >= self.time


#상속받아서 사용
