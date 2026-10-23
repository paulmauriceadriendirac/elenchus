# (ii) Decay (exponential, mean 1): believed interval at t=0.9 under three rules
import math
t=0.9
central=(-math.log(1-(1-t)/2), -math.log((1-t)/2))
hpd_id=(0.0, -math.log(1-t))
# HPD in log-time: density of Y=ln T is g(y)=exp(y-exp(y)); find c s.t. {g>=c} has mass t
def mass(c):
    # solve exp(y-exp(y))=c for two roots y1<0<y2 (max of g at y=0, g(0)=1/e)
    import math
    lo,hi=-30.0,0.0
    for _ in range(200):
        m=(lo+hi)/2
        (lo,hi)=(m,hi) if math.exp(m-math.exp(m))<c else (lo,m)
    y1=hi
    lo,hi=0.0,10.0
    for _ in range(200):
        m=(lo+hi)/2
        (lo,hi)=(m,hi) if math.exp(m-math.exp(m))>=c else (lo,m)
    y2=lo
    F=lambda y:1-math.exp(-math.exp(y))
    return F(y2)-F(y1),y1,y2
lo,hi=1e-12,1/math.e
for _ in range(200):
    c=(lo+hi)/2; mm,y1,y2=mass(c)
    (lo,hi)=(c,hi) if mm>t else (lo,c)
mm,y1,y2=mass(lo)
print("central (accuracy/interval-score) interval: [%.4f, %.4f]"%central)
print("HPD, identity measure (G&S default):        [%.4f, %.4f]"%hpd_id)
print("HPD, log measure (G&S Decay model):         [%.4f, %.4f]  mass=%.4f"%(math.exp(y1),math.exp(y2),mm))
