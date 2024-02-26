package ejercicio_08;

import java.util.ArrayList;
import java.util.List;

public class JesusWay69 {

  public static void main(String[] args) {

    Stack stack_instance = new Stack();
    Queue queue_instance = new Queue();

    stack_instance.add(1, 11);
    stack_instance.show();
    System.out.println("La lista tiene " + stack_instance.leight() + " números\n");
    stack_instance.unstack();
    stack_instance.show();
    System.out.println("La lista tiene " + stack_instance.leight() + " números\n");
    
    queue_instance.add(1, 11);
    queue_instance.show();
    System.out.println("La lista tiene " + queue_instance.leight() + " números\n");
    queue_instance.dequeue();
    queue_instance.show();
    System.out.println("La lista tiene " + queue_instance.leight() + " números\n");
    

  }

}



class Stack {


  public ArrayList my_stack_list;

  public Stack() {
    my_stack_list = new ArrayList<>();

  }

  public void add(int init_num, int end_num) {

    for (int i = init_num; i < end_num; i++) {
      my_stack_list.add(i);

    }

  }

  public void unstack() {

    my_stack_list.remove(my_stack_list.size() - 1);
  }

  public int leight() {

    return my_stack_list.size();
  }

  public void show() {
    System.out.println(my_stack_list);
  }

}

class Queue {

  public ArrayList my_stack_list;

  public Queue() {
    my_stack_list = new ArrayList<>();

  }

  public void add(int init_num, int end_num) {

    for (int i = init_num; i < end_num; i++) {
      my_stack_list.add(i);

    }

  }

  public void dequeue() {

    my_stack_list.remove(0);
  }

  public int leight() {

    return my_stack_list.size();
  }

  public void show() {
    System.out.println(my_stack_list);
  }

}
