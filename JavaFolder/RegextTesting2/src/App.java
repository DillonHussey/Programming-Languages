import java.util.regex.Pattern;
import java.util.regex.Matcher;
public class App {
    public static void main(String[] args) throws Exception {
        //System.out.println(isTrueOrYes("yes"));

        String exampleText = "We are in this together, I got your back";
        Pattern pattern = Pattern.compile("\\w+");
        Matcher m = pattern.matcher(exampleText);
        while(m.find()){
            System.out.print("Start: " + m.start());
            System.out.print(" End: " + m.end()+ " ");
            System.out.println(m.group());
            
        }
    }

    static boolean isTrue(String s){
        return s.matches("[Tt]rue");
    }

    static boolean isTrueOrYes(String s) {
        return s.matches("[tT]rue|[yY]es");
    }
    
    static boolean isThreeLetters(String s){
        return s.matches("[a-zA-Z](3)");
    }

    static boolean isNoNumberAtBeginning(String s) {
        return s.matches("^[^\\d].*");

    }
}
