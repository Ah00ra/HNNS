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


def minibi(sf,et,nu,dcap,tcap,t,f,phi):
    def degrees_to_radians(degrees):
        return degrees * (math.pi / 180)

    deltaf = (2*tcap)/dcap
    #a = (sf-(et/((1-(nu**2))*dcap))) * t
    x = et/((1-nu**2)*dcap)
    a = (sf - x)*t
    radianphi = degrees_to_radians(phi)
    minb = deltaf / a*math.exp(f*radianphi)/(math.exp(f*radianphi)-1)
    return minb




