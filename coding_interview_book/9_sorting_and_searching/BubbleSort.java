public class BubbleSort{
  public static void sort(int[] a){
    int temp;
    for(int i=0,length = a.length;i<length;i++){
      for(int j=i+1;j<length;j++){
        if(a[i]>a[j]){
          temp = a[i];
          a[i] = a[j];
          a[j] = temp;
        }
      }
    }
  }

  public static void main(String[] args){
    int[] a = {6,5,4,3,2,123};
    sort(a);
    for(int i:a){
      System.out.println(i);
    }
  }
}
