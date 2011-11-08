import java.util.*;
import java.lang.*;

public class MergeSort{
  public static int[] merge(int[] a, int[] b){
    int[] r = new int[a.length + b.length];
    int i=0,j=0,count=0;
    while(i< a.length && j<b.length){
      if(a[i]<b[j]){
        r[count++] = a[i++];
      }else{
        r[count++] = b[j++];
      }
    }
    while(i<a.length){
      r[count++] = a[i++];
    }
    while(j<b.length){
      r[count++] = b[j++];
    }
    return r;
  }

  public static int[] sort(int[] a){
    if(a.length <= 1){
      return a;
    }

    int mid = (int) Math.floor(a.length /2);
    int[] a1 = Arrays.copyOfRange(a,0,mid);
    int[] a2 = Arrays.copyOfRange(a,mid,a.length);
    return merge(sort(a1),sort(a2));
  }

  public static void main(String[] args){
    int[] a = {3,23,45,123,56,12,123,54};
    int[] b = sort(a);

    for(int e:b){
      System.out.println(e);
    }
  }
}
