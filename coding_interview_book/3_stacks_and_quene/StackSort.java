public class StackSort{
  public static Stack<int> sort(Stack<int> s){
    Stack<int> r = new Stack<int>();

    while(s.isEmpty()){
      int temp = s.pop();
      while(!r.isEmpty() && r.peek() > temp){
        s.push(r.pop());
      }
      r.push(temp);
    }
  }
}
