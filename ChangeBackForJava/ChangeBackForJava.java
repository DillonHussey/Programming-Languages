package ChangeBackForJava;
import java.util.*;

public class ChangeBackForJava {
    
    public static void main(String [] arg){
        Scanner reader = new Scanner(System.in);
        Boolean flag = true;
        double total;
        while(flag){
            System.out.println("Enter a double to be evaluated for all \ncombinations of Quarters, Dimes, and Nickels.");
            total = reader.nextDouble();
            if(total%.05 != 0){
                flag=false;
            }
            else{
                System.out.println("Please enter a total (must not require pennies)");
            }

            System.out.println(change("Q\tD\tN\n", (int)(100*total)));

            reader.close();
        }
    }

    public static String change(String str, int t){
        int[] bases = {25, 10, 5};
        //for loop that runs through every testable number of quarters, dimes and nickels
        // temporary variable is used to represent the running total which is what remains from the total after accounting for higher bases
        //for loop then runs through new running total with new temporary total and smaller base
        //in innermost nested for loop, the total is tested for each of the smallest base combination and if the total would be zero, meaning the coins divide the total evenly then the number of coins is printed
        for(int x=0; x<=t/bases[0]; x++){
            int temp = t-x*bases[0];
            for(int y=0; y<=temp/bases[1];y++) {
                int temp1 = temp-y*bases[1];
                for(int z=0; z<=temp1/bases[2]; z++){
                    if(temp1-z*bases[2]==0){
                        str= str +(x+"\t"+y+"\t"+z)+"\n";
                    }
                }
            }
        }
        
        return str;
    }
}
