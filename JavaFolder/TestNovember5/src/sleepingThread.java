
public class sleepingThread implements Runnable{
    
    private int waitTime;

    //create sleeping thread task
    public sleepingThread(int wT){
        this.waitTime = wT;
    }

    public void run(){
        //wait for set sleep time
        try{
            Thread.sleep(this.waitTime*1000);
        } catch (InterruptedException e){}

        //print thread name and "awake status"
        System.out.println(Thread.currentThread().getName() + "      awake");

    }

}
