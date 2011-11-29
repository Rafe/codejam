public class Moderate1{
  public static void main(String[] args){
  }

  public static int swap(int a, int b){
    a = a + b; // a : a + b , b: b
    b = -(b - a); // a: a + b, b: a
    a = a - b; // a: b, b:a
  }

  public static int swapInBit(int a, int b){
    a = a ^ b // a : a^b , b:b
    b = b ^ a; // a:a^b, b:a
    a = a ^ b;
  }
}
