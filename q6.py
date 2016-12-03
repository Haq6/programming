
Pseudocode 

For i=  length-1 i > = 0 i

Out i




Implementation 

using namespace std;

int main()
{
    string l;
    cout << "Please Enter a word to reverse: " << endl;
    if(getline(cin, l))
    {
        cout << "Your word are reversed: " << endl;
        for(int i= l.length()-1; i >= 0; i--)

        {
            cout << l[i];

        }
    }


    return 0;
