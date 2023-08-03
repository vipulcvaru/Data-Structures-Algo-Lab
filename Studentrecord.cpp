#include <iostream>
using namespace std;

// Node class to represent each student record in the linked list
class node
{
public:
    int roll;
    string name;
    node *next;
};

// Global variable representing the head of the linked list
node *head = new node();

// Function to check if a student record with a given roll number exists in the linked list
bool check(int x)
{
    if (head == NULL)
        return false;

    node *t = head;
    while (t != NULL)
    {
        if (t->roll == x)
            return true;
        t = t->next;
    }
    return false;
}

// Function to insert a new student record into the linked list
void Insert_Record(int roll, string name)
{
    if (check(roll))
    {
        cout << "Student with this record already exists!!\n";
        return;
    }

    node *t = new node();
    t->roll = roll;
    t->name = name;
    t->next = NULL;

    // Insert at the beginning of the linked list or in the middle/end
    if (head == NULL || (head->roll >= t->roll))
    {
        t->next = head;
        head = t;
    }
    else
    {
        node *c = head;
        while (c->next != NULL && c->next->roll < t->roll)
        {
            c = c->next;
        }
        t->next = c->next;
        c->next = t;
    }

    cout << "Record inserted successfully!\n";
}

// Function to search for a student record with a given roll number
void Search_Record(int roll)
{
    if (!head)
    {
        cout << "No such record available!!\n";
        return;
    }
    else
    {
        node *p = head;
        while (p)
        {
            if (p->roll == roll)
            {
                cout << "Roll Number: " << p->roll << endl;
                cout << "Name: " << p->name << endl;
                return;
            }
            p = p->next;
        }
        cout << "No such record available\n";
    }
}

// Function to delete a student record with a given roll number from the linked list
int Delete_Record(int roll)
{
    node *t = head;
    node *p = NULL;

    // Deletion at the beginning
    if (t != NULL && t->roll == roll)
    {
        head = t->next;
        delete t;
        cout << "Record Deleted Successfully\n";
        return 0;
    }

    // Deletion other than the beginning
    while (t != NULL && t->roll != roll)
    {
        p = t;
        t = t->next;
    }
    if (t == NULL)
    {
        cout << "Record does not Exist\n";
        return -1;
    }
    p->next = t->next;
    delete t;
    cout << "Record Deleted Successfully\n";
    return 0;
}

// Function to display all the student records in the linked list
void Show_Record()
{
    node *p = head;
    if (p == NULL)
    {
        cout << "No Record Available\n";
    }
    else
    {
        cout << "Roll Number\tName\n";
        while (p != NULL)
        {
            cout << p->roll << "\t\t" << p->name << "\n";
            p = p->next;
        }
    }
}

int main()
{
    head = NULL;
    string Name;
    int Roll;

    // Menu-driven program
    while (true)
    {
        cout << "\n\t\tWelcome to Student Record Management System\n\n\tPress\n\t1 to create a new Record\n\t2 to delete a student record\n\t3 to Search a Student Record\n\t4 to view all student records\n\t5 to Exit\n";
        cout << "\nEnter your Choice: ";
        int Choice;

        // Enter Choice
        cin >> Choice;
        if (Choice == 1)
        {
            cout << "Enter Name of Student: ";
            cin >> Name;
            cout << "Enter Roll Number of Student: ";
            cin >> Roll;

            Insert_Record(Roll, Name);
        }
        else if (Choice == 2)
        {
            cout << "Enter Roll Number of Student whose record is to be deleted: ";
            cin >> Roll;
            Delete_Record(Roll);
        }
        else if (Choice == 3)
        {
            cout << "Enter Roll Number of Student whose record you want to Search: ";
            cin >> Roll;
            Search_Record(Roll);
        }
        else if (Choice == 4)
        {
            Show_Record();
        }
        else if (Choice == 5)
        {
            exit(0);
        }
        else
        {
            cout << "Invalid Choice! Try Again.\n";
        }
    }
    return 0;
}
