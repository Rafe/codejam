public class SelectionSort{
  public static void sort(int[] a){
    int s,temp;
    for(int i=0,length=a.length;i<length;i++){
      s = i;
      for(int j=i+1; j<length; j++){
        if(a[s]>a[j]){
          s = j;
        }
      }
      temp = a[i];
      a[i] = a[s];
      a[s] = temp;
    }
  }

  public static void main(String args[]){
    int[] a = {34,123,65,12,54,3,57,123,12,1,1,1,1,1};
    sort(a);
    for(int e:a){
      System.out.println(e);
    }
  }
}
