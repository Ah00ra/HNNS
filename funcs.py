import math
def torque(a,b,c,d):
    #a=int(a)
    #b=int(b)
    #c=int(c)
    #a=int(d)
    return str(a+b+c+d)


def spur_gear(h, d, n):
    ans = (60000*h)/(math.pi*d*n)
    return str(ans)


def open_belt(cd, d, c):
    tcd = math.pi - math.asin((cd-d)/(2*c))
    td = math.pi + math.asin((cd+d)/(2*c))
    l = math.sqrt(4*cd ** 2 - (cd - d) ** 2) + 1/2 * (cd*tcd + d*td)
    #TODO: write andis
    ans = f"""theta D = {tcd}
θd = ϕ = {td}  
L = {l}
"""
    return ans


def open_belt(cd, d, c):
    td = math.pi + math.asin((cd+d)/(2*c))
    l = math.sqrt(4*cd ** 2 - (cd - d) ** 2) + 1/2 * ((cd + d)*td)

    ans = f"""θ = {td}
L = {l}
"""
    return ans


def belt_speed(d, n):
    ans = (math.pi * d * n)/12

    return ans


def fc_belt(w, v):
    g =32.17 
    ans = (w/g)*((v/60)**2)
    return ans


def omg(y,b,t):
    ans = 12*y*b*t
    return ans


def expphi(phi, f):
    ans = math.exp(phi*f)
    return ans

def TorqueBelt(H_nom,K_s,n_d,n):
    ans = ((63025*H_nom*K_s*n_d))/n
    return ans

def f1a_f2(T,d):
    ans = ((2*T)/d)
    return ans

def fi(t,d,f,phi,):
    ans = (t/d*(((math.exp(f*phi)+1)/((math.exp(f*phi)-1)))))
    return ans

def fi2(fc,f2_p,f1a_p):
    ans = (((f2_p+f1a_p)/2)-fc)
    return ans


def f2(f1a_p,f1ap_f2):
    ans = ((f1a_p)-(f1ap_f2))
    return ans

def f1a(b,fa,cv,cp):
    ans = (b*fa*cv*cp)
    return ans

def f_prime(phi,f1a_p,fc,f2):
    ans =((1/phi)*(math.log((f1a_p-fc)/(f2-fc))))    
    return ans

def dip(c,w,fi_p,):
    ans =(((c**2)*w)/(96*fi_p))   
    return ans


def sfnp(np):
    ans = 14.17*1000000*(1000000)**-0.407
    return ans

def sfsy(sy):
    ans = sy/3
    return ans

def degrees_to_radians(degrees):
    return degrees * (math.pi / 180)

def minibi(sf,et,nu,dcap,tcap,t,f,phi):

    deltaf = (2*tcap)/dcap
    #a = (sf-(et/((1-(nu**2))*dcap))) * t
    x = et/((1-nu**2)*dcap)
    a = (sf - x)*t
    radianphi = degrees_to_radians(phi)
    minb = deltaf / a*math.exp(f*radianphi)/(math.exp(f*radianphi)-1)
    return minb

def f1pa(sf, et, nu, dcap, t, b):
    x = et/((1-nu**2)*dcap)
    ab = (sf - x)*t*b
    return ab


def deltaf(capt, capd):
    ans = 2*capt/capd
    return ans 


def f2metalbelt(sf,et,nu,dcap,tcap,t,b):
    x = et/((1-nu**2)*dcap)
    ab = (sf - x)*t*b
    delf = 2*tcap/dcap
    ans = ab - delf
    return ans

def fi_2(sf,et,nu,dcap,tcap,t,b):
    x = et/((1-nu**2)*dcap)
    ab = (sf - x)*t*b
    delf = 2*tcap/dcap
    ans = ab - (delf/2)
    return ans



def fprime2(sf,et,nu,dcap,tcap,t,b, phi):
    f1a = f1pa(sf,et,nu,dcap,t,b) 
    f2 = f2metalbelt(sf,et,nu,dcap,tcap,t,b)
    radian_phi = degrees_to_radians(phi)
    ans = (1/radian_phi)*math.log(f1a/f2)
    return ans


def h_link_plate(N,n,p):
    a = N**1.08
    b = (n**0.9)
    c = 3-(0.07*p)
    ans = 0.004*a*b*(p**c)
    return ans

def center_distance(n1,n2,p,L):
    a = ((n1+n2)/2)-(L/p) 
    ans = (p/4)*(-a+math.sqrt((a**2)-(8*(((n2-n1)/(2*math.pi))**2))))
    return ans

    print(center_distance(17,34,1.75,5))
