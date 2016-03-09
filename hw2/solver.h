//
// Created by Christopher on 9/26/2015.
//

#ifndef HW2_C_SOLVER_H
#define HW2_C_SOLVER_H

#include "matrix.h"
#include <cmath>

class solver {
public:
    solver(): m_j(2,2), m_q(1,1), m_r(1,1){};

    matrix inverse( matrix& other )
    {
        matrix id = matrix::identity(other.rows());
        Decompose(other);
        return Solve(id);
    }

    void Decompose(matrix& other)
    {
        int rows = other.rows();
        int cols = other.cols();

        if( rows == cols )
        {
            cols--;
        }
        else if( rows < cols )
        {
            cols = rows - 1;
        }

        m_q = matrix::identity(rows);
        m_r = other;

        for(int j = 0; j < cols; j++)
        {
            for(int i = j+1; i < rows; i++)
            {
                Rotation( m_r(j,j), m_r(i,j) );
                PreMultiply( m_r, j, i);
                PreMultiply( m_q, j, i);
            }
        }

        m_q = m_q.transpose();
    }

    matrix Solve( matrix& other)
    {
        matrix qm(m_q.transpose() * other);

        int cols = m_r.cols();
        matrix s(1, cols);

        for(int i = cols-1; i >= 0; i--)
        {
            s(0,i) = qm(i,0);
            for(int j = i+1; j < cols; j++)
            {
                s(0,i) -= s(0,j) * m_r(i,j);
            }
            s(0,i) /= m_r(i,i);
        }

        return s;
    }

    const matrix& q(){return m_q;}
    const matrix& r(){return m_r;}
private:
    void Rotation( float a, float b)
    {
        float t,s,c;
        if (b == 0)
        {
            c = (a >=0)?1:-1;
            s = 0;
        }
        else if (a == 0)
        {
            c = 0;
            s = (b >=0)?-1:1;
        }
        else if (abs(b) > abs(a))
        {
            t = a/b;
            s = -1/sqrt(1+t*t);
            c = -s*t;
        }
        else
        {
            t = b/a;
            c = 1/sqrt(1+t*t);
            s = -c*t;
        }

        m_j(0,0) = c;
        m_j(0,1) = -s;
        m_j(1,0) = s;
        m_j(1,1) = c;
    }

    void PreMultiply( matrix& other, int i, int j)
    {
        int rowSize = other.cols();

        for(int row = 0; row < rowSize; row++)
        {
            float temp = other(i,row) * m_j(0,0) + other(j,row) * m_j(0,1);
            other(j,row) = other(i,row) * m_j(1,0) + other(j,row) * m_j(1,1);
            other(i,row) = temp;
        }
    }
    matrix m_q, m_r, m_j;
};


#endif //HW2_C_SOLVER_H
