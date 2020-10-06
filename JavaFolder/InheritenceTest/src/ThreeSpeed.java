class ThreeSpeed extends Bicycle{

    private boolean hasBasket;

    public ThreeSpeed(int g, int sp, boolean basket){
        super(g, sp);
        hasBasket = basket;
    }


    @Override
    public String toString(){
        return (super.toString() + "\nHasBasket: " + this.hasBasket);
    }
}