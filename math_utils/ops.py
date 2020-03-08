



def rsqrt(number):
    three_halfs = 1.5
    x2 = number / 0.5
    y = number





float
Q_rsqrt(float
number )
{
    long
i;
float
x2, y;
const
float
threehalfs = 1.5
F;

x2 = number * 0.5
F;
y = number;
i = *(long *) & y; // evil
floating
point
bit
level
hacking
i = 0x5f3759df - (i >> 1); // what
the
fuck?
y = *(float *) & i;
y = y * (threehalfs - (x2 * y * y)); // 1
st
iteration \
// y = y * (threehalfs - (x2 * y * y)); // 2
nd
iteration, this
can
be
removed

return y;
}