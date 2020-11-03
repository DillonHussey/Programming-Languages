package web;
import java.util.*;
import java.io.IOException;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.Response;
import java.util.regex.*;


//This class will create have a runnable method to be passed to the thread pool to execute. It will also have a re-usable OKHttpClient to reduce processing time
public class CrawlingThreadTask implements Runnable{
    private static int activeCount = 0;
    private String address;
    private String body;
    private CrawlItem site;

     static HashMap<String, CrawlItem> allItems = new HashMap<String, CrawlItem>();
    
    private static HashMap<String, CrawlItem> blacklist;

     static Stack<CrawlItem> allTasks = new Stack<CrawlItem>();

    //allItems = new HashMap<String, CrawlItem>();
    public static void setUp(){
        allItems.put("https://google.com", null);
        allItems.put("http://google.com",null);
        allItems.put("https://www.google.com", null);
        allItems.put("http://www.google.com",null);
        updateBlacklist();
    }
    

    public static synchronized void updateBlacklist(){
        blacklist = (HashMap<String, CrawlItem>) allItems.clone();
    }


    //this regex targets any link in the body of the website
    //Pattern urlRegex = Pattern.compile("['\"](http[s]:\\/\\/.*?)['\"]");
    final Pattern urlRegex = Pattern.compile("(http[s]:\\/\\/.*?)['\"]");

    //this regex targets the top domain
    final Pattern FQDN = Pattern.compile("\\/\\/(.*?)[\\/\n].*?");

    private Matcher urlmatcher;
    private OkHttpClient client;

    //Crawling Task Constructor. Establishes CrawlItem to be crawled and creates the OkHttpClient only once to reduce processing time.
    public CrawlingThreadTask(CrawlItem item){
        //client = new OkHttpClient();
        site =item;

    }


    //this will need to set the data to the class array
    public void setActive(CrawlItem website) throws IOException{
        site = website;
    }


    //retrieves body from website of this.address
    public String retrieveBody() throws IOException {
        
        client = new OkHttpClient();
/*
        String run(String url) throws IOException {
          Request request = new Request.Builder()
              .url(url)
              .build();
        
          try (Response response = client.newCall(request).execute()) {
            return response.body().string();
          }
        }
        */        
        Request request = new Request.Builder()
            .url(this.address)
            .build();
        try (Response response = this.client.newCall(request).execute()){
            String bod = response.body().string();
            return bod;
            
        }
    
    }

    //use regex on body to find links and send append new CrawlItems to the array of CrawlItems
    public LinkedList<String> findLinks() {
        LinkedList<String> links = new LinkedList<String>();
        this.urlmatcher = this.urlRegex.matcher(body);
        String longStringLinks = "";
        while(urlmatcher.find()){
            //check og list for dup FDQN (SYNC THIS PART, then add)

            String a = urlmatcher.group();
            longStringLinks = longStringLinks + a +"\n";
            links.add(a);

        }
        links.add(longStringLinks);
        return links;  
    }

    public LinkedList<CrawlItem>  prepNValLinks(LinkedList<String> links){
        
        //use another regex which targets address for some string before .com, .edu, .org, .gov, .net.
        //additionally, blacklist checked links and search engines
        this.urlmatcher = this.FQDN.matcher(links.getLast());
        LinkedList<CrawlItem> tbAdded = new LinkedList<CrawlItem>();
        int x=0;
   
        //call for  blacklist to quickly reduce number of duplicate links and put items in hashMap so lock time is reduced
        while(urlmatcher.find()){

            String a = urlmatcher.group();
            //checks parent domain and  blacklist for search engines/used sites
            if(!blacklist.containsKey(a) && !a.contains(site.domain) )
            {
                tbAdded.add(new CrawlItem(a, links.get(x), site.domain ));
            }
            x++;
        }
        return tbAdded;
    }

    //triggers set active
    public void run(){
        incrementActiveCount();
        this.address = site.address;
        
        
        try{
            this.body = this.retrieveBody(); //this retrieves the body of the website
        } catch(Exception ex){
            
        }

        //use regex to find links with domain other than original domain and prior domain
        LinkedList<String> allLinks = findLinks();

        //validate FQDN, return CrawlItems of FQDN, Full link, and keep id empty.
        LinkedList<CrawlItem> tbAdded = prepNValLinks(allLinks);

        //go through process of appending links to master list and list to be crawled while checking for duplication 
        addCrawlItems(tbAdded);
        
        decrementActiveCount();

    }



    //add crawl items to Hashmap and add tasks to stack
    public synchronized void addCrawlItems(LinkedList<CrawlItem> items){
        for(int x=0; x<items.size();x++){
            CrawlItem it = items.get(x);
            if(!allItems.containsKey(it.domain))
            {
                System.out.println(it.toString(allItems.size()));
                allItems.put(it.domain, it);
                allTasks.add(it);
            }
        }
    }


    //get and increment/decrement methods for active thread counter
    //get Active Count
    public static synchronized int getActiveCount(){    return activeCount++;   }
    //Increment and return Active Count
    public static synchronized int incrementActiveCount(){    return ++activeCount;}
    //decrement and return active count
    public static synchronized int decrementActiveCount(){    return --activeCount;}
    }



