import java.lang.*;
import java.util.*;

public class Counter{

  private int counter = 0;
  //synchronized access for multithreads
  public synchronized void increment(int x) {
    counter += x;
  }
  public int getCounter(){
    return counter;
  }

  public static void main(String[] args){
    final Counter counter = new Counter();
    for(int i = 0; i < 2; i++){
      new Thread(new Runnable() {
        public void run() {
          int x = 0;
          for(int i = 0; i < 100000000; i++)
            x++;
          counter.increment(x);
        }
      }).start();
    }

    try{
      Thread.sleep(20000);
    }catch(InterruptedException e){
      System.out.println(e.getMessage());
    }
    System.out.println(counter.getCounter());
    // 200000000
  }
}
