import math


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
            error = f"An error occurred: {e}"
            return error  # or handle other exceptions as needed
    return wrapper


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

@error_handling_decorator
def expphi(phi, f):
    ans = math.exp(phi*f)
    return ans

def TorqueBelt(H_nom,K_s,n_d,n):
    ans = ((63025*H_nom*K_s*n_d))/n
    return ans


@error_handling_decorator
#TODO: check if it wasn't error
def f1a_f2(T,d):
    ans = (2*T)/d
    ans =f"{ans} N" 
    
    return ans



@error_handling_decorator
def fi(t,d,f,phi,):
    ans = (t/d*(((math.exp(f*phi)+1)/((math.exp(f*phi)-1)))))
    ans =f"{ans} N" 
    return ans


@error_handling_decorator
def fi2(fc,f2_p,f1a_p):
    ans = (((f2_p+f1a_p)/2)-fc)
    ans =f"{ans} N" 
    return ans

@error_handling_decorator
def f2(f1a_p,f1ap_f2):
    ans = ((f1a_p)-(f1ap_f2))
    ans =f"{ans} N" 
    return ans

@error_handling_decorator
def f1a(b,fa,cv,cp):
    ans = (b*fa*cv*cp)
    ans =f"{ans} N" 
    return ans

@error_handling_decorator
def f_prime(phi,f1a_p,fc,f2):
    ans =((1/phi)*(math.log((f1a_p-fc)/(f2-fc))))    
    return ans


@error_handling_decorator
def dip(c,w,fi_p,):
    ans =(((c**2)*w)/(96*fi_p))   
    ans =f"{ans} in" 
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
    ans =f"{ans} N" 
    return ans 

@error_handling_decorator
def f2metalbelt(sf,et,nu,dcap,tcap,t,b):
    x = et/((1-nu**2)*dcap)
    ab = (sf - x)*t*b
    delf = 2*tcap/dcap
    ans = ab - delf
    ans =f"{ans} N" 
    return ans

@error_handling_decorator
def fi_2(sf,et,nu,dcap,tcap,t,b):
    x = et/((1-nu**2)*dcap)
    ab = (sf - x)*t*b
    delf = 2*tcap/dcap
    ans = ab - (delf/2)
    ans =f"{ans} N" 
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


# TODO: edit lable, dynamic m 
def f_f_wire_rope(ps, s, cap_d, d): 
    # TODO: WRITE IN TABLE
    ans = []
    for this_d in d:
        ans.append((ps*s*this_d*cap_d)/2)
    return ans 


def f_b_wire_rope(er, dw, am, cap_d, d): 
    # TODO: WRITE IN TABLE
    ans = []
    for this_d in d:
        ans.append((er*dw*this_d*am*this_d**2)/(cap_d))
    return ans 

print(f_b_wire_rope(12000000, 0.067, 0.4, 72, [0.25]))


def nf_wire_rope(cap_w, w, l, a, ps, su,cap_d, d, er, dw, am):
    ans = []
    for this_d in d:
        d1_ans = []
        ff = (ps*su*this_d*cap_d)/2
        fb = (er*dw*this_d*am*this_d**2)/(cap_d)
        for this_m in range(1,11):
            ft = ((cap_w/this_m) +(w*l*this_d**2))*(1+(a/32.2))
            d1_ans.append((ff-fb)/ft)
        ans.append(d1_ans)
    return ans 