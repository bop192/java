package fraction;

public class Fraction {
    private int numerator, denomirator;

    public Fraction(int n, int d)throws ArithmeticException {
        if(d==0){
            throw new ArithmeticException();}
            numerator = n;
            denomirator=d;
        }
       }              
