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

def center_distance(n1,n2,p,l):
    a = ((n1+n2)/2)-(l/p) 
    ans = (p/4)*(-a+math.sqrt((a**2)-(8*(((n2-n1)/(2*math.pi))**2))))
    return ans

def np_rc(n1,n2,p,c):
    a = (n2-n1)**2
    b = (4*(math.pi**2))*(c/p) 
    d = (2*c/p)+((n1+n2)/2)+(a/b)
    ans = round(d)
    return ans
    print(center_distance(17,34,1.75,5))


ansi_chain_number = [25, 35, 40, 41, 50, 60, 80, 100, 120, 140, 160, 180, 200, 240]                                                             
speed = [50, 100, 150, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1200, 1400, 1600, 1800, 2000, 2500, 3000]   

table =[
[0.05, 0.16, 0.37, 0.20, 0.72, 1.24, 2.88, 5.52, 9.33, 14.4, 20.9, 28.9, 38.4, 61.8],
[0.09, 0.29, 0.69, 0.38, 1.34, 2.31, 5.38, 10.3, 17.4, 26.9, 39.1, 54.0, 71.6, 115],
[0.13, 0.41, 0.99, 0.55, 1.92, 3.32, 7.75, 14.8, 25.1, 38.8, 56.3, 77.7, 103, 166], 
[0.16, 0.54, 1.29, 0.71, 2.50, 4.30, 10.0, 19.2, 32.5, 50.3, 72.9, 101, 134, 215],
[0.23, 0.78, 1.85, 1.02, 3.61, 6.20, 14.5, 27.7, 46.8, 72.4, 105, 145, 193, 310],
[0.30, 1.01, 2.40, 1.32, 4.67, 8.03, 18.7, 35.9, 60.6, 93.8, 136, 188, 249, 359],
[0.37, 1.24, 2.93, 1.61, 5.71, 9.81, 22.9, 43.9, 74.1, 115, 166, 204, 222, 0],
[0.44, 1.46, 3.45, 1.90, 6.72, 11.6, 27.0, 51.7, 87.3, 127, 141, 155, 169, 0],
[0.50, 1.68, 3.97, 2.18, 7.73, 13.3, 31.0, 59.4, 89.0, 101, 112, 123, 0, 0],
[0.56, 1.89, 4.48, 2.46, 8.71, 15.0, 35.0, 63.0, 72.8, 82.4, 91.7, 101, 0, 0],
[0.62, 2.10, 4.98, 2.74, 9.69, 16.7, 39.9, 52.8, 61.0, 69.1, 76.8, 84.4, 0, 0],
[0.68, 2.31, 5.48, 3.01, 10.7, 18.3, 37.7, 45.0, 52.1, 59.0, 65.6, 72.1, 0, 0],
[0.81, 2.73, 6.45, 3.29, 12.6, 21.6, 28.7, 34.3, 39.6, 44.9, 49.9, 0, 0, 0],
[0.93, 3.13, 7.41, 2.61, 14.4, 18.1, 22.7, 27.2, 31.5, 35.6, 0, 0, 0, 0],
[1.05, 3.53, 8.36, 2.14, 12.8, 14.8, 18.6, 22.3, 25.8, 0, 0, 0,0 , 0],
[1.16, 3.93, 8.96, 1.79, 10.7, 12.4, 15.6, 18.7, 21.6, 0, 0, 0, 0, 0], 
[1.27, 4.32, 7.72, 1.52, 9.23, 10.6, 13.3, 15.9, 0, 0, 0, 0, 0, 0], 
[1.56, 5.28, 5.51, 1.10, 6.58, 7.57, 9.56, 0.40, 0, 0, 0, 0, 0, 0], 
[1.84, 5.64, 4.17, 0.83, 4.98, 5.76, 7.25, 0, 0, 0, 0, 0, 0, 0]] 

