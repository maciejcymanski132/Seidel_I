#include <iostream>
#include <vector>
#include <time.h>
#include <typeinfo>


bool only_one_right(std::vector <std::vector <double>> A){

    int constr = A.size();
    bool git = true;

    for(int i = 0; i < constr; i++){

        if(A[i][0] != 0){
            git = false;
        }

    }

    return git;
}

bool only_one_left(std::vector <std::vector <double>> A){

    int constr = A.size();
    bool git = true;

    for(int i = 0; i < constr; i++){

        if(A[i][1] != 0){
            git = false;
        }

    }

    return git;
}

std::vector <double> gauss(std::vector <std::vector <double>> A, std::vector <double> b){

    int constr = A.size();

    std::vector <std::vector <double>> matrix = { {0, 0, 0}, {0, 0, 0}};
    std::vector <double> xVector(constr);

    for(int i = 0; i < constr; i++){

        for(int j = 0; j < 2; j++){

            matrix[i][j] = A[i][j];

        }

        matrix[i][constr] = b[i];

    }

    double var = 0;
    double huncwot = 0;

    //to find the elements of diagonal matrix
    for(int j = 0; j < constr; j++){

        for(int i = 0; i < constr; i++){

            if(i != j){

                var = matrix[i][j]/matrix[j][j];

                for(int k = 0; k < constr; k++){

                    huncwot = var*matrix[j][k];
                    matrix[i][k] = matrix[i][k] - huncwot;

                }

            }

        }

    }

    for(int i = 0; i < constr; i++){

        xVector[i] = matrix[i][constr]/matrix[i][i];

    }

    return xVector;
}

std::vector <double> seidel(std::vector <std::vector <double>> A, std::vector <double> b, std::vector <double> c){

    std::vector <double> Xi(2);

    int constr = A.size();
    bool one_variable_left = only_one_left(A);
    bool one_variable_right = only_one_right(A);

    if(one_variable_left == true){

        double max = 0;

        for(int i = 0; i < constr; i++){

            if(max < c[0]*A[i][0]){

                max = c[0]*A[i][0];
                Xi[0] = b[i]/(A[i][0] + A[i][1]);

            }

        }

            Xi[1] = 0;

        return Xi;
    }

    if(one_variable_right == true){

        double max = 0;

        for(int i = 0; i < constr; i++){

            if(max < c[1]*(b[i]/(A[i][0] + A[i][1]))){

                max = c[1]*(b[i]/(A[i][0] + A[i][1]));
                Xi[1] = b[i]/(A[i][0] + A[i][1]);

            }

        }

            Xi[0] = 0;

        return Xi;
    }

    if(A.size() == A[0].size()){

        std::cout << "gałs\n";
        Xi = gauss(A, b);

        return Xi;
    }

    int completelyRandomInteger = 0 + rand() % constr;
    std::cout << "random: " << completelyRandomInteger << "\n";
    std::vector<double> erasedRow(3);

    erasedRow[0] = A[completelyRandomInteger][0];
    erasedRow[1] = A[completelyRandomInteger][1];
    erasedRow[2] = b[completelyRandomInteger];

    A.erase(A.begin() + completelyRandomInteger);
    b.erase(b.begin() + completelyRandomInteger);

    Xi = seidel(A, b, c);
    std::cout << Xi[0] << " " << Xi[1] <<"\n";

    if((erasedRow[0]*Xi[0] + erasedRow[1]*Xi[1]) <= erasedRow[2]){

        return Xi;

    }else{

        int constr_after_deletion = A.size();
        std::vector<double> change(2);
        change[0] = (-1.0)*erasedRow[1]/erasedRow[0];
        change[1] = erasedRow[2]/erasedRow[0];

        for(int i = 0; i < constr_after_deletion; i++){

            A[i][1] += change[0]*A[i][0];
            b[i] += (-1.0)*change[1]*A[i][0];

            //A[i].erase(A[i].begin());
            A[i][0] = 0;

        }

        return seidel(A, b, c);

    }

}

int main(){

    srand(time(NULL));

    std::vector <std::vector <double>> matrixA = {

        {-1, 1}, {-1, 1}, {-1, 1}

    };

    std::vector <double> matrixB = {

        {1, 2, 3}

    };

    std::vector <double> function = {-1, 1};
    int constraints = matrixA.size();

    for(int i = 0; i < constraints; i++){

        for(int j = 0; j < 2; j++){

            std::cout << matrixA[i][j] << " ";

        }

        std::cout << "<= " << matrixB[i];
        std::cout << std::endl;

    }

    std::vector<double> xopt = seidel(matrixA, matrixB, function);

    if(xopt[0] < 0){
        xopt[0] = 0;
    }

    if(xopt[1] < 0){
        xopt[1] = 0;
    }

    std::cout << xopt[0] << " " << xopt[1] << std::endl;


    return 0;
}

//dorobić do macierzy ograniczenia elementarne

//wytropić czemu kod sie konczy


