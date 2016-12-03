

#include <iostream>
#include <cstdlib>

using namespace std;
//This our class for the list
class List{
//In private our variable go
private:

 typedef struct node{
    int data;
    node* next;
    node* perv;
    }* nodePtr;

    //these are our pointers
    nodePtr head;
    nodePtr curr;
    nodePtr temp;
//In this our function go
public:
    List();
    void AddNode(int addData);
    void DeleteNode(int delData);
    void PrintList();

    };



    List::List(){
        head = NULL;
        curr = NULL;
        temp = NULL;
        }

void List::AddNode(int addData){
    nodePtr n = new node;
    n->next = NULL;
     n->perv = NULL;
    n->data = addData;

    if(head != NULL){
        curr = head;
        while(curr->next != NULL){
            curr = curr->next;
        }
        curr->next = n;
    }
    else
    {
        head = n;
    }
}

void List::DeleteNode(int delData){
    nodePtr delPtr = NULL;
    temp = head;
    curr = head;
    while(curr != NULL && curr->data != delData){
        temp = curr;
        curr = curr->next;
    }
    if(curr == NULL){
        cout << delData << " was not in the list\n";
        delete delPtr;
    }
    else{
        delPtr = curr;
        curr = curr->next;
        temp->next = curr;
        delete delPtr;
        cout << "The Value" << delData << "was deleted\n";
}
}

void List::PrintList(){
    curr = head;
    while(curr != NULL)

    {
        cout << curr->data << endl;
        curr = curr->next;
    }
}
int main(int argc, char** argv){
    List Paul;
    Paul.AddNode(2);
    Paul.AddNode(3);
    Paul.AddNode(7);
    Paul.PrintList();

    Paul.DeleteNode(3);
    Paul.PrintList();


    return 0;
}