table_types = [
["A","A", "A", "A", "A", "A", "A", "A", "A", "B", "B", "B", "B","B"],
["A","A", "A", "A", "A", "A", "A", "B", "B", "B", "B", "B", "B", "B"],
["A","A", "A", "A", "A", "A", "B", "B", "B", "B", "B", "B", "B", "B"],
["A","A", "A", "A", "A", "A", "B", "B", "B", "B", "B", "B", "B", "C"],
["A","A", "A", "A", "B", "B", "B", "B", "B", "B", "B", "C", "C′", "C′"],
["A","A", "B", "B", "B", "B", "B", "B", "B", "B", "C", "C", "C′", "C′"],
["A","A", "B", "B", "B", "B", "B", "B", "B", "C", "C", "C′", "C′", "ERROR"],
["A","A", "B", "B", "B", "B", "B", "B", "C", "C", "C", "C′", "C′", "ERROR"],
["A","B", "B", "B", "B", "B", "B", "B", "C", "C", "C", "C′", "ERROR", "ERROR"],
["A","B", "B", "B", "B", "B", "B", "B", "C", "C", "C", "C′", "ERROR", "ERROR"],
["A","B", "B", "B", "B", "B", "B", "C", "C", "C", "C′", "C′", "ERROR", "ERROR"],
["A","B", "B", "B", "B", "B", "B", "C", "C", "C", "C′", "C′", "ERROR", "ERROR"],
["A","B", "B", "B", "B", "B", "B", "C", "C", "C", "C′", "C′", "ERROR", "ERROR"],
["A","B", "B", "B", "B", "B", "B", "C", "C", "C", "C′", "C′", "ERROR", "ERROR"],
["A","B", "B", "B", "B", "B", "C", "C", "C", "C′", "C′", "ERROR", "ERROR", "ERROR"],
["A","B", "B", "B", "B", "B", "C", "C", "C", "C′", "ERROR", "ERROR", "ERROR", "ERROR"],
["A","B", "B", "B", "B", "B", "C", "C", "C′","ERROR", "ERROR", "ERROR", "ERROR", "ERROR"],
["B","B", "B", "B", "B", "C", "C", "C′", "C′","ERROR", "ERROR", "ERROR", "ERROR", "ERROR"],
["B","B", "B", "B", "B", "C", "C", "C′", "C′","ERROR", "ERROR", "ERROR", "ERROR", "ERROR"],
["B","B", "B", "B", "B", "C", "C", "C′", "ERROR","ERROR", "ERROR", "ERROR", "ERROR", "ERROR"],
["B","B", "B", "B", "C", "C", "C", "C′", "ERROR","ERROR", "ERROR", "ERROR", "ERROR", "ERROR"],
["B","B", "B", "B", "C", "C", "C′", "ERROR","ERROR","ERROR", "ERROR", "ERROR", "ERROR", "ERROR"]]


def chain_selection(hps, v):
    chain_answers = []
    type_answers = []
    for hp in hps:
        row_ind = speed.index(v)
        r = table[row_ind]
        r_nozero = [i for i in r if i != 0]
        for i in range(0, len(r)):
            #print(r[-1])
            
            if hp < r_nozero[0]:
                chain_answers.append(ansi_chain_number[0])
                type_answers.append(table_types[row_ind][0])
                break
            elif hp==r_nozero[-1]:
                chain_answers.append(ansi_chain_number[-1])
                type_answers.append(table_types[row_ind][-1])
                break
            elif hp > r_nozero[-1]:
                chain_answers.append("Not Found")
                type_answers.append("ERROR")
                break
            elif i != 13:
               last = i+1
               if hp < r[last]:
                   type_answers.append(table_types[row_ind][last])
                   chain_answers.append(ansi_chain_number[last])
                   break
    return chain_answers, type_answers
# TYPES return chain load.py


#lst =[0.1, 103, 70, 53, 45, 39, 30]
#lst =[0.1, 100/1.7, 100/2.5, 100/3.3, 100/3.9, 100/4.6, 100/6]
#x = [i for i in lst]
#a = chain_selection(lst , 300)

def ha_roller_chain(nd, ks, hnom, ncap, pre_or_post, v):
    k2s = [1, 1.7, 2.5, 3.3, 3.9, 4.6, 6]
    ans = [] 
    a = nd * ks * hnom
    if pre_or_post == "Pre-extreme Horsepower":
        k1 = (ncap/17)**1.08
        for i in range(len(k2s)):
            k2 = k2s[i]
            result = round(a / (k1 * k2), 3)
            ans.append(result)
    else:
        k1 = (ncap/17)**1.5
        for i in range(len(k2s)):
            k2 = k2s[i]
            result = round(a / (k1 * k2),3)
            ans.append(result)

    chains, types = chain_selection(ans, v)
    chains = [str(item) for item in chains]
    types = [str(item) for item in types]
    ans = [str(item) for item in ans]
    return ans, chains, types



def f_t_wire_rope(cap_w, w, l, a, d):
    # m = 1..10
    ans = []
    for this_d in d:
        row_ans = []
        for this_m in range(1, 11):
            row_ans.append(((cap_w/this_m) +(w*l*this_d**2))*(1+(a/32.2)))
        ans.append(row_ans)
    return ans


def f_f_wire_rope(ps, s, cap_d, d):

    ans = ((ps*s*d*cap_d)/2)
    return ans

def f_b_wire_rope(er, dw, am, cap_d):

    ans = ((er*dw*am)/(cap_d))
    return ans

def nf_wire_rope(cap_w, w, l, a, ps, su,cap_d, d, er, dw, am):
    ans = []
    for this_d in d:
        row_ans = []
        a = ((ps*su*this_d*cap_d)/2)
        b = ((er*dw*am)/(cap_d))
        for this_m in range(1, 11):
            c = ((cap_w/this_m) +(w*l))*(1+(a/32.2))
            row_ans.append((a-b)/c)
        ans.append(row_ans)
    return ans