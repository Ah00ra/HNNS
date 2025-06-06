from decimal import ROUND_UP
from encodings.punycode import selective_find
import math
from operator import index


def error_handling_decorator(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ZeroDivisionError:
            error = "Error: Division by zero is not allowed."
            return error      # or handle it as needed
        except ValueError:
            error = "Error: Invalid value provided."
            return error  # or handle it as needed
        except Exception as e:
            error = f"Error: {e}"
            return error  # or handle other exceptions as needed
    return wrapper


def torque(a,b,c,d):
    
    return str(a+b+c+d)


def spur_gear(h, d, n):
    ans = (60000*h)/(math.pi*d*n)
    return str(ans)


@error_handling_decorator
def open_belt(cd, d, c):
    tcd = math.pi - math.asin((cd-d)/(2*c))
    td = math.pi + math.asin((cd+d)/(2*c))
    l = math.sqrt(4*cd ** 2 - (cd - d) ** 2) + 1/2 * (cd*tcd + d*td)
    #TODO: write andis
    tcd = round(tcd,3)
    td = round(td,3)
    l = round(l,3)
    ans = f"""theta D = {tcd}
θd = ϕ = {td}  
L = {l}
"""
    return ans

@error_handling_decorator
def crossed_belt(cd, d, c):
    td = math.pi + math.asin((cd+d)/(2*c))
    l = math.sqrt(4*cd ** 2 - (cd - d) ** 2) + 1/2 * ((cd + d)*td)
    td = round(td,3)
    l = round(l,3)
    ans = f"θ,L = {td}, {l}"

    return ans


@error_handling_decorator
def belt_speed(d, n):
    ans = (math.pi * d * n)/12

    return ans


@error_handling_decorator
def fc_belt(w, v):
    g =32.17 
    ans = (w/g)*((v/60)**2)
    return ans


@error_handling_decorator
def omg(y,b,t):
    ans = 12*y*b*t
    return ans

@error_handling_decorator
def expphi(phi, f):
    ans = math.exp(phi*f)
    return ans

@error_handling_decorator
def TorqueBelt(H_nom,K_s,n_d,n):
    ans = ((63025*H_nom*K_s*n_d))/n
    return ans

@error_handling_decorator
#TODO: check if it wasn't error
def f1a_f2(T,d):
    ans = (2*T)/d
    return ans


@error_handling_decorator
def fi(t,d,f,phi,):
    ans = (t/d*(((math.exp(f*phi)+1)/((math.exp(f*phi)-1))))) 
    return ans

@error_handling_decorator
def fi2(fc,f2_p,f1a_p):
    ans = (((f2_p+f1a_p)/2)-fc)
    return ans

@error_handling_decorator
def f2(f1a_p,f1ap_f2):
    ans = ((f1a_p)-(f1ap_f2))
    return ans

@error_handling_decorator
def f1a(b,fa,cv,cp):
    ans = (b*fa*cv*cp)
    return ans

@error_handling_decorator
def f_prime(phi,f1a_p,fc,f2):
    ans =((1/phi)*(math.log((f1a_p-fc)/(f2-fc))))    
    return ans


@error_handling_decorator
def dip(c,w,fi_p,):
    ans =(((c**2)*w)/(96*fi_p))   
    return ans


error_handling_decorator
def sfnp(np):
    ans = 14.17*1000000*(1000000)**-0.407
    ans =f"{ans} Psi" 
    return ans


error_handling_decorator
def sfsy(sy):
    ans = sy/3
    ans =f"{ans} Psi" 
    return ans

def degrees_to_radians(degrees):
    return degrees * (math.pi / 180)


@error_handling_decorator
def minibi(sf,et,nu,dcap,tcap,t,f,phi):

    deltaf = (2*tcap)/dcap
    #a = (sf-(et/((1-(nu**2))*dcap))) * t
    x = et/((1-nu**2)*dcap)
    a = (sf - x)*t
    radianphi = degrees_to_radians(phi)
    minb = deltaf / a*math.exp(f*radianphi)/(math.exp(f*radianphi)-1)
    ans =f"{minb} in" 
    return ans

@error_handling_decorator
def f1pa(sf, et, nu, dcap, t, b):
    x = et/((1-nu**2)*dcap)
    ab = (sf - x)*t*b
    ans =f"{ab} N" 
    return ans


@error_handling_decorator
def deltaf(capt, capd):
    ans = 2*capt/capd
    return ans 

@error_handling_decorator
def f2metalbelt(sf,et,nu,dcap,tcap,t,b):
    x = et/((1-nu**2)*dcap)
    ab = (sf - x)*t*b
    delf = 2*tcap/dcap
    ans = ab - delf
    return ans

@error_handling_decorator
def fi_2(sf,et,nu,dcap,tcap,t,b):
    x = et/((1-nu**2)*dcap)
    ab = (sf - x)*t*b
    delf = 2*tcap/dcap
    ans = ab - (delf/2)
    return ans


@error_handling_decorator
def fprime2(sf,et,nu,dcap,tcap,t,b, phi):
    f1a = f1pa(sf,et,nu,dcap,t,b) 
    f2 = f2metalbelt(sf,et,nu,dcap,tcap,t,b)
    radian_phi = degrees_to_radians(phi)
    ans = (1/radian_phi)*math.log(f1a/f2)
    return ans


@error_handling_decorator
def h_link_plate(N,n,p):
    a = N**1.08
    b = (n**0.9)
    c = 3-(0.07*p)
    ans = 0.004*a*b*(p**c)
    ans =f"{ans} Hp" 
    return ans

@error_handling_decorator
def center_distance(n1,n2,p,l):
    a = ((n1+n2)/2)-(l/p) 
    ans = (p/4)*(-a+math.sqrt((a**2)-(8*(((n2-n1)/(2*math.pi))**2))))
    ans =f"{ans} in" 
    return ans

@error_handling_decorator
def np_rc(n1,n2,p,c):
    a = (n2-n1)**2
    b = (4*(math.pi**2))*(c/p) 
    d = (2*c/p)+((n1+n2)/2)+(a/b)
    ans = round(d)
    return ans


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
    try:
        row_ind = speed.index(v)
    except ValueError:
        chain_answers, type_answers = chain_selection_int_speed(v, hps)
        return chain_answers, type_answers

    for hp in hps:
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



def chain_selection_int_speed(v, hps):
    chain_answers = []
    type_answers = []
    
    if v > 50 and v < 100:
        a = (v/1250) + 1/100
        b = ((13*v)/5000) + (3/100)
        c = ((4*v)/625) + (1/20)
        d = ((9*v)/2500) + (1/50)
        e = (31*v)/2500 + 1/10
        f = (107*v)/5000 + 17/100
        g = (v/20) + 19/50
        h = (239*v)/2500 + 37/50 
        i = (807*v)/5000 + 63/50 
        j = (v/4) + 19/10
        k = (91*v)/250 + 27/10
        l = (251*v)/500 + 19/5
        m = (83*v)/125 + 26/5
        n = (133*v)/125 + 43/5

        def selection(ansi_chain_hp_int_speed, hp_list):
            for hp in hp_list:  
                if hp < ansi_chain_hp_int_speed[0]:  
                    chain_answers.append(ansi_chain_number_int_speed[0])  
                    type_answers.append("A")

                elif hp > ansi_chain_hp_int_speed[-1]:
                    chain_answers.append("Not found")  
                    type_answers.append("ERROR")

                else:
                    for i, num in enumerate(ansi_chain_hp_int_speed):
                        if num > hp:
                            chain_answers.append(ansi_chain_number_int_speed[i])
                            break  
                    if i < 7:
                        type_answers.append("A")
                    elif i == 7 or i == 8 :
                        type_answers.append("A or B")
                    else:
                        type_answers.append("B")
            return chain_answers,type_answers


        ansi_chain_hp_int_speed = [a, b, c, d, e, f, g, h, i, j, k, l, m, n]
        ansi_chain_number_int_speed = [25, 35, 40, 41, 50, 60, 80, 100, 120, 140, 160, 180, 200, 240]

        chain_answers, type_answers = selection(ansi_chain_hp_int_speed, hps)
        return chain_answers, type_answers

    elif v > 100 and v < 150:
        a = (1291*v)/5000 - 2573/100    
        b = (3*v)/1250 + 1/20
        c = (3*v)/500 + 9/100
        d = (17*v)/5000 + 1/25
        e = (29*v)/2500 + 9/50
        f = (101*v)/5000 + 29/100
        g = (237*v)/5000 + 16/25
        h = (9*v)/100 + 13/10 
        i = (77*v)/500 + 2 
        j = (119*v)/500 + 31/10
        k = (43*v)/125 + 47/10
        l = (237*v)/500 + 33/5
        m = (157*v)/250 + 44/5
        n = (51*v)/50 + 13
        
        ansi_chain_hp_int_speed = [a, b, c, d, e, f, g, h, i, j, k, l, m, n]

        def selection(ansi_chain_hp_int_speed, hp_list):
            for hp in hp_list:  
                if hp < ansi_chain_hp_int_speed[0]:  
                    chain_answers.append(ansi_chain_number_int_speed[0])  
                    type_answers.append("A")

                elif hp > ansi_chain_hp_int_speed[-1]:
                    chain_answers.append("Not found")  
                    type_answers.append("ERROR")

                else:
                    for i, num in enumerate(ansi_chain_hp_int_speed):
                        if num > hp:
                            chain_answers.append(ansi_chain_number_int_speed[i])
                            break  
                    if i < 6 :
                        type_answers.append("A")
                    elif i == 6 :
                        type_answers.append("A or B")
                    else :
                        type_answers.append("B")
            return chain_answers,type_answers


        ansi_chain_hp_int_speed = [a, b, c, d, e, f, g, h, i, j, k, l, m, n]
        ansi_chain_number_int_speed = [25, 35, 40, 41, 50, 60, 80, 100, 120, 140, 160, 180, 200, 240]

        chain_answers, type_answers = selection(ansi_chain_hp_int_speed, hps)
        return chain_answers, type_answers
    
    elif v > 150 and v < 200:
        a = (3*v)/5000 + 1/25    
        b = (13*v)/5000 + 5764607523034075/288230376151711744
        c = (3*v)/500 + 9/100
        d = (2*v)/625 + 7/100
        e = (29*v)/2500 + 9/50
        f = (49*v)/2500 + 19/50
        g = (9*v)/200 + 1
        h = (11*v)/125 + 8/5 
        i = (37*v)/250 + 29/10
        j = (23*v)/100 + 43/10
        k = (83*v)/250 + 13/2
        l = (233*v)/500 + 39/5
        m = (31*v)/50 + 10
        n = (49*v)/50 + 19

        ansi_chain_hp_int_speed = [a, b, c, d, e, f, g, h, i, j, k, l, m, n]

        def selection(ansi_chain_hp_int_speed, hp_list):
            for hp in hp_list:  
                if hp < ansi_chain_hp_int_speed[0]:  
                    chain_answers.append(ansi_chain_number_int_speed[0])  
                    type_answers.append("A")

                elif hp > ansi_chain_hp_int_speed[-1]:
                    chain_answers.append("Not found")  
                    type_answers.append("ERROR")

                else:
                    for i, num in enumerate(ansi_chain_hp_int_speed):
                        if num > hp:
                            chain_answers.append(ansi_chain_number_int_speed[i])
                            break  
                    if i < 6 :
                        type_answers.append("A")
                    else :
                        type_answers.append("B")
            return chain_answers,type_answers


        ansi_chain_hp_int_speed = [a, b, c, d, e, f, g, h, i, j, k, l, m, n]
        ansi_chain_number_int_speed = [25, 35, 40, 41, 50, 60, 80, 100, 120, 140, 160, 180, 200, 240]
    
        chain_answers, type_answers = selection(ansi_chain_hp_int_speed, hps)
        return chain_answers, type_answers 

    elif v > 200 and v < 300:

        a = (7*v)/10000 + 1/50   
        b = (3*v)/1250 + 3/50
        c = (7*v)/1250 + 17/100
        d = (31*v)/10000 + 9/100
        e = (111*v)/10000 + 7/25
        f = (19*v)/1000 + 1/2
        g = (9*v)/200 + 1
        h = (17*v)/200 + 11/5
        i = (143*v)/1000 + 39/10
        j = (221*v)/1000 + 61/10
        k = (321*v)/1000 + 87/10
        l = (11*v)/25 + 13
        m = (59*v)/100 + 16
        n = (19*v)/20 + 25
        ansi_chain_hp_int_speed = [a, b, c, d, e, f, g, h, i, j, k, l, m, n]

        def selection(ansi_chain_hp_int_speed, hp_list):
            for hp in hp_list:  
                if hp < ansi_chain_hp_int_speed[0]:  
                    chain_answers.append(ansi_chain_number_int_speed[0])  
                    type_answers.append("A")

                elif hp > ansi_chain_hp_int_speed[-1]:
                    chain_answers.append("Not found")  
                    type_answers.append("ERROR")

                else:
                    for i, num in enumerate(ansi_chain_hp_int_speed):
                        if num > hp:
                            chain_answers.append(ansi_chain_number_int_speed[i])
                            break  
                    if i < 4:
                        type_answers.append("A")
                    elif i == 4 or i == 5:
                        type_answers.append("A or B")    
                    elif i > 5 and i < 11 : 
                        type_answers.append("B")
                    elif i == 11:
                        type_answers.append("B or C")    
                    elif i == 12:
                        type_answers.append("B or C'")
                    else:
                        type_answers.append("C'")
    

            return chain_answers,type_answers


        ansi_chain_hp_int_speed = [a, b, c, d, e, f, g, h, i, j, k, l, m, n]
        ansi_chain_number_int_speed = [25, 35, 40, 41, 50, 60, 80, 100, 120, 140, 160, 180, 200, 240]

        chain_answers, type_answers = selection(ansi_chain_hp_int_speed, hps)
        return chain_answers, type_answers 

    
    elif v > 300 and v < 400:

        a = (7*v)/10000 + 9/100
        b = (23*v)/10000 + 8/25
        c = (11*v)/2000 + 3/4
        d = (3*v)/1000 + 21/50
        e = (23*v)/2000 + 131/100
        f = (183*v)/10000 + 127/50
        g = (21*v)/500 + 61/10
        h = (41*v)/500 + 113/10
        i = (69*v)/500 + 96/5
        j = (107*v)/500 + 148/5
        k = (31*v)/100 + 43
        l = (43*v)/100 + 59
        m = (14*v)/25 + 81
        n = (49*v)/100 + 212

        ansi_chain_hp_int_speed = [a, b, c, d, e, f, g, h, i, j, k, l, m, n]

        def selection(ansi_chain_hp_int_speed, hp_list):
            for hp in hp_list:  
                if hp < ansi_chain_hp_int_speed[0]:  
                    chain_answers.append(ansi_chain_number_int_speed[0])  
                    type_answers.append("A")

                elif hp > ansi_chain_hp_int_speed[-1]:
                    chain_answers.append("Not found")  
                    type_answers.append("ERROR")

                else:
                    for i, num in enumerate(ansi_chain_hp_int_speed):
                        if num > hp:
                            chain_answers.append(ansi_chain_number_int_speed[i])
                            break  
                    if i < 2:
                        type_answers.append("A")
                    elif i == 2 or i == 3:
                        type_answers.append("A or B")    
                    elif i > 3 and i < 10 : 
                        type_answers.append("B")
                    elif i == 10:
                        type_answers.append("B or C")    
                    elif i == 11:
                        type_answers.append("C")
                    else:
                        type_answers.append("C'")
    

            return chain_answers,type_answers


        ansi_chain_hp_int_speed = [a, b, c, d, e, f, g, h, i, j, k, l, m, n]
        ansi_chain_number_int_speed = [25, 35, 40, 41, 50, 60, 80, 100, 120, 140, 160, 180, 200, 240]

        chain_answers, type_answers = selection(ansi_chain_hp_int_speed, hps)
        return chain_answers, type_answers 

    elif v > 400 and v < 500:

        a = (7*v)/10000 + 1/50
        b = (23*v)/10000 + 9/100
        c = (53*v)/10000 + 7/25
        d = (29*v)/10000 + 4/25
        e = (13*v)/1250 + 51/100
        f = (89*v)/5000 + 91/100
        g = (21*v)/500 + 19/10
        h = (2*v)/25 + 39/10
        i = (27*v)/200 + 33/5
        j = (53*v)/250 + 9
        k = (3*v)/10 + 16
        l = (4*v)/25 + 124
        m = 357 - (27*v)/100
        n = 4337/5 - (1271*v)/1000

        ansi_chain_hp_int_speed = [a, b, c, d, e, f, g, h, i, j, k, l, m, n]

        def selection(ansi_chain_hp_int_speed, hp_list):
            for hp in hp_list:  
                if hp < ansi_chain_hp_int_speed[0]:  
                    chain_answers.append(ansi_chain_number_int_speed[0])  
                    type_answers.append("A")

                elif hp > ansi_chain_hp_int_speed[-1]:
                    chain_answers.append("Not found")  
                    type_answers.append("ERROR")

                else:
                    for i, num in enumerate(ansi_chain_hp_int_speed):
                        if num > hp:
                            chain_answers.append(ansi_chain_number_int_speed[i])
                            break  
                    if i < 2:
                        type_answers.append("A")
                    elif i >= 2 and i < 9:
                        type_answers.append("B")    
                    elif i ==9 : 
                        type_answers.append("B or C")
                    elif i == 10:
                        type_answers.append("C")    
                    elif i == 11:
                        type_answers.append("C or C'")
                    else:
                        type_answers.append("C'")
    

            return chain_answers,type_answers


        ansi_chain_hp_int_speed = [a, b, c, d, e, f, g, h, i, j, k, l, m, n]
        ansi_chain_number_int_speed = [25, 35, 40, 41, 50, 60, 80, 100, 120, 140, 160, 180, 200]
        chain_answers, type_answers = selection(ansi_chain_hp_int_speed, hps)

        return chain_answers, type_answers 
    
    elif v > 500 and v < 600:

        a = (7*v)/10000 + 1/50
        b = (11*v)/5000 + 7/50
        c = (13*v)/2500 + 33/100
        d = (29*v)/10000 + 4/25
        e = (101*v)/10000 + 33/50
        f = (179*v)/10000 + 43/50
        g = (41*v)/1000 + 12/5
        h = (39*v)/500 + 49/10
        i = (33*v)/250 + 81/10
        j = (3*v)/25 + 55
        k = 291 - v/4
        l = 449 - (49*v)/100
        m = 487 - (53*v)/100

        ansi_chain_hp_int_speed = [a, b, c, d, e, f, g, h, i, j, k, l, m]

        def selection(ansi_chain_hp_int_speed, hp_list):
            for hp in hp_list:  
                if hp < ansi_chain_hp_int_speed[0]:  
                    chain_answers.append(ansi_chain_number_int_speed[0])  
                    type_answers.append("A")

                elif hp > ansi_chain_hp_int_speed[-1]:
                    chain_answers.append("Not found")  
                    type_answers.append("ERROR")

                else:
                    for i, num in enumerate(ansi_chain_hp_int_speed):
                        if num > hp:
                            chain_answers.append(ansi_chain_number_int_speed[i])
                            break  
                    if i < 2:
                        type_answers.append("A")
                    elif i >= 2 and i < 8:
                        type_answers.append("B")    
                    elif i ==8 : 
                        type_answers.append("B or C")
                    elif i == 10 or i == 11:
                        type_answers.append("C")    
                    else:
                        type_answers.append("C'")
            return chain_answers,type_answers



        ansi_chain_hp_int_speed = [a, b, c, d, e, f, g, h, i, j, k, l, m]
        ansi_chain_number_int_speed = [25, 35, 40, 41, 50, 60, 80, 100, 120, 140, 160, 180, 200]

        chain_answers, type_answers = selection(ansi_chain_hp_int_speed, hps)
        return chain_answers, type_answers 

    elif v > 600 and v < 700:

        a = (3*v)/5000 + 2/25
        b = (11*v)/5000 + 7/50
        c = (13*v)/2500 + 33/100
        d = (7*v)/2500 + 11/50
        e = (101*v)/10000 + 33/50
        f = (17*v)/1000 + 7/5
        g = v/25 + 3
        h = (77*v)/1000 + 11/2
        i = (17*v)/1000 + 771/10
        j = 283 - (13*v)/50
        k = 315 - (29*v)/100
        l = 347 - (8*v)/25
        m = 305 - (17*v)/50


        ansi_chain_hp_int_speed = [a, b, c, d, e, f, g, h, i, j, k, l, m]

        def selection(ansi_chain_hp_int_speed, hp_list):
            for hp in hp_list:  
                if hp < ansi_chain_hp_int_speed[0]:  
                    chain_answers.append(ansi_chain_number_int_speed[0])  
                    type_answers.append("A")

                elif hp > ansi_chain_hp_int_speed[-1]:
                    chain_answers.append("Not found")  
                    type_answers.append("ERROR")

                else:
                    for i, num in enumerate(ansi_chain_hp_int_speed):
                        if num > hp:
                            chain_answers.append(ansi_chain_number_int_speed[i])
                            break  
                    if i < 1:
                        type_answers.append("A")
                    elif i == 1 :
                        type_answers.append("A or B")    
                    elif i > 1 and i < 8 : 
                        type_answers.append("B")
                    elif i > 7 and i < 11:
                        type_answers.append("C")    
                    else:
                        type_answers.append("C'")
    

            return chain_answers,type_answers


        ansi_chain_hp_int_speed = [a, b, c, d, e, f, g, h, i, j, k, l, m]
        ansi_chain_number_int_speed = [25, 35, 40, 41, 50, 60, 80, 100, 120, 140, 160, 180, 200]

        chain_answers, type_answers = selection(ansi_chain_hp_int_speed, hps)
        return chain_answers, type_answers 

    elif v > 700 and v < 800:

        a = (3*v)/5000 + 2/25
        b = (21*v)/10000 + 21/100
        c = (51*v)/10000 + 2/5
        d = (7*v)/2500 + 11/50
        e = (49*v)/5000 + 87/100
        f = (17*v)/1000 + 1.4
        g = v/25 + 3
        h = (9*v)/250 + 171/5
        i = 1012/5 - (81*v)/500
        j = 1156/5 - (93*v)/500
        k = 2541/10 - (203*v)/1000
        l = 277 - (11*v)/50



        ansi_chain_hp_int_speed = [a, b, c, d, e, f, g, h, i, j, k, l]

        def selection(ansi_chain_hp_int_speed, hp_list):
            for hp in hp_list:  
                if hp < ansi_chain_hp_int_speed[0]:  
                    chain_answers.append(ansi_chain_number_int_speed[0])  
                    type_answers.append("A")

                elif hp > ansi_chain_hp_int_speed[-1]:
                    chain_answers.append("Not found")  
                    type_answers.append("ERROR")

                else:
                    for i, num in enumerate(ansi_chain_hp_int_speed):
                        if num > hp:
                            chain_answers.append(ansi_chain_number_int_speed[i])
                            break  
                    if i < 1:
                        type_answers.append("A")   
                    elif i > 0 and i < 7 : 
                        type_answers.append("B")
                    elif i == 7 :
                        type_answers.append("B or C")
                    elif i == 8 or i == 9 :
                        type_answers.append("C")
                    elif i == 7 :
                        type_answers.append("C or C'")        
                    else:
                        type_answers.append("C'")
    

            return chain_answers,type_answers


        ansi_chain_hp_int_speed = [a, b, c, d, e, f, g, h, i, j, k, l]
        ansi_chain_number_int_speed = [25, 35, 40, 41, 50, 60, 80, 100, 120, 140, 160, 180, 200]

        chain_answers, type_answers = selection(ansi_chain_hp_int_speed, hps)
        return chain_answers, type_answers 


    elif v > 800 and v < 900:

        a = (3*v)/5000 + 2/25
        b = (21*v)/10000 + 21/100
        c = v/200 + 12/25
        d = (7*v)/2500 + 11/50
        e = (49*v)/5000 + 0.87
        f = (17*v)/1000 + 7/5
        g = (49*v)/1000 - 21/5
        h = 723/5 - (51*v)/500
        i = 836/5 - (59*v)/500
        j = 944/5 - (133*v)/1000
        k = 2109/10 - (149*v)/1000
        l = 1169/5 - (83*v)/500


        ansi_chain_hp_int_speed = [a, b, c, d, e, f, g, h, i, j, k, l]

        def selection(ansi_chain_hp_int_speed, hp_list):
            for hp in hp_list:  
                if hp < ansi_chain_hp_int_speed[0]:  
                    chain_answers.append(ansi_chain_number_int_speed[0])  
                    type_answers.append("A")

                elif hp > ansi_chain_hp_int_speed[-1]:
                    chain_answers.append("Not found")  
                    type_answers.append("ERROR")

                else:
                    for i, num in enumerate(ansi_chain_hp_int_speed):
                        if num > hp:
                            chain_answers.append(ansi_chain_number_int_speed[i])
                            break  
                    if i < 1:
                        type_answers.append("A")   
                    elif i > 0 and i < 7 : 
                        type_answers.append("B")
                    elif i > 6 and i < 10 :
                        type_answers.append("C")        
                    else:
                        type_answers.append("C'")
    

            return chain_answers,type_answers


        ansi_chain_hp_int_speed = [a, b, c, d, e, f, g, h, i, j, k, l]
        ansi_chain_number_int_speed = [25, 35, 40, 41, 50, 60, 80, 100, 120, 140, 160, 180, 200]


        chain_answers, type_answers = selection(ansi_chain_hp_int_speed, hps)
        return chain_answers, type_answers 
    
    elif v > 900 and v < 1000:

        a = (3*v)/5000 + 7/50
        b = (21*v)/10000 + 21/100
        c = v/200 + 12/25
        d = (27*v)/10000 + 31/100
        e = (101*v)/10000 + 3/5
        f = (2*v)/125 + 2.29
        g = 597/10 - (11*v)/500
        h = 123 - (39*v)/500
        i = 1411/10 - (89*v)/1000
        j = 160 - (101*v)/1000
        k = 888/5 - (14*v)/125
        l = 1951/10 - (123*v)/1000



        ansi_chain_hp_int_speed = [a, b, c, d, e, f, g, h, i, j, k, l]

        def selection(ansi_chain_hp_int_speed, hp_list):
            for hp in hp_list:  
                if hp < ansi_chain_hp_int_speed[0]:  
                    chain_answers.append(ansi_chain_number_int_speed[0])  
                    type_answers.append("A")

                elif hp > ansi_chain_hp_int_speed[-1]:
                    chain_answers.append("Not found")  
                    type_answers.append("ERROR")

                else:
                    for i, num in enumerate(ansi_chain_hp_int_speed):
                        if num > hp:
                            chain_answers.append(ansi_chain_number_int_speed[i])
                            break  
                    if i < 1:
                        type_answers.append("A")   
                    elif i > 0 and i < 7 : 
                        type_answers.append("B")
                    elif i > 6 and i < 10 :
                        type_answers.append("C")        
                    else:
                        type_answers.append("C'")
    

            return chain_answers,type_answers


        ansi_chain_hp_int_speed = [a, b, c, d, e, f, g, h, i, j, k, l]
        ansi_chain_number_int_speed = [25, 35, 40, 41, 50, 60, 80, 100, 120, 140, 160, 180, 200]


        chain_answers, type_answers = selection(ansi_chain_hp_int_speed, hps)
        return chain_answers, type_answers 



    elif v > 1000 and v < 1200:

        a = (13*v)/20000 + 0.299
        b = (21*v)/10000 + 21/100
        c = (97*v)/20000 + 63/100
        d = (7*v)/5000 + 161/100
        e = (19*v)/2000 + 6/5
        f = (33*v)/2000 + 9/5
        g = 827/10 - (9*v)/200
        h = 197/2 - (107*v)/2000
        i = 573/5 - (v/16)
        j = 259/2 - (141*v)/2000
        k = 1441/10 - (157*v)/2000
        l = 3231/20 - (1789*v)/20000




        ansi_chain_hp_int_speed = [a, b, c, d, e, f, g, h, i, j, k, l]

        def selection(ansi_chain_hp_int_speed, hp_list):
            for hp in hp_list:  
                if hp < ansi_chain_hp_int_speed[0]:  
                    chain_answers.append(ansi_chain_number_int_speed[0])  
                    type_answers.append("A")

                elif hp > ansi_chain_hp_int_speed[-1]:
                    chain_answers.append("Not found")  
                    type_answers.append("ERROR")

                else:
                    for i, num in enumerate(ansi_chain_hp_int_speed):
                        if num > hp:
                            chain_answers.append(ansi_chain_number_int_speed[i])
                            break  
                    if i < 1:
                        type_answers.append("A")   
                    elif i > 0 and i < 7 : 
                        type_answers.append("B")
                    elif i > 6 and i < 10 :
                        type_answers.append("C")        
                    else:
                        type_answers.append("C'")
    

            return chain_answers,type_answers


        ansi_chain_hp_int_speed = [a, b, c, d, e, f, g, h, i, j, k, l]
        ansi_chain_number_int_speed = [25, 35, 40, 41, 50, 60, 80, 100, 120, 140, 160, 180, 200]

        chain_answers, type_answers = selection(ansi_chain_hp_int_speed, hps)
        return chain_answers, type_answers 
    
    elif v > 1200 and v < 1400:

        a = (3*v)/5000 + 9/100
        b = v/500 + 33/100
        c = (3*v)/625 + 69/100
        d = 737/100 - (17*v)/5000
        e = (9*v)/1000 + 9/5
        f = 213/5 - (7*v)/400
        g = 647/10 - (3*v)/100
        h = 769/10 - (71*v)/2000
        i = 441/5 - (81*v)/2000
        j = 1007/10 - (93*v)/2000
        k = 1111/10 - (51*v)/1000

        ansi_chain_hp_int_speed = [a, b, c, d, e, f, g, h, i, j, k]

        def selection(ansi_chain_hp_int_speed, hp_list):
            for hp in hp_list:  
                if hp < ansi_chain_hp_int_speed[0]:  
                    chain_answers.append(ansi_chain_number_int_speed[0])  
                    type_answers.append("A")

                elif hp > ansi_chain_hp_int_speed[-1]:
                    chain_answers.append("Not found")  
                    type_answers.append("ERROR")

                else:
                    for i, num in enumerate(ansi_chain_hp_int_speed):
                        if num > hp:
                            chain_answers.append(ansi_chain_number_int_speed[i])
                            break  
                    if i < 1:
                        type_answers.append("A")   
                    elif i > 0 and i < 6 : 
                        type_answers.append("B")
                    elif i > 5 and i < 9 :
                        type_answers.append("C")        
                    else:
                        type_answers.append("C'")
    

            return chain_answers,type_answers


        ansi_chain_hp_int_speed = [a, b, c, d, e, f, g, h, i, j, k]
        ansi_chain_number_int_speed = [25, 35, 40, 41, 50, 60, 80, 100, 120, 140, 160]

        chain_answers, type_answers = selection(ansi_chain_hp_int_speed, hps)
        return chain_answers, type_answers
    
    elif v > 1400 and v < 1600:

        a = (3*v)/5000 + 9/100
        b = v/500 + 33/100
        c = (19*v)/4000 + 19/25
        d = 59/10 - (47*v)/20000
        e = 128/5 - v/125
        f = 206/5 - (33*v)/2000
        g = 257/5 - (41*v)/2000
        h = 123/2 - (49*v)/2000
        i =357/5 - (57*v)/2000
        j =797/10 - (63*v)/2000
 

        ansi_chain_hp_int_speed = [a, b, c, d, e, f, g, h, i, j]

        def selection(ansi_chain_hp_int_speed, hp_list):
            for hp in hp_list:  
                if hp < ansi_chain_hp_int_speed[0]:  
                    chain_answers.append(ansi_chain_number_int_speed[0])  
                    type_answers.append("A")

                elif hp > ansi_chain_hp_int_speed[-1]:
                    chain_answers.append("Not found")  
                    type_answers.append("ERROR")

                else:
                    for i, num in enumerate(ansi_chain_hp_int_speed):
                        if num > hp:
                            chain_answers.append(ansi_chain_number_int_speed[i])
                            break  
                    if i < 1:
                        type_answers.append("A")   
                    elif i > 0 and i < 6 : 
                        type_answers.append("B")
                    elif i == 6 and i == 7:
                        type_answers.append("C") 
                    elif i == 8:
                        type_answers.append("C or C'")           
                    else:
                        type_answers.append("C'")
    

            return chain_answers,type_answers


        ansi_chain_hp_int_speed = [a, b, c, d, e, f, g, h, i, j]
        ansi_chain_number_int_speed = [25, 35, 40, 41, 50, 60, 80, 100, 120, 140]

        chain_answers, type_answers = selection(ansi_chain_hp_int_speed, hps)
        return chain_answers, type_answers
    
    elif v > 1600 and v < 1800:

        a = (11*v)/20000 + 17/100
        b = v/500 + 33/100
        c = (3*v)/1000 + 89/25
        d = 247/50 - (7*v)/4000
        e = 148/5 - (21*v)/2000
        f = 34 - (3*v)/250
        g = 213/5 - (3*v)/200
        h = 511/10 - (9*v)/500
        i = 297/5 - (21*v)/1000
 
        ansi_chain_hp_int_speed = [a, b, c, d, e, f, g, h, i]

        def selection(ansi_chain_hp_int_speed, hp_list):
            for hp in hp_list:  
                if hp < ansi_chain_hp_int_speed[0]:  
                    chain_answers.append(ansi_chain_number_int_speed[0])  
                    type_answers.append("B")

                elif hp > ansi_chain_hp_int_speed[-1]:
                    chain_answers.append("Not found")  
                    type_answers.append("ERROR")

                else:
                    for i, num in enumerate(ansi_chain_hp_int_speed):
                        if num > hp:
                            chain_answers.append(ansi_chain_number_int_speed[i])
                            break  
                    if i < 1:
                        type_answers.append("A or B")   
                    elif i > 0 and i < 5 : 
                        type_answers.append("B")
                    elif i == 5 :
                        type_answers.append("B or C") 
                    elif i == 6:
                        type_answers.append("C")
                    elif i == 7:
                        type_answers.append("C or C'")               
                    else:
                        type_answers.append("C'")
    

            return chain_answers,type_answers


        ansi_chain_hp_int_speed = [a, b, c, d, e, f, g, h, i]
        ansi_chain_number_int_speed = [25, 35, 40, 41, 50, 60, 80, 100, 120]

        chain_answers, type_answers = selection(ansi_chain_hp_int_speed, hps)
        return chain_answers, type_answers

    elif v > 1800 and v < 2000:

        a = (11*v)/20000 + 17/100
        b = (39*v)/20000 + 0.419
        c = 503/25 - (31*v)/5000
        d = 211/50 - (27*v)/20000
        e = 2393/100 - (147*v)/20000
        f = 143/5 - (9*v)/1000
        g = 363/10 - (23*v)/2000
        h = 439/10 - (7*v)/500
        i = 252/5 - (2*v)/125

 
        ansi_chain_hp_int_speed = [a, b, c, d, e, f, g, h, i]

        def selection(ansi_chain_hp_int_speed, hp_list):
            for hp in hp_list:  
                if hp < ansi_chain_hp_int_speed[0]:  
                    chain_answers.append(ansi_chain_number_int_speed[0])  
                    type_answers.append("B")

                elif hp > ansi_chain_hp_int_speed[-1]:
                    chain_answers.append("Not found")  
                    type_answers.append("ERROR")

                else:
                    for i, num in enumerate(ansi_chain_hp_int_speed):
                        if num > hp:
                            chain_answers.append(ansi_chain_number_int_speed[i])
                            break  
                    if i < 5:
                        type_answers.append("B")   
                    elif i > 0 and i < 6 : 
                        type_answers.append("B")
                    elif i == 6 and i == 7:
                        type_answers.append("C")            
                    else:
                        type_answers.append("C'")
    

            return chain_answers,type_answers


        ansi_chain_hp_int_speed = [a, b, c, d, e, f, g, h, i]
        ansi_chain_number_int_speed = [25, 35, 40, 41, 50, 60, 80, 100, 120]

        chain_answers, type_answers = selection(ansi_chain_hp_int_speed, hps)
        return chain_answers, type_answers

    elif v > 2000 and v < 2500:

        a = (29*v)/50000 + 11/100
        b = (6*v)/3125 + 12/25
        c = 414/25 - (221*v)/50000
        d = 16/5 - (21*v)/25000
        e = 1983/100 - (53*v)/10000
        f = 568/25 - (303*v)/50000
        g = 1413/50 - (187*v)/25000
        h = 779/10 - (31*v)/1000

 
        ansi_chain_hp_int_speed = [a, b, c, d, e, f, g, h]

        def selection(ansi_chain_hp_int_speed, hp_list):
            for hp in hp_list:  
                if hp < ansi_chain_hp_int_speed[0]:  
                    chain_answers.append(ansi_chain_number_int_speed[0])  
                    type_answers.append("B")

                elif hp > ansi_chain_hp_int_speed[-1]:
                    chain_answers.append("Not found")  
                    type_answers.append("ERROR")

                else:
                    for i, num in enumerate(ansi_chain_hp_int_speed):
                        if num > hp:
                            chain_answers.append(ansi_chain_number_int_speed[i])
                            break  
                    if i < 5:
                        type_answers.append("B")   
                    elif i == 4 : 
                        type_answers.append("B or C")
                    elif i == 5 or i == 6:
                        type_answers.append("C")            
                    else:
                        type_answers.append("C'")
    

            return chain_answers,type_answers


        ansi_chain_hp_int_speed = [a, b, c, d, e, f, g, h,]
        ansi_chain_number_int_speed = [25, 35, 40, 41, 50, 60, 80, 100]

        chain_answers, type_answers = selection(ansi_chain_hp_int_speed, hps)
        return chain_answers, type_answers

    elif v > 2500 and v < 3000:

        a = (7*v)/12500 + 4/25
        b = (9*v)/12500 + 87/25
        c = 1221/100 - (67*v)/25000
        d = 49/20 - (27*v)/50000
        e = 729/50 - (2*v)/625
        f = 831/50 - (181*v)/50000
        g = 2111/100 - (231*v)/50000
        h = (103*v)/6250 - 204/5


 
        ansi_chain_hp_int_speed = [a, b, c, d, e, f, g, h]

        def selection(ansi_chain_hp_int_speed, hp_list):
            for hp in hp_list:  
                if hp < ansi_chain_hp_int_speed[0]:  
                    chain_answers.append(ansi_chain_number_int_speed[0])  
                    type_answers.append("B")

                elif hp > ansi_chain_hp_int_speed[-1]:
                    chain_answers.append("Not found")  
                    type_answers.append("ERROR")

                else:
                    for i, num in enumerate(ansi_chain_hp_int_speed):
                        if num > hp:
                            chain_answers.append(ansi_chain_number_int_speed[i])
                            break  
                    if i < 4:
                        type_answers.append("B")   
                    elif i == 4 or i == 5: 
                        type_answers.append("C")         
                    else:
                        type_answers.append("C'")
    

            return chain_answers,type_answers


        ansi_chain_hp_int_speed = [a, b, c, d, e, f, g, h,]
        ansi_chain_number_int_speed = [25, 35, 40, 41, 50, 60, 80, 100]

        chain_answers, type_answers = selection(ansi_chain_hp_int_speed, hps)
        return chain_answers, type_answers
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
    ans = []
    for this_d in d:
        this_ans = round(((ps*s*this_d*cap_d)/2), 3)
        ans.append(this_ans)
    return ans 


def f_b_wire_rope(er, dw, am, cap_d, d): 
    ans = []
    for this_d in d:
        this_ans = round((er*dw*this_d*am*this_d**2)/(cap_d), 3)
        ans.append(this_ans)
    return ans 



def nf_wire_rope(cap_w, w, l, a, ps, su,cap_d, d, er, dw, am):
    ans = []
    for this_d in d:
        d1_ans = []
        ff = (ps*su*this_d*cap_d)/2
        fb = (er*dw*this_d*am*this_d**2)/(cap_d)
        for this_m in range(1,11):
            ft = ((cap_w/this_m) +(w*l*this_d**2))*(1+(a/32.2))
            this_ans = round(((ff-fb)/ft), 3)
            d1_ans.append(this_ans)
        ans.append(d1_ans)
    return ans 

@error_handling_decorator
def center_distance_vbelt(lp, cd, d):
    a = lp-((math.pi/2) * (cd + d))
    b = a**2
    c = 2 * ((cd - d)**2)
    d = math.sqrt(b-c)
    ans = 0.25*(a+d)
    return ans


@error_handling_decorator
def lengh_pitch_vbelt(c, capd, d):
    ans = (2 * c) + (math.pi*(capd+d)/2) + (((capd-d)**2)/(4*c))
    return ans


@error_handling_decorator
def ha_vbelt(k1, k2, h_tab):
    ans =k1* k2 *h_tab
    return ans 

#lis_k1_vbelt:
lis_theta = [180, 174.3, 166.5, 162.7, 156.9, 151, 145.1, 139, 132.8, 126.5, 120, 113.3, 106.3, 98.9, 91.1, 82.8]
k1_vv = [1, .99, .97, .96, .94, .93, .91, .89, .87, .85, .82, .80, .77, .73, .70, .65]
k1_vflat = [.75, .76, .78, .79, .80, .81, .83, .84, .85, .85, .82, .80, .77, .73, .70, .65]

def k1_vbelt(theta,selected_type):
    if theta > 180 or theta < 82.2:
        return "Error: Range for θ is (82.2 < θ < 180) degree"
    else:
        if selected_type == "VV" :   
            for item in lis_theta:
                if item == theta:
                    index = lis_theta.index(item)
                    vv_belt = k1_vv[index] 
                    return vv_belt
            
                else:
                    for i in range(len(lis_theta) - 1):
                        if lis_theta[i] >= theta > lis_theta[i + 1]:
                            t1 = lis_theta[i]
                            t2 = lis_theta[i + 1]
                            k1= k1_vv[i] 
                            k2 = k1_vv[i + 1]
                            vv_belt = (k1 + (k2 - k1)) * ((theta - t1) / (t2 - t1))
                            return vv_belt
                    return k1_vv[-1]
            
        else:
            for item in lis_theta:
                if item == theta:
                    index = lis_theta.index(item)
                    vflat_belt = k1_vflat[index] 
                    return vflat_belt
            
            else:
                for i in range(len(lis_theta) - 1):
                    if lis_theta[i] >= theta > lis_theta[i + 1]:
                        t1 = lis_theta[i]
                        t2 = lis_theta[i + 1]
                        k1= k1_vflat[i] 
                        k2 = k1_vflat[i + 1]
                        vflat_belt = k1 + (k2 - k1) * (theta - t1) / (t2 - t1)
                        return vflat_belt
                return k1_vv[-1]      
                
print(k1_vbelt(121,"vv"))

standard_speed_vbelt = [1000,2000,3000,4000,5000]

standard_sheave_d_vbelt_A = [2.6, 3, 3.4, 3.8, 4.2, 4.6, 5]
standard_sheave_d_vbelt_B = [4.2, 4.6, 5, 5.4, 5.8, 6.2, 6.6, 7]
standard_sheave_d_vbelt_C = [6, 7, 8, 9, 10, 11, 12]
standard_sheave_d_vbelt_D = [10, 11, 12, 13, 14, 15, 16, 17]
standard_sheave_d_vbelt_E = [16, 18 ,20, 22, 24, 26, 28]

table_vbelt_standard_hp_type_A = [
    [0.47, 0.62, 0.53, 0.15, 0.10],
    [0.66, 1.01, 1.12, 0.93, 0.38],
    [0.81, 1.31, 1.57, 1.53, 1.12],
    [0.93, 1.55, 1.92, 2.00, 1.71],
    [1.03, 1.74, 2.20, 2.38, 2.19],
    [1.11, 1.89, 2.44, 2.69, 2.58],
    [1.17, 2.03, 2.64, 2.96, 2.89],]

table_vbelt_standard_hp_type_B = [
    [1.07, 1.58, 1.68, 1.26, 0.22],
    [1.27, 1.99, 2.29, 2.08, 1.24],
    [1.44, 2.33, 2.80, 2.76, 2.10],
    [1.59, 2.62, 3.24, 3.34, 2.82],
    [1.72, 2.87, 3.61, 3.85, 3.45],
    [1.82, 3.09, 3.94, 4.28, 4.00],
    [1.92, 3.29, 4.23, 4.67, 4.48],
    [2.01, 3.46, 4.49, 5.01, 4.90]]

table_vbelt_standard_hp_type_C = [
    [1.84, 2.66, 2.72, 1.87, 1.81],
    [2.48, 3.94, 4.64, 4.44, 3.12],
    [2.96, 4.90, 6.09, 6.36, 5.52],
    [3.34, 5.65, 7.21, 7.86, 7.39],
    [3.64, 6.25, 8.11, 9.06, 8.89],
    [3.88, 6.74, 8.84, 10.0, 10.1],
    [4.09, 7.15, 9.46, 10.9, 11.1]]

table_vbelt_standard_hp_type_D = [
    [4.14, 6.13, 6.55, 5.09, 1.35],
    [5.00, 7.83, 9.11, 8.50, 5.62],
    [5.71, 9.26, 11.2, 11.4, 9.18],
    [6.31, 10.5, 13.0, 13.8, 12.2],
    [6.82, 11.5, 14.6, 15.8, 14.8],
    [7.27, 12.4, 15.9, 17.6, 17.0],
    [7.66, 13.2, 17.1, 19.2, 19.0],
    [8.01, 13.9, 18.1, 20.6, 20.7]]

table_vbelt_standard_hp_type_E = [
    [8.68, 14.0, 17.5, 18.1, 15.3],
    [9.92, 16.7, 21.2, 23.0, 21.5],
    [10.9, 18.7, 24.2, 26.9, 26.4],
    [11.7, 20.3, 26.6, 30.2, 30.5],
    [12.4, 21.6, 28.6, 32.9, 33.8],
    [13.0, 22.8, 30.3, 35.1, 36.7],
    [13.4, 23.7, 31.8, 37.1, 39.1]]

def h_table_vbelt(v,sheave_d,selected_type):
    v = int(v)
    sheave_d = float(sheave_d)
    # TODO NOT found handle error
    vind = (v//1000)-1
    if selected_type == "A" :
        if sheave_d >= 5:
            hp = table_vbelt_standard_hp_type_A[-1][vind]
            return hp

        elif sheave_d in standard_sheave_d_vbelt_A:
            row = standard_sheave_d_vbelt_A.index(sheave_d)
            hp = table_vbelt_standard_hp_type_A[row][vind]
            return hp

    elif selected_type == "B" :
        if sheave_d >= 7:
            hp = table_vbelt_standard_hp_type_B[-1][vind]
            return hp
        elif sheave_d in standard_sheave_d_vbelt_B:
            row = standard_sheave_d_vbelt_B.index(sheave_d)
            hp = table_vbelt_standard_hp_type_B[row][(v//1000)-1]
            return hp

    elif selected_type == "C" :
        if sheave_d >= 12:
            hp = table_vbelt_standard_hp_type_C[-1][vind]
            return hp
        elif sheave_d in standard_sheave_d_vbelt_C:
            row = standard_sheave_d_vbelt_C.index(sheave_d)
            hp = table_vbelt_standard_hp_type_C[row][(v//1000)-1]
            return hp

    elif selected_type == "D" :
        if sheave_d >= 17:
            hp = table_vbelt_standard_hp_type_D[-1][vind]
            return hp
        if sheave_d in standard_sheave_d_vbelt_D:
            row = standard_sheave_d_vbelt_D.index(sheave_d)
            hp = table_vbelt_standard_hp_type_D[row][(v//1000)-1]
            return hp

    elif selected_type == "E" :
        if sheave_d >= 28:
            hp = table_vbelt_standard_hp_type_E[-1][vind]
            return hp
        if sheave_d in standard_sheave_d_vbelt_E:
            row = standard_sheave_d_vbelt_E.index(sheave_d)
            hp = table_vbelt_standard_hp_type_E[row][(v//1000)-1]
            return hp


def linear_int_speed(speed1, speed2, v, hp1, hp2):
    ans = ((hp2-hp1)*((v-speed1)/(speed2-speed1)))+hp1
    return ans

def h_table_vbelt_int_speed(v, sheave_d, selected_type):
    v = float(v)
    sheave_d = float(sheave_d)
    if v > 5000 or v < 1000:
        return "Error: speed range should be between 1000 and 5000."
    if selected_type == "A":
        row = standard_sheave_d_vbelt_A.index(sheave_d)
        for i in range(len(standard_speed_vbelt)):
            if v < standard_speed_vbelt[i]:
                speed2 = standard_speed_vbelt[i]
                speed1 = standard_speed_vbelt[i-1]
                print(speed1, speed2)
                row = standard_sheave_d_vbelt_A.index(sheave_d)
                hp2 = table_vbelt_standard_hp_type_A[row][i]
                hp1 = table_vbelt_standard_hp_type_A[row][i-1]
                print(hp2, hp1)

                return linear_int_speed(speed1, speed2, v, hp1, hp2)
        
    if selected_type == "B":
        row = standard_sheave_d_vbelt_A.index(sheave_d)
        for i in range(len(standard_speed_vbelt)):
            if v < standard_speed_vbelt[i]:
                speed2 = standard_speed_vbelt[i]
                speed1 = standard_speed_vbelt[i-1]
                print(speed1, speed2)
                row = standard_sheave_d_vbelt_B.index(sheave_d)
                hp2 = table_vbelt_standard_hp_type_B[row][i]
                hp1 = table_vbelt_standard_hp_type_B[row][i-1]
                print(hp2, hp1)

                return linear_int_speed(speed1, speed2, v, hp1, hp2)
            
    if selected_type == "C":
        row = standard_sheave_d_vbelt_C.index(sheave_d)
        for i in range(len(standard_speed_vbelt)):
            if v < standard_speed_vbelt[i]:
                speed2 = standard_speed_vbelt[i]
                speed1 = standard_speed_vbelt[i-1]
                print(speed1, speed2)
                row = standard_sheave_d_vbelt_C.index(sheave_d)
                hp2 = table_vbelt_standard_hp_type_C[row][i]
                hp1 = table_vbelt_standard_hp_type_C[row][i-1]
                print(hp2, hp1)

                return linear_int_speed(speed1, speed2, v, hp1, hp2)

    if selected_type == "D":
        row = standard_sheave_d_vbelt_D.index(sheave_d)
        for i in range(len(standard_speed_vbelt)):
            if v < standard_speed_vbelt[i]:
                speed2 = standard_speed_vbelt[i]
                speed1 = standard_speed_vbelt[i-1]
                print(speed1, speed2)
                row = standard_sheave_d_vbelt_D.index(sheave_d)
                hp2 = table_vbelt_standard_hp_type_D[row][i]
                hp1 = table_vbelt_standard_hp_type_D[row][i-1]
                print(hp2, hp1)

                return linear_int_speed(speed1, speed2, v, hp1, hp2)

    if selected_type == "E":
        row = standard_sheave_d_vbelt_E.index(sheave_d)
        for i in range(len(standard_speed_vbelt)):
            if v < standard_speed_vbelt[i]:
                speed2 = standard_speed_vbelt[i]
                speed1 = standard_speed_vbelt[i-1]
                print(speed1, speed2)
                row = standard_sheave_d_vbelt_E.index(sheave_d)
                hp2 = table_vbelt_standard_hp_type_E[row][i]
                hp1 = table_vbelt_standard_hp_type_E[row][i-1]
                print(hp2, hp1)

                return linear_int_speed(speed1, speed2, v, hp1, hp2)                                    
#print(h_table_vbelt_int_speed(300, 2.6, "A"))

def linear_int_pulley(pulley1, pulley2, input_pulley, hp1, hp2):
    ans = (input_pulley-pulley1)/(pulley2-pulley1)*(hp2-hp1)+hp1
    return ans

def h_table_vbelt_int_pulley(v, sheave_d, selected_type):
    v = int(v)
    sheave_d = float(sheave_d)
    #TODO: out of the range not found!
    vind = (v//1000)-1
    if selected_type == "A":
        if sheave_d < 2.6:
            # TODO: Edit message error d>5
            return "Error: selected Sheave Pitch Diameter is not allowable; in 'A' Belt Section "
        if sheave_d > 5:
            return "Error:For Sheave Pitch Diameters larger than (5 in) in 'A' Belt Section;" \
            "Use Standard (5 in) Sheave Pitch Diameter or use another belt section."
        index_pulley = 0
        for i in range(len(standard_sheave_d_vbelt_A)):
            if sheave_d > standard_sheave_d_vbelt_A[i]:
                index_pulley = i
        pulley1 = (standard_sheave_d_vbelt_A[index_pulley])
        pulley2 = (standard_sheave_d_vbelt_A[index_pulley+1])

        hp1= table_vbelt_standard_hp_type_A[index_pulley][vind]
        hp2 = table_vbelt_standard_hp_type_A[index_pulley+1][vind]

        return linear_int_pulley(pulley1, pulley2, sheave_d, hp1, hp2)

    if selected_type == "B":
        if sheave_d < 4.2 :
            return "Error: selected Sheave Pitch Diameter is not allowable; Select another Belt Section."
        if sheave_d > 7:
            return "Error:For Sheave Pitch Diameters larger than (7 in) in 'B' Belt Section;" \
            "Use Standard (7 in) Sheave Pitch Diameter or use another belt section."
        index_pulley = 0
        for i in range(len(standard_sheave_d_vbelt_B)):
            if sheave_d > standard_sheave_d_vbelt_B[i]:
                index_pulley = i
        pulley1 = (standard_sheave_d_vbelt_B[index_pulley])
        pulley2 = (standard_sheave_d_vbelt_B[index_pulley+1])

        hp1= table_vbelt_standard_hp_type_B[index_pulley][vind]
        hp2 = table_vbelt_standard_hp_type_B[index_pulley+1][vind]

        return linear_int_pulley(pulley1, pulley2, sheave_d, hp1, hp2)                

    if selected_type == "C":
        if sheave_d < 6 :
            return "Error: selected Sheave Pitch Diameter is not allowable; Select another Belt Section."
        if sheave_d > 12 :
            return "Error:For Sheave Pitch Diameters larger than (12 in) in 'C' Belt Section;" \
            "Use Standard (12 in) Sheave Pitch Diameter or use another belt section."
        index_pulley = 0
        for i in range(len(standard_sheave_d_vbelt_C)):
            if sheave_d > standard_sheave_d_vbelt_C[i]:
                index_pulley = i
        pulley1 = (standard_sheave_d_vbelt_C[index_pulley])
        pulley2 = (standard_sheave_d_vbelt_C[index_pulley+1])

        hp1= table_vbelt_standard_hp_type_C[index_pulley][vind]
        hp2 = table_vbelt_standard_hp_type_C[index_pulley+1][vind]

        return linear_int_pulley(pulley1, pulley2, sheave_d, hp1, hp2)


    if selected_type == "D":
        if sheave_d < 10 :
            return "Error: selected Sheave Pitch Diameter is not allowable; Select another Belt Section."
        if sheave_d > 17:
            return "Error:For Sheave Pitch Diameters larger than (17 in) in 'D' Belt Section;" \
            "Use Standard (17 in) Sheave Pitch Diameter or use another belt section."
        index_pulley = 0
        for i in range(len(standard_sheave_d_vbelt_D)):
            if sheave_d > standard_sheave_d_vbelt_D[i]:
                index_pulley = i
        pulley1 = (standard_sheave_d_vbelt_D[index_pulley])
        pulley2 = (standard_sheave_d_vbelt_D[index_pulley+1])

        hp1= table_vbelt_standard_hp_type_D[index_pulley][vind]
        hp2 = table_vbelt_standard_hp_type_D[index_pulley+1][vind]

        return linear_int_pulley(pulley1, pulley2, sheave_d, hp1, hp2)

    if selected_type == "E":
        if sheave_d < 16 :
            return "Error: selected Sheave Pitch Diameter is not allowable; Select another Belt Section."
        if sheave_d > 28 :
            return "Error:For Sheave Pitch Diameters larger than (28 in) in 'E' Belt Section;" \
            "Use Standard (28 in) Sheave Pitch Diameter or use another belt section."
        index_pulley = 0
        for i in range(len(standard_sheave_d_vbelt_E)):
            if sheave_d > standard_sheave_d_vbelt_E[i]:
                index_pulley = i
        pulley1 = (standard_sheave_d_vbelt_E[index_pulley])
        pulley2 = (standard_sheave_d_vbelt_E[index_pulley+1])

        hp1= table_vbelt_standard_hp_type_E[index_pulley][vind]
        hp2 = table_vbelt_standard_hp_type_E[index_pulley+1][vind]

        return linear_int_pulley(pulley1, pulley2, sheave_d, hp1, hp2)
    
#print(h_table_vbelt_int_pulley(2000, 16.4, "E"))

def h_table_vbelt_int_pulley_and_speed(v, sheave_d, selected_type):
    v = float(v)
    print("im in correct funcs")
    sheave_d = float(sheave_d)
    

    if selected_type == "A":
        if v > 5000 or v < 1000 and sheave_d<2.6:
            return "Error : goh v sheave_d < 2.6"
        
        elif v > 5000 or v < 1000 and sheave_d>5:
            return "Error goh v sheave_d > 5"

        elif v > 5000 or v < 1000 :
            return "Error:Speed is out of the range; Speed Range (1000 < V < 5000) ft/min"
        elif sheave_d < 2.6 :
            return "Error:Sheave Pitch Diameter should be larger than '2.6'(in); in 'A' Belt Section"
        elif sheave_d > 5 :
            return "Error:For Sheave Pitch Diameter larger than '5'(in); Use Standard '5'(in) in 'A' Belt Section"


        pulley_index = 0
        for ind in range(len(standard_sheave_d_vbelt_A)):
            if sheave_d > standard_sheave_d_vbelt_A[ind]:
                pulley_index = ind
        
        pulley1_index=pulley_index # row ind
        pulley3_index=pulley_index+1

        pulley1 = standard_sheave_d_vbelt_A[pulley1_index]
        pulley3 = standard_sheave_d_vbelt_A[pulley3_index]
        speed_index = 0
        for ind in range(len(standard_speed_vbelt)):
            if v > standard_speed_vbelt[ind]:
                speed_index = ind
        speed1_index = speed_index # col ind
        speed3_index = speed_index+1

        speed1 = standard_speed_vbelt[speed1_index]
        speed3 = standard_speed_vbelt[speed3_index] # second speed! not third one!

        hp1 = table_vbelt_standard_hp_type_A[pulley1_index][speed1_index]
        hp2 = table_vbelt_standard_hp_type_A[pulley1_index][speed3_index]
        hp3 = table_vbelt_standard_hp_type_A[pulley3_index][speed1_index]
        hp4 = table_vbelt_standard_hp_type_A[pulley3_index][speed3_index]


        hp12 = linear_int_speed(speed1, speed3, v, hp1, hp2)
        hp34 = linear_int_speed(speed1, speed3, v, hp3, hp4)
        
        final_answer = linear_int_pulley(pulley1, pulley3, sheave_d, hp12, hp34)
        return final_answer

    elif selected_type == "B":
        if v > 5000 or v < 1000 and sheave_d<4.2:
            return "Error : goh v sheave_d < 4.2"
        
        elif v > 5000 or v < 1000 and sheave_d>7:
            return "Error goh v sheave_d > 7"

        elif v > 5000 or v < 1000 :
            return "Error:Speed is out of the range; Speed Range (1000 < V < 5000) ft/min"
        elif sheave_d < 4.2 :
            return "Error:Sheave Pitch Diameter should be larger than '4.2'(in); in 'B' Belt Section"
        elif sheave_d > 7 :
            return "Error:For Sheave Pitch Diameter larger than '7'(in); Use Standard '7'(in) in 'B' Belt Section"
        
        pulley_index = 0
        for ind in range(len(standard_sheave_d_vbelt_B)):
            if sheave_d > standard_sheave_d_vbelt_B[ind]:
                pulley_index = ind
        
        pulley1_index=pulley_index # row ind
        pulley3_index=pulley_index+1

        pulley1 = standard_sheave_d_vbelt_B[pulley1_index]
        pulley3 = standard_sheave_d_vbelt_B[pulley3_index]
        speed_index = 0
        for ind in range(len(standard_speed_vbelt)):
            if v > standard_speed_vbelt[ind]:
                speed_index = ind
        speed1_index = speed_index # col ind
        speed3_index = speed_index+1

        speed1 = standard_speed_vbelt[speed1_index]
        speed3 = standard_speed_vbelt[speed3_index] # second speed! not third one!

        hp1 = table_vbelt_standard_hp_type_B[pulley1_index][speed1_index]
        hp2 = table_vbelt_standard_hp_type_B[pulley1_index][speed3_index]
        hp3 = table_vbelt_standard_hp_type_B[pulley3_index][speed1_index]
        hp4 = table_vbelt_standard_hp_type_B[pulley3_index][speed3_index]


        hp12 = linear_int_speed(speed1, speed3, v, hp1, hp2)
        hp34 = linear_int_speed(speed1, speed3, v, hp3, hp4)
        
        final_answer = linear_int_pulley(pulley1, pulley3, sheave_d, hp12, hp34)
        return final_answer

    elif selected_type == "C":
        if v > 5000 or v < 1000 and sheave_d<6:
            return "Error : goh v sheave_d < 6"
        
        elif v > 5000 or v < 1000 and sheave_d>12:
            return "Error goh v sheave_d > 12"

        elif v > 5000 or v < 1000 :
            return "Error:Speed is out of the range; Speed Range (1000 < V < 5000) ft/min"
        elif sheave_d < 6 :
            return "Error:Sheave Pitch Diameter should be larger than '6'(in); in 'C' Belt Section"
        elif sheave_d > 12 :
            return "Error:For Sheave Pitch Diameter larger than '12'(in); Use Standard '12'(in) in 'C' Belt Section"       

        pulley_index = 0
        for ind in range(len(standard_sheave_d_vbelt_C)):
            if sheave_d > standard_sheave_d_vbelt_C[ind]:
                pulley_index = ind
        
        pulley1_index=pulley_index # row ind
        pulley3_index=pulley_index+1

        pulley1 = standard_sheave_d_vbelt_C[pulley1_index]
        pulley3 = standard_sheave_d_vbelt_C[pulley3_index]
        speed_index = 0
        for ind in range(len(standard_speed_vbelt)):
            if v > standard_speed_vbelt[ind]:
                speed_index = ind
        speed1_index = speed_index # col ind
        speed3_index = speed_index+1

        speed1 = standard_speed_vbelt[speed1_index]
        speed3 = standard_speed_vbelt[speed3_index] # second speed! not third one!

        hp1 = table_vbelt_standard_hp_type_C[pulley1_index][speed1_index]
        hp2 = table_vbelt_standard_hp_type_C[pulley1_index][speed3_index]
        hp3 = table_vbelt_standard_hp_type_C[pulley3_index][speed1_index]
        hp4 = table_vbelt_standard_hp_type_C[pulley3_index][speed3_index]


        hp12 = linear_int_speed(speed1, speed3, v, hp1, hp2)
        hp34 = linear_int_speed(speed1, speed3, v, hp3, hp4)
        
        final_answer = linear_int_pulley(pulley1, pulley3, sheave_d, hp12, hp34)
        return final_answer

    elif selected_type == "D":
        if v > 5000 or v < 1000 and sheave_d<10:
            return "Error : goh v sheave_d < 10"
        
        elif v > 5000 or v < 1000 and sheave_d>17:
            return "Error goh v sheave_d > 17"
        elif v > 5000 or v < 1000 :
            return "Error:Speed is out of the range; Speed Range (1000 < V < 5000) ft/min"
        elif sheave_d < 10 :
            return "Error:Sheave Pitch Diameter should be larger than '10'(in); in 'D' Belt Section"
        elif sheave_d > 17 :
            return "Error:For Sheave Pitch Diameter larger than '17'(in); Use Standard '17'(in) in 'D' Belt Section"
        
        
        pulley_index = 0
        for ind in range(len(standard_sheave_d_vbelt_D)):
            if sheave_d > standard_sheave_d_vbelt_D[ind]:
                pulley_index = ind
        
        pulley1_index=pulley_index # row ind
        pulley3_index=pulley_index+1

        pulley1 = standard_sheave_d_vbelt_D[pulley1_index]
        pulley3 = standard_sheave_d_vbelt_D[pulley3_index]
        speed_index = 0
        for ind in range(len(standard_speed_vbelt)):
            if v > standard_speed_vbelt[ind]:
                speed_index = ind
        speed1_index = speed_index # col ind
        speed3_index = speed_index+1

        speed1 = standard_speed_vbelt[speed1_index]
        speed3 = standard_speed_vbelt[speed3_index] # second speed! not third one!

        hp1 = table_vbelt_standard_hp_type_D[pulley1_index][speed1_index]
        hp2 = table_vbelt_standard_hp_type_D[pulley1_index][speed3_index]
        hp3 = table_vbelt_standard_hp_type_D[pulley3_index][speed1_index]
        hp4 = table_vbelt_standard_hp_type_D[pulley3_index][speed3_index]


        hp12 = linear_int_speed(speed1, speed3, v, hp1, hp2)
        hp34 = linear_int_speed(speed1, speed3, v, hp3, hp4)
        
        final_answer = linear_int_pulley(pulley1, pulley3, sheave_d, hp12, hp34)
        return final_answer

    elif selected_type == "E":
        if v > 5000 or v < 1000 and sheave_d<16:
            return "Error : goh v sheave_d < 16"
        
        elif v > 5000 or v < 1000 and sheave_d>28:
            return "Error goh v sheave_d > 28"

        elif v > 5000 or v < 1000 :
            return "Error:Speed is out of the range; Speed Range (1000 < V < 5000) ft/min"
        elif sheave_d < 16 :
            return "Error:Sheave Pitch Diameter should be larger than '16'(in); in 'E' Belt Section"
        elif sheave_d > 28 :
            return "Error:For Sheave Pitch Diameter larger than '28'(in) Use Standard '28'(in); in 'E' Belt Section"
        
        pulley_index = 0
        for ind in range(len(standard_sheave_d_vbelt_E)):
            if sheave_d > standard_sheave_d_vbelt_C[ind]:
                pulley_index = ind
        
        pulley1_index=pulley_index # row ind
        pulley3_index=pulley_index+1

        pulley1 = standard_sheave_d_vbelt_E[pulley1_index]
        pulley3 = standard_sheave_d_vbelt_E[pulley3_index]
        speed_index = 0
        for ind in range(len(standard_speed_vbelt)):
            if v > standard_speed_vbelt[ind]:
                speed_index = ind
        speed1_index = speed_index # col ind
        speed3_index = speed_index+1

        speed1 = standard_speed_vbelt[speed1_index]
        speed3 = standard_speed_vbelt[speed3_index] # second speed! not third one!

        hp1 = table_vbelt_standard_hp_type_E[pulley1_index][speed1_index]
        hp2 = table_vbelt_standard_hp_type_E[pulley1_index][speed3_index]
        hp3 = table_vbelt_standard_hp_type_E[pulley3_index][speed1_index]
        hp4 = table_vbelt_standard_hp_type_E[pulley3_index][speed3_index]


        hp12 = linear_int_speed(speed1, speed3, v, hp1, hp2)
        hp34 = linear_int_speed(speed1, speed3, v, hp3, hp4)
        
        final_answer = linear_int_pulley(pulley1, pulley3, sheave_d, hp12, hp34)
        return final_answer

@error_handling_decorator
def hd_vbelt(h_nom, ks, nd):
    ans = h_nom*ks*nd
    return ans

@error_handling_decorator
def nb_vbelt(ha, hd):
    nb = hd/ha
    ans = math.ceil(nb)
    return ans

@error_handling_decorator
def fc_vbelt(kc, v):
    ans = kc * ((v/1000)**2)
    return ans

@error_handling_decorator
def delta_f_vbelt(hd, nb, n , d):
    ans = (63025*hd/nb)/(n*(d/2))
    return ans

@error_handling_decorator
def f1_vbelt(fc, detaf, exp):
    ans = fc + ((detaf*exp)/(exp-1))
    return ans

@error_handling_decorator
def f2_vbelt(f1, deltaf):
    ans = f1 - deltaf
    return ans 

@error_handling_decorator
def fi_vbelt(f1, f2, fc):
    ans = ((f1+f2)/2)-fc
    return ans

@error_handling_decorator
def nfs_vbelt(ha, nb, hnom, ks):
    ans = (ha*nb)/(hnom*ks)
    return ans

@error_handling_decorator
def fb1_vbelt(kb, d):
    ans = kb/d
    return ans

@error_handling_decorator
def fb2_vbelt(kb, cd):
    ans = kb/cd
    return ans

@error_handling_decorator
def t1_vbelt(f1,fb1):
    ans = f1+fb1
    return ans

@error_handling_decorator
def t2_vbelt(f1,fb2):
    ans = f1 + fb2
    return ans

@error_handling_decorator
def np_vbelt(k, b, t1, t2):
    a = (k/t1)**(-b)
    b = (k/t2)**(-b)
    ans = ((a+b)**-1)
    fans = "{:.3e}".format(ans)
    return fans

@error_handling_decorator
def t_vbelt(np, lp, v):
    if np > 10e9:
        ans = ((10e9)*lp)/(720*v)
    else:
        ans = (np*lp)/(720*v)
    return ans            

