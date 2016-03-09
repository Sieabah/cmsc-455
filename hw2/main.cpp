#include <iostream>
#include "matrix.h"
#include "solver.h"

using namespace std;

vector<float> leastsq( const vector<float> x, const vector<float> y, int degree )
{
    degree++;

    int nCount = x.size();

    matrix xMat( nCount, degree );
    matrix yMat( nCount, 1 );

    for( int i = 0; i < nCount; i++)
    {
        yMat(i, 0) = y[i];
    }

    for( int row = 0; row < nCount; row++)
    {
        float val = 1.0f;
        for( int col = 0; col < degree; col++)
        {
            xMat(row, col) = val;
            val *= x[row];
        }
    }

    matrix xTran(xMat.transpose());
    matrix xMul( xTran * xMat );
    matrix xyMul ( xTran * yMat );

    solver slvr;
    slvr.Decompose(xyMul);
    matrix coEf = slvr.Solve(xyMul);
    return coEf.data();
}

int main() {
    vector<float> x; x = {0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9};
    vector<float> y; y = {0.0,6.0,12.0,5.5,4.8,4.5,4.5,4.5,4.5,4.5,4.5,4.5,4.5,4.5,4.5,4.5,4.5,4.5,0.0};


    for(int i = 1; i < 18; i++)
    {
        cout << "Degree: " << i << " | ";

        vector<float> out = leastsq(x,y,i);

        for(int j = 0; j < out.size(); j++)
        {
            cout << out[j] << ",";
        }
        cout << endl;
    }
}