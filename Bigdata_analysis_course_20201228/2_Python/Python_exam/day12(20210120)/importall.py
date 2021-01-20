import sys
sys.path.append("C:/PyStudy")

from mypack.calc import *
add.outadd(1,2)
multi.outmulti(1,2)

# 가능하지만 권장되지는 않는 방법
from mypack.report.table import *
outreport()
a()
b()
c()