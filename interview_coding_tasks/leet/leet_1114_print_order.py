"""
Suppose we have a class:

public class Foo {
  public void first() { print("first"); }
  public void second() { print("second"); }
  public void third() { print("third"); }
}
The same instance of Foo will be passed to three different threads. Thread A will call first(), thread B will call second(), and thread C will call third(). Design a mechanism and modify the program to ensure that second() is executed after first(), and third() is executed after second().

Note:

We do not know how the threads will be scheduled in the operating system, even though the numbers in the input seem to imply the ordering. The input format you see is mainly to ensure our tests' comprehensiveness.

 

Example 1:

Input: nums = [1,2,3]
Output: "firstsecondthird"
Explanation: There are three threads being fired asynchronously. The input [1,2,3] means thread A calls first(), thread B calls second(), and thread C calls third(). "firstsecondthird" is the correct output.
Example 2:

Input: nums = [1,3,2]
Output: "firstsecondthird"
Explanation: The input [1,3,2] means thread A calls first(), thread B calls third(), and thread C calls second(). "firstsecondthird" is the correct output.
"""
from typing import Callable
import threading

class Foo:
    def __init__(self):
        self.first_done = threading.Event()
        self.second_done = threading.Event()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        # printFirst()
        from time import sleep
        sleep(1)
        print(f"{printFirst}")
        self.first_done.set()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.first_done.wait()
        # printSecond() outputs "second". Do not change or remove this line.
        # printSecond()
        print(f"{printSecond}")
        self.second_done.set()


    def third(self, printThird: 'Callable[[], None]') -> None:
        self.second_done.wait()
        # printThird() outputs "third". Do not change or remove this line.
        # printThird()
        print(f"{printThird}")


if __name__ == '__main__':
    threads = []
    f = Foo()
    t = threading.Thread(target=f.third, args=("ccc",))
    threads.append(t)
    t = threading.Thread(target=f.second, args=("bbb",))
    threads.append(t)
    t = threading.Thread(target=f.first, args=("aaa",))
    threads.append(t)
    for i in range(3):
        threads[i].start()
    