package web;

//import java.util.Date;

public class CrawlItem {
    String id;
    String address;
    String domain;
    int linkCount;
    String parentDom;

    public CrawlItem(String dom, String add, String parent){
        this.domain = dom;
        this.address = add;
        this.parentDom = parent;
    }

    public String displayAdress(){
        return this.domain+"\n"+this.address+"\n"+this.parentDom+"\n\n";
    }

    public String toString(int x){
        return x+ "\t\t" + Thread.currentThread().getName() + "\t\t" + this.address;
    }

    public void setLinkCount(int c){
        linkCount = c;
    }
    
}
