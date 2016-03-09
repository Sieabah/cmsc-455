//
// Created by Christopher on 9/26/2015.
//

#ifndef HW2_C_MATRIX_H
#define HW2_C_MATRIX_H

#include <vector>
#include <algorithm>

class matrix {
public:
    matrix( int nRows, int nCols ):
            m_rows(nRows), m_cols(nCols), m_data( nRows * nCols, 0 ) {};

    float& operator()(int row, int col)
    {
        return m_data[col+m_cols*row];
    }

    matrix transpose()
    {
        matrix result(m_cols, m_rows);
        for(int i = 0; i < m_rows; i++)
        {
            for(int j = 0; j< m_cols; j++)
            {
                result(j,i) += (*this)(i,j);
            }
        }
        return result;
    }

    int rows(){return m_rows;}
    int cols(){return m_cols;}
    std::vector<float> data(){return m_data;}

    static matrix identity( int size )
    {
        matrix result(size,size);
        int count = 0;

        std::generate( result.data().begin(), result.data().end(), [&count, size]() {return !(count++%(size+1));});
    }
    matrix operator*(matrix& other)
    {
        matrix result(m_rows, other.cols());
        for(int i = 0; i < m_rows; i++)
        {
            for(int j = 0; j < other.cols(); j++)
            {
                for(int k = 0; k < m_cols; k++)
                {
                    result(i,j) += (*this)(i,k) * other(k,j);
                }
            }
        }

        return result;
    }

private:
    int m_rows;
    int m_cols;

    std::vector<float> m_data;

};


#endif //HW2_C_MATRIX_H
