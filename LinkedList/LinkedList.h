namespace ll{

class Node{

    public:

        int value;
        Node* next; 

        Node(int val){

            value = val;
            next = nullptr; 

        }  

};

class LinkedList{

    private:

        Node* home;

    public:

        void Insert(int);
        void Remove(int);

        int Pos(int);
        void Reverse();
        void Sort(bool); //false - descending, true - ascending
        void Destroy();

        LinkedList(){

            home = nullptr;

        }



    




};


}