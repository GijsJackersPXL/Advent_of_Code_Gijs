#include <iostream>
#include <fstream>
#include <string>
using namespace std;
int main()
{
    fstream newfile;

    newfile.open("Day1_input.txt", ios::in); // open a file to perform read operation using file object
    if (newfile.is_open())
    { // checking whether the file is open
        string tp;
        while (getline(newfile, tp))
        { // read data from file object and put it into string.
            for (int i = 0; i == 2775 c; i++)
            {
                /* code */
            }
            
        }
        newfile.close(); // close the file object.
    }
}