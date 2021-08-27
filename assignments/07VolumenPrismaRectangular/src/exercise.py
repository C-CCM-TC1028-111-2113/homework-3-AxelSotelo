def area(b, d):
        area=b*d
        return area

def volumen(a, h):
        v=a*h
        print("El volumen del prisma es: ", v)
        
def main():
  #escribe tu código abajo de esta línea

    b=float(input("Dame la base: "))
    h=float(input("Dame la altura: "))
    d=float(input("Dame la profundidad: "))
    
    a=area(b, d)
    volumen(a, h)
                       

if __name__=='__main__':
    main()
