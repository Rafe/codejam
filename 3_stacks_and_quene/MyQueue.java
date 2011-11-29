public class MyQueue<T>{
  Stack<T> s1,s2;
  public MyQueue(){
    s1 = new Stack<T>();
    s2 = new Stack<T>();
  }

  public int size(){
    return s1.size() +s2.size();
  }

  public T peek(){
    if(!s2.empty()) return s2.pop();
    while(!s2.empty()) s2.push(s1.pop());
    return s2.peek();
  };

  public T unshift(){
    if(!s2.empty()) return s2.pop();
    while(!s2.empty()) s2.push(s1.pop());
    return s2.pop();
  };

  public boolean shift(T element){
    s1.push(element);
  };
}
