import java.util.Arrays;
import java.util.Collection;
import java.util.Collections;
import java.util.HashSet;
import java.util.ArrayList;
import java.util.HashMap;
public class App {
    public static void main(String[] args) {
        HashMap<String, Integer> map = new HashMap<>();
//\/\/(.*\.?)
        map.put("Hello", 10);
        map.put("Dorris", 20);
        map.put("Fofo", 30);

        System.out.println("Size is: " + map.size());
        System.out.println(map);
        if(map.containsKey("Dorris")){
            System.out.println("Yes");
        }
        Integer a = map.get("Fofo");
        System.out.println(a);
        Integer b = map.get("Yoyo");
        System.out.println(b);

        /*
        Collection<String> c = new HashSet<>();

        Collection<String> d = Arrays.asList("one", "two");
        Collection<String> e = Collections.singleton("three");

        c.add("zero");
        c.addAll(d);

        Collection<String> copy = new ArrayList<String>(c);

        c.remove("zero");  //return true
        c.remove("yo");     //return false
        
        c.removeAll(e);
        c.retainAll(d);
        c.clear();

        boolean b = c.isEmpty();
        int s = c.size();
        
        c.addAll(copy);

        b = c.contains("zero");
        b = c.containsAll(d);

        System.out.println(c);

        Object[] elements = c.toArray();

        String[] strings = c.toArray(new String[c.size()]);

        strings = c.toArray(new String[0]);
        */
        
    }
}
