import math as mt

for i in range(0,181,10):
    print("sin({})= {:.3f}, cos({}) = {:.3f}, tan({}) = {:.3f}"
          .format(i,mt.sin(mt.radians(i)),i, mt.cos(mt.radians(i)),
                  i, mt.tan(mt.radians(i))))
