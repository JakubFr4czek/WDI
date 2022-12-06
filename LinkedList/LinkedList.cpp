#include "Linkedlist.h"

void ll::LinkedList::Insert(int val){

    ll::Node* temp = new ll::Node(val);

    temp->next = (ll::LinkedList::home == nullptr)?nullptr:ll::LinkedList::home;

    ll::LinkedList::home = temp;

}

void ll::LinkedList::Remove(int val){

    ll::Node* temp = ll::LinkedList::home;
    ll::Node* prev = temp;

    while(temp != nullptr){

        if(temp -> value == val){

            prev->next = temp->next;
            delete temp;


        }else{ 
            prev = temp; 
            temp = temp->next;
        }

    }

}

int ll::LinkedList::Pos(int index){

    ll::Node * temp = ll::LinkedList::home;

    int cnt = 0;

    while(temp != nullptr){

        if(index == cnt) return temp->value;

        cnt++;
        temp = temp->next;

    }

    return -1;

}

