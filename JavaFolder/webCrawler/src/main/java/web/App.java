/*
Dillon Hussey
WebCrawler Project
    Uses concurrency and okhttp3 to "crawl" websites to look for
    links to add to a list and then crawls those new sites
November 3 2020
For Programming Languages with Brett Huffman
*/


package web;

import java.io.IOException;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;


import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.Response;


/*
 * Hello world!
 *
 */
public class App 
{

    
    OkHttpClient client = new OkHttpClient();
        
        String run(String url) throws IOException {
            Request request = new Request.Builder()
                .url(url)
                .build();
            try (Response response = client.newCall(request).execute()){
                return response.body().string();
            }
        }
//what does a link look like <ahref = "https://sdofijsdofisdoijioj"


    public static void main( String[] args ) throws IOException
    {
        CrawlingThreadTask.setUp();
       // ArrayList<CrawlItem> siteList = new ArrayList<CrawlItem>();
        CrawlItem site = new CrawlItem("npr.org", "http://npr.org", "google.com");
        CrawlingThreadTask.allTasks.add(site);


        ExecutorService pool = Executors.newFixedThreadPool(1);
        CrawlingThreadTask.incrementActiveCount();
        while(CrawlingThreadTask.getActiveCount()>0){
            if(CrawlingThreadTask.allTasks.size()>0){
                pool.execute(new CrawlingThreadTask(CrawlingThreadTask.allTasks.pop()));
                try {
                    Thread.sleep(100);
                } catch (InterruptedException e) {
                    System.out.println("InteruptedException on sleep attempt");
                }
            }
        }
     

        
    }
}
