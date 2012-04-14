import java.util.*;

public class BusinessTasks {
  public static String getTask(String[] list, int n){
    int i;
    ArrayList l = new ArrayList();

    for(i=0;i<list.length;i++){
      l.add(list[i]);
    }

    i = 0;
    while (l.size() > 1) {
      i = (n+i-1) % (l.size());
      l.remove(i);
    }

    return l.remove(0).toString();
  }
}
