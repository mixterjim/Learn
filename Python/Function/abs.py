print abs(1)
print abs(-2)
def fake_abs(x):
    if x < 0:
        x = -x
    return x
print fake_abs(1)
print fake_abs(-2)
