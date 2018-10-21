#Receives Ip as string x.y.z.w then prints it's class and mask in decimal and binary 
def number2bin(num):
    m=0x01
    b=[]
    for i in range(8):
        if (num&m) == m:
            b.append('1')
        else:
            b.append('0')
        m=m*2
    b.reverse()    
    return ''.join(b)

def parser_ip(ip_string):
    a,b,c,d = ip_string.split('.')
    a=int(a)
    m2=0
    m3=0
    if (a&0x80) == 0x00:
        print('class A')
    elif (a&0xC0) == 0x80:
        print('class B')
        m2=255
    elif (a&0xE0) == 0xC0:
        print('class C')
        m2=255
        m3=255
    else:
        print('class D or E')
    print('IP : %s.%s.%s.%s'%(a,b,c,d) )
    print('MSK: %s.%s.%s.%s'%(255,m2,m3,0))
    print('IP Binary : %s.%s.%s.%s'%(number2bin(a),number2bin(int(b)),number2bin(int(c)),number2bin(int(d))))
    print('MSK Binary: %s.%s.%s.%s'%(number2bin(255),number2bin(int(m2)),number2bin(int(m3)),number2bin(int(0))))
        
parser_ip("173.23.2.58")
