package Duck;

public class DuckAdaptor implements Turkeylike {
    public Duck duck;
    @Override
    public void gobble(){

    }
    public void DuckAdaptor(Duck Ducklike){
        this.duck = ducklike;
    }    
     
    @Override
    public void fly() {
        for (int i= 0; i<5;i++){
            duck.fly();
        }
    }
}            