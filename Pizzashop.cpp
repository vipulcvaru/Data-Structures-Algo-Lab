#include<iostream>
using namespace std;
const int MAX = 5;

class order
{
    int order_id;

public:
    void acceptorder()
    {
        cout << "\nEnter order id: ";
        cin >> order_id;
    }

    void displayorder()
    {
        cout << order_id << ",";
    }

    friend class Queue;
};

class Queue
{
    order data[MAX];
    int front, rear;

public:
    Queue()
    {
        front = rear = -1;
    }

    int isfull()
    {
        if ((front == 0 && rear == MAX - 1) || front == rear + 1)
            return 1;
        else
            return 0;
    }

    int isempty()
    {
        if (front == -1 && rear == -1)
            return 1;
        else
            return 0;
    }

    void enqueue()
    {
        if (isfull())
        {
            cout << "Queue is full!!\n";
            cout << "Please wait...\n";
        }
        else
        {
            order temp;
            temp.acceptorder();
            rear = (rear + 1) % MAX; // Move rear circularly
            data[rear] = temp;
            cout << "Order placed\n";
            if (front == -1)
                front = 0;
        }
    }

    void dequeue()
    {
        if (isempty())
        {
            cout << "No orders left!!\n";
        }
        else
        {
            cout << "\nOrder served successfully\n";
            if (front == rear)
            {
                // Only one element in the queue, reset front and rear
                front = rear = -1;
            }
            else
            {
                // Move front circularly
                front = (front + 1) % MAX;
            }
        }
    }

    void display()
    {
        if (isempty())
        {
            cout << "No orders left to display\n";
        }
        else
        {
            int i = front;
            cout << "\nOrders in queue:\n";
            if (front <= rear)
            {
                while (i <= rear)
                {
                    data[i].displayorder();
                    i++;
                }
            }
            else
            {
                // Display elements from front to the end of the array
                while (i < MAX)
                {
                    data[i].displayorder();
                    i++;
                }

                // Display elements from the beginning of the array to rear
                i = 0;
                while (i <= rear)
                {
                    data[i].displayorder();
                    i++;
                }
            }
        }
    }
};

int main()
{
    int ch;
    Queue q;
    cout << "\n----PIZZA PLAZZA----\n";
    cout << "\n1. Place order";
    cout << "\n2. Serve order";
    cout << "\n3. Display order";
    cout << "\n4. Exit";
    do
    {
        cout << "\nEnter your choice:  ";
        cin >> ch;

        switch (ch)
        {
        case 1:
            q.enqueue();
            break;
        case 2:
            q.dequeue();
            break;
        case 3:
            q.display();
            break;
        case 4:
            break;
        default:
            cout << "Invalid Choice! Try Again.\n";
            break;
        }
    } while (ch != 4);

    return 0;
}
