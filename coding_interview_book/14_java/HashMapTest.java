import java.util.*;

class HashMapTest{
  
  public static void main(String[] args){
    Map<String,String> map = new HashMap<String,String>();
    map.put("test","1234");
    map.put("1234","test");

    System.out.println(map.get("test"));
    System.out.println(map.get("1234"));
  }
}
