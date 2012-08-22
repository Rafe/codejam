import java.lang.Math;
import java.util.*;

public class CheatSheet{
  public static void main(String[] args){
    int[] anArray = {
      100, 200, 300,
      400, 500, 600,
      700, 800, 900
    };
    Arrays.sort(anArray); //sort array as ascend sequence
    Math.max(100, Math.max(200, 300)); // tri compare
  }

  public static void StringAPI(){
    String a = "This is";
    String b = "a pan";

    a.length();
    a.charAt(4);
    a.subString(2,5);
    a.startWith("the");
    a.indexOf("is");
    a.concat(c);
    b.replace("pan","pen");
    a.split(" ")[1]; // is
    a.equals(b);
  }

  public static void InAndOut(){
    //java.io
    System.in.readInt();
    System.in.readDouble();

    //read from file
    BufferReader reader = new BufferReader(new FileReader("./file.txt"));
    //read from input
    BufferReader input = new BufferReader(new InputStreamReader(System.in));
    reader.read(); //read single char
    reader.readLine(); // read line
    input.readLine();
  }

  //object orient
  class Person{};
  interface ITestable{
    public int test(){};
  };
  interface ISuperTestable extends ITestable{
    public int test(){};
  }
  class Programmer extends Person implements ITestable{
    public int test(){};
  }
  //annotation
  public @interface language{
    String[] lang;
  }

  @language("c","c++","c#","java","perl","python","ruby");
  class Hacker extends Programmer implements ITestable{
    public int test(){};
  }

  //hash table
  public static void HashAndArray(){
    HashMap<Integer, Person> map = new HashMap<Integer,Person>;
    map.put(1,new Person);
    map.get(1);

    ArrayList<String> sentence = new ArrayList<String>();
    for(String word : words){
      sentence.add(word);
    }

    //StringBuffer / StringBuilder
    StringBuilder sentence = new StringBuilder();
    sentence.append("word");

  }

  //stack and quene
  public static void StackAndQuene(){
    Stack<int> stack = new Stack<int>();
    stack.push(1);
    stack.pop();
    stack.empty();
    stack.peek();

    Quene<int> quene = new Quene<int>();
    quene.poll();
    quene.add();

    LinkedList<int> list = new LinkedList();
    list.add(12);
    list.removeFirst(); // same as remove()
  }

  //Tree and graph
  public static void TreeAndGraph(){
    //tree:
    class TreeNode(){
      int data;
      TreeNode left;
      TreeNode right;
    }

    //inOrder
    public visit(TreeNode n){
      visit(left);
      n;
      visit(right);
    }

    //preorder
    public visit(TreeNode n){
      n;
      visit(left);
      visit(right);
    }
    //post order
    public visit(TreeNode n){
      visit(right);
      visit(left);
      n;
    }

    //BreadthFirstSearch
    public visit(TreeNode n){
      n;
      quene.add(n.left);
      quene.add(n.right);
      visit(quene.remove); // process first in -> [1] -> [2,3] -> [3,4,5] -> [4,5,6,7];
    }

    //DepthFirstSearch
    public visit(TreeNode n){
      n;
      stack.push(n.left);
      stack.push(n.right);
      visit(quene.pop); // push -> [1] -> [2,3] -> [4,5,3] -> [6,7,5,3];
    }
  }

  //thread
  public static void Thread(){
    class Foo implements Runnable{
      public void run(){
        while(true) beep();
      }
    }
    Foo foo = new Foo();
    Thread myThread = new Thread(foo);
    myThread.start();
  }
}
