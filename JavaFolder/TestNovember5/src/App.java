/*
Dillon Hussey
Java Test
    Uses concurrency and Singleton Collection to loop for loop and assign Random sleep periods to Threads
November 5 2020
For Programming Languages with Brett Huffman
*/



import java.util.Random;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class App {

    //create random "generator"
    static Random randy = new Random();

    //initialize random sleep number
    static int randomSleep;
    public static void main(String[] args) {
        
        //intialize threadpool
        ExecutorService pool = Executors.newFixedThreadPool(20);
        
        for(int x=0; x<100; x++){
            
            //get random sleep time [1, 5]
            randomSleep = (randy.nextInt(5)+1);

            //Set sleep time
            sleepingThread t = new sleepingThread(randomSleep);
            
            //no "extra" synchronization required because sleepingThread randomSleep is 
            //a primitive data type so sleeping thread is sent the value, not the reference


            //thread pool completes task
            pool.execute(t);
        
            //Sleep main thread for ~100 milliseconds
            try{
                Thread.sleep(100);
            } catch (InterruptedException e){}


        }
        
        
    }
}
