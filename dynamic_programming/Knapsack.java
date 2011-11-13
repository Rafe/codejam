public class Knapsack{
  public static void main(String[] args){
    int MAX = 8;
    int MIN = 1;
    int[] item = new int[MAX+1];
    int[] value = new int[MAX+1];

    Fruit[] fruits = {
      new Fruit("plam",4,4500),
      new Fruit("apple",5,5700),
      new Fruit("orange",2,2250),
      new Fruit("strawberry",1,1100),
      new Fruit("melon",6,6700)
    };

    for(int i = 0; i < fruits.length; i++){
      for(int s = fruits[i].size;s <= MAX; s++){
        int p = s - fruits[i].size;
        int newValue = value[p] + fruits[i].price;
        if(newValue > value[s]){
          value[s] = newValue;
          item[s] = i;
        }
      }
    }

    System.out.println("item\t price");
    for(int i = MAX; i >= MIN; i-= fruits[item[i]].size){
      System.out.println(fruits[item[i]].name+"\t"+fruits[item[i]].price);
    }

    System.out.println("total\t" + value[MAX]);
  }
}

class Fruit{
  public String name;
  public int size;
  public int price;

  public Fruit(String name,int size,int price){
    this.name = name;
    this.size = size;
    this.price = price;
  }
}
