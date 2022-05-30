import math

class interval():
    def __init__(self,lower,upper=None):
        if lower is None:
            print("interval: No value assigned.")
        
        if upper is None:
            self._lower = lower
            self._upper = lower
        else:
            self._lower = lower
            self._upper = upper

    @property
    def lower(self):
        return self._lower 
    
    @lower.setter
    def lower(self, v):
        self._lower = v
    
    @property
    def upper(self):
        return self._upper

    @upper.setter
    def upper(self, v):
        self._upper = v

    #round 
    #toward plus infinity
    def succ(x):
        a = math.fabs(x)
        if a >= 2**(-969):
            return x + a * (2**(-53)+2**(-105))
        if a < -2**(-1021):
            return x + 2**(-1074)
        c = 2**53 * x
        e = (2**(-53)+2**(-105)) * abs(c)
        return (c + e) * 2**(-53)

    #toward minus infinity
    def pred(x):
        a = math.fabs(x)
        if a >= 2**(-969):
            return x - a * (2**(-53)+2**(-105))
        if a < -2**(-1021):
            return x - 2**(-1074)
        c = 2**53 * x
        e = (2**(-53)+2**(-105)) * abs(c)
        return (c - e) * 2**(-53)


    #4 arithmetic operations
    #(interval) + (interval)
    def __add__(self, v):
        lower = interval.pred(self.lower + v.lower)
        upper = interval.succ(self.upper + v.upper)
        return interval(lower, upper)

    #(interval) += (interval)
    def __iadd__(self, v):
        tmp = self + v
        return tmp    
    
    #(interval) - (interval)
    def __sub__(self, v):
        lower = interval.pred(self.lower - v.upper)
        upper = interval.succ(self.upper - v.lower)
        return interval(lower, upper)
    
    #(interval) -= (interval)
    def __isub__(self, v):
        tmp = self - v
        return tmp 

    #(interval) * (interval)
    def __mul__(self, v):
        if self.lower >= 0:
            if v.lower >= 0:
                lower = interval.pred(self.lower * v.lower)
                upper = interval.succ(self.upper * v.upper)
            elif v.upper <= 0:
                lower = interval.pred(self.upper * v.lower)
                upper = interval.succ(self.lower * v.upper)
            else:
                lower = interval.pred(self.upper * v.lower)
                upper = interval.succ(self.upper * v.upper)
        elif self.upper <= 0:
            if v.lower >= 0:
                lower = interval.pred(self.lower * v.upper)
                upper = interval.succ(self.upper * v.lower)
            elif v.upper <= 0:
                lower = interval.pred(self.upper * v.upper)
                upper = interval.succ(self.lower * v.lower)
            else:
                lower = interval.pred(self.lower * v.upper)
                upper = interval.succ(self.lower * v.lower)
        else:
            if v.lower >= 0:
                lower = interval.pred(self.lower * v.upper)
                upper = interval.succ(self.upper * v.upper)
            elif v.upper <= 0:
                lower = interval.pred(self.upper * v.lower)
                upper = interval.succ(self.lower * v.lower)
            else:
                lower = min(interval.pred(self.lower * v.upper), interval.pred(self.upper * v.lower))
                upper = max(interval.succ(self.lower * v.lower), interval.succ(self.upper * v.upper))
        
        return interval(lower, upper)

    #(interval) *= (interval)
    def __imul__(self, v):
        self = self * v
        return self 

    #(interval) / (interval)
    def __truediv__(self,v):
        if v.lower > 0:
            if self.lower >= 0:
                lower = interval.pred(self.lower / v.upper)
                upper = interval.succ(self.upper / v.lower)
            elif self.upper <= 0:
                lower = interval.pred(self.lower / v.lower)
                upper = interval.succ(self.upper / v.upper)
            else:
                lower = interval.pred(self.lower / v.lower)
                upper = interval.succ(self.upper / v.lower)
        elif v.upper < 0:
            if self.lower >= 0:
                lower = interval.pred(self.upper / v.upper)
                upper = interval.succ(self.lower / v.lower)
            elif self.upper <= 0:
                lower = interval.pred(self.upper / v.lower)
                upper = interval.succ(self.lower / v.upper)
            else:
                lower = interval.pred(self.upper / v.upper)
                upper = interval.succ(self.lower / v.upper)
        else:
            print("interval: division by 0")

        return interval(lower, upper)

    #(interval) /= (interval)
    def __itruediv__(self, v):
        self = self / v
        return self 

    #sqrt
    def sqrt(self):
        if(self.lower < 0):
            print("interval: sqrt of negative value")
        else:
            lower = interval.pred(math.sqrt(self.lower))
            upper = interval.succ(math.sqrt(self.upper))

        return interval(lower, upper)

    #print
    def __str__(self):
        return "[{0:.17f}, {1:.17f}]".format(self.lower, self.upper)