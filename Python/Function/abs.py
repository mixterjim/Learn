print abs(1)
print abs(-2)
def fake_abs(x):
    if x < 0:
        x = -x
    print x
fake_abs(1)
fake_abs(-2)
