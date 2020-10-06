//import jdk.internal.jshell.tool.resources.l10n;
package CircleCompare;

public class App {
    
    
    private int count = 0;

    public void increment() {
        count++;
    }

    public int getCount(){
        return count;
    }

    public static void main(String[] args) throws Exception {
        
        App obj1 = new App();
        App obj2 = new App();

        obj1.increment();
        obj2.increment();
        
        System.out.println("Obj1 count: " + obj1.getCount());
        System.out.println("Obj2 count: " + obj2.getCount());
        
        
    
    }
}
