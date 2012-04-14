public class QuickSort{
  public static void main(String args[]){
    int[] s = {4,2,5,4,3,2,1,12};
    sort(s,0,s.length-1);
  }

  public static void print(int[] array){
    for(int e:array){
      System.out.print(e + ",");
    }
    System.out.println("");
  }

  public static void sort(int[] array,int first,int last){
    if(array.length < 1 || first >= last ){
      return ;
    }

    int i = first;
    int j = last;
    int pivot = array[i++];
    while(i < j){
      if(array[i] > pivot && array[j] < pivot ){
        swap(array,i,j);
      }else {
        if(array[i] <= pivot){
          i++;
        }     
        if(array[j] >= pivot){
          j--;
        }
      } 
    }
    if(array[first]>array[j]){
      swap(array,first,j);
    }
    print(array);
    sort(array,first,j - 1);
    sort(array,j + 1,last);
  }

  public static void swap(int[] array, int i, int j){
    int t = array[i];
    array[i] = array[j];
    array[j] = t;
  }
}
