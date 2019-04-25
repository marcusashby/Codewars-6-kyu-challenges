def create_phone_number(n):
    s=""
    for i in n:
        s=s+str(i)
    return "("+s[0:3]+") "+s[3:6]+"-"+s[6:]