// =================================================================================================
// C++ Implementation of Selection Sort
// Author: Matheus José Oliveira dos Santos
// Based on: https://joaoarthurbm.github.io/eda/posts/selection-sort/ acessed on 01/09/2022
// =================================================================================================

#include <iostream>

using namespace std;

int* selection_sort(int mArray[10]){
    static int r[10];

    int array_size = sizeof(mArray)/sizeof(mArray[0]);

    for (int i = 1; i < array_size; i++){
        
    }

    return r;
}

int main(){
    
    cout << "Selection sort algorithm" << endl;

    int example_sample[10] = {1569, 17, 369, 258, 147, 5, 15, 14789, 30, 1920};
    
    int array_size = sizeof(example_sample)/sizeof(example_sample[0]);
    cout << "Size of the array: ";
    cout << array_size << endl;

    cout << "Initial array: ";

    for (int i = 0; i < array_size; i++){
        cout << std::to_string(example_sample[i]) + " ";
    };

    int example_sample_ordered[10];
    example_sample_ordered = selection_sort(example_sample);

    int array_size_ordered = sizeof(example_sample_ordered)/sizeof(example_sample_ordered[0]);

    cout << "Ordered array: ";

    for (int i = 0; i < array_size_ordered; i++){
        cout << std::to_string(example_sample[i]) + " ";
    };

    return 0;
}