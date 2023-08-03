#include <iostream>
using namespace std;

class Queue
{
public:
    int size;
    int start = -1;
    int end = -1;
    int *array;

    // Constructor to initialize the queue with a given size
    Queue(int s)
    {
        size = s;
        array = new int[size];
    }

    // Destructor to release memory occupied by the queue
    ~Queue()
    {
        delete[] array;
    }

    // Function to add an element to the end of the queue (enqueue)
    void enqueue(int x)
    {
        if (end == size - 1)
        {
            cout << "Queue overflow !!\n";
        }
        else
        {
            // Increment 'end' to move the pointer to the next empty position,
            // and then store the new element in that position.
            array[++end] = x;
        }
    }

    // Function to remove an element from the front of the queue (dequeue)
    void dequeue()
    {
        if (start == end)
        {
            cout << "Queue underflow !!\n";
        }
        else
        {
            // Increment 'start' to move the pointer to the next element to be dequeued.
            start++;
        }
    }

    // Function to display the contents of the queue
    void display()
    {
        cout << "Queue contains: ";
        if (start == end)
        {
            // If 'start' is equal to 'end', the queue is empty.
            cout << "Empty\n";
        }
        else
        {
            // Print the elements from 'start+1' to 'end' since these are the elements in the queue.
            for (int i = start + 1; i <= end; i++)
            {
                cout << array[i] << " ";
            }
            cout << endl;
        }
    }
};

int main()
{
    int size;
    cout << "Enter the size of the queue: ";
    cin >> size;

    // Create a queue object with the given size
    Queue j(size);

    int choice, job;
    while (true)
    {
        cout << "\n1. Enqueue a job\n";
        cout << "2. Dequeue a job\n";
        cout << "3. Display the queue\n";
        cout << "4. Exit\n";
        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice)
        {
        case 1:
            cout << "Enter the job to enqueue: ";
            cin >> job;
            // Call the enqueue function to add the job to the queue
            j.enqueue(job);
            break;
        case 2:
            // Call the dequeue function to remove the front job from the queue
            j.dequeue();
            break;
        case 3:
            // Call the display function to show the contents of the queue
            j.display();
            break;
        case 4:
            // Exit the program if the user chooses '4'
            return 0;
        default:
            cout << "Invalid choice. Please try again.\n";
        }
    }

    return 0;
}
