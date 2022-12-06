#include<iostream>
#include "LinkedList.h"

using namespace ll;

int main(){

    LinkedList linkedList;

    linkedList.Insert(2);
    linkedList.Insert(1);
    linkedList.Insert(1);
    linkedList.Insert(5);

    linkedList.Remove(1);

    for(int i = 0; i < 3; i++){

        std::cout<<linkedList.Pos(i)<<std::endl;

    }


}