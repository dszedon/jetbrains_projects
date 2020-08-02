"""
NUMERIC MATRIX PROCESOR

Here’s a project for devoted matrix enthusiasts: 
learn to perform a variety of operations on matrices including addition, multiplication, finding the determinant, and dealing with inverse matrices. 
If you are working on your tech or math major, this project is a good chance for you to learn matrices in action and not just in your notebook.

Stage 1
Use nested lists to add matrices.

Stage 2
Learn to multiply a matrix by a number and display the result.

Stage 3
Multiply matrices and create a menu where you can list all the awesome abilities of your matrix processor.

Stage 4
Add another useful operation to your processor: allow matrix transposition, and then add this option to the menu.

Stage 5
Use recursion to enable your program to find the determinant.

Stage 6
Yet another possible operation is finding the inverse of a matrix: add this option to your program.


TODO:
Use a single format for functions, i.e. input parameters, return, local or global varibales, etc.
Get better with the recursions

"""


import copy


def mtrx1_dim():
    global dim
    dim = [int(x) for x in input("Enter size of first matrix: ").split()]
    while True:
        mtrx1.append([float(x) for x in input("Enter first matrix:").split()])
        if ((len(mtrx1[-1])) > dim[1]) or ((len(mtrx1[-1])) < dim[1]):
            print("The operation cannot be performed.")
            mtrx1.remove(mtrx1[-1])
        elif len(mtrx1) >= dim[0]:
            break


def mtrx2_dim():
    global dim2
    dim2 = [int(x) for x in input("Enter size of second matrix: ").split()]
    while True:
        mtrx2.append([float(x) for x in input("Enter second matrix:").split()])
        if (len(mtrx2[-1])) > dim2[1]:
            print("The operation cannot be performed.")
            mtrx2.remove(mtrx2[-1])
        elif len(mtrx2) >= dim2[0]:
            break


def clean_mtrx():
    del mtrx1[:]
    del mtrx2[:]
    del result[:]
    del res_mtrx[:]
    del m_cof[:]
    del minor[:]
    del cof[:]


def result_print(result):
    newlst = []
    print("The result is:")
    if type(result) is list:
        for m in range(0, len(result)):
            for n in range(0, len(result[0])):
                newlst.append(result[m][n])
            print(*newlst)
            newlst = []
            if (len(newlst)) == (len(result)):
                break
    else:
        print(result)
    print()


def add_cond():
    mtrx1_dim()
    mtrx2_dim()
    while True:
        if (dim[0] != dim2[0]) and (dim[1] != dim2[1]):
            print("The operation cannot be performed.")
            clean_mtrx()
            break
        else:
            add_mtrx(mtrx1, mtrx2)
            clean_mtrx()
            break


def add_mtrx(mtrx1, mtrx2):

    rows_mtrx1 = len(mtrx1)
    cols_mtrx2 = len(mtrx2[0])

    res_mtrx = [[mtrx1[i][j] + mtrx2[i][j]
                 for j in range(cols_mtrx2)] for i in range(rows_mtrx1)]

    result_print(res_mtrx)


def esc_mtrx():
    mtrx1_dim()
    esc = int(input("Enter constant:"))
    res_mtrx = [
        [mtrx1[i][j] * esc for j in range(0, len(mtrx1[0]))]
        for i in range(0, len(mtrx1))
    ]

    result_print(res_mtrx)
    clean_mtrx()


def mult_cond():
    mtrx1_dim()
    mtrx2_dim()
    while True:
        if dim[1] != dim2[0]:
            print("The operation cannot be performed.")
            clean_mtrx()
            break
        else:
            mult_mtrx(mtrx1, mtrx2)
            clean_mtrx()
            break


def zeros_matrix(rows, cols):
    M = []
    while len(M) < rows:
        M.append([])
        while len(M[-1]) < cols:
            M[-1].append(0.0)

    return M


def mult_mtrx(mtrx1, mtrx2):
    rows_mtrx1 = len(mtrx1)
    cols_mtrx1 = len(mtrx1[0])
    cols_mtrx2 = len(mtrx2[0])

    res_mtrx = zeros_matrix(rows_mtrx1, cols_mtrx2)

    for i in range(rows_mtrx1):
        for j in range(cols_mtrx2):
            total = 0
            for ii in range(cols_mtrx1):
                total += mtrx1[i][ii] * mtrx2[ii][j]
            res_mtrx[i][j] = total
    result_print(res_mtrx)


def transpose():
    action2 = str(
        input(
            """1. Main diagonal
2. Side diagonal
3. Vertical line
4. Horizontal line"""
        )
    )
    mtrx1_dim()
    if action2.isdigit():
        action2 = int(action2)
        if action2 == 1:
            result_print(t_main(mtrx1))
        elif action2 == 2:
            result_print(t_side(mtrx1))
        elif action2 == 3:
            result_print(t_vert(mtrx1))
        elif action2 == 4:
            result_print(t_hor(mtrx1))
        else:
            print("The operation cannot be performed.")
    else:
        print("The operation cannot be performed.")
    clean_mtrx()


def t_main(mtrx1):

    rows_mtrx1 = len(mtrx1)
    cols_mtrx1 = len(mtrx1[0])
    res_mtrx = zeros_matrix(rows_mtrx1, cols_mtrx1)

    for i in range(0, len(mtrx1)):
        for j in range(0, len(mtrx1[0])):
            res_mtrx[j][i] = mtrx1[i][j]
    return res_mtrx


def t_side(mtrx1):
    for x in range(0, len(mtrx1)):
        mtrx1[x].reverse()
    mtrx1.reverse()
    res_mtrx = mtrx1
    rows_mtrx1 = len(mtrx1)
    cols_mtrx1 = len(mtrx1[0])
    res_mtrx = zeros_matrix(rows_mtrx1, cols_mtrx1)

    for i in range(0, len(mtrx1)):
        for j in range(0, len(mtrx1[0])):
            res_mtrx[j][i] = mtrx1[i][j]
    return res_mtrx


def t_vert(mtrx1):
    for x in range(0, len(mtrx1)):
        mtrx1[x].reverse()
    res_mtrx = mtrx1
    return res_mtrx


def t_hor(mtrx1):
    mtrx1.reverse()
    res_mtrx = mtrx1
    return res_mtrx


def det_cond(mtrx1):
    if len(mtrx1) == 1:
        result_print(mtrx1)
    elif len(mtrx1) == 2:
        result_print(det_2x2(mtrx1))
    elif len(mtrx1) == 3:
        result_print(det_3x3(mtrx1))
    elif len(mtrx1) == 4:
        result_print(det_4x4(mtrx1))
    elif len(mtrx1) == 5:
        result_print(det_5x5(mtrx1))
    clean_mtrx()


def det_cond2(mtrx1):
    if len(mtrx1) == 1:
        return (mtrx1)
    elif len(mtrx1) == 2:
        return det_2x2(mtrx1)
    elif len(mtrx1) == 3:
        return det_3x3(mtrx1)
    elif len(mtrx1) == 4:
        return det_4x4(mtrx1)
    elif len(mtrx1) == 5:
        return det_5x5(mtrx1)


def det_2x2(mtrx):
    det_mtrx = mtrx[0][0] * mtrx[1][1] - mtrx[0][1] * mtrx[1][0]
    return det_mtrx


def det_3x3(mtrx):
    sub_mtrx1 = [[mtrx[j][i]
                  for i in range(1, len(mtrx))] for j in range(1, len(mtrx))]

    sub_mtrx2 = [[mtrx[j][i]
                  for i in range(0, len(mtrx))] for j in range(1, len(mtrx))]

    for x in range(0, 2):
        sub_mtrx2[x].pop(1)

    sub_mtrx3 = [[mtrx[j][i] for i in range(
        0, len(mtrx[:2]))] for j in range(1, len(mtrx[:3]))]

    det_mtrx = (
        mtrx[0][0] * det_2x2(sub_mtrx1)
        - mtrx[0][1] * det_2x2(sub_mtrx2)
        + mtrx[0][2] * det_2x2(sub_mtrx3)
    )
    return det_mtrx


def det_4x4(mtrx):
    mtrx_col = [[mtrx[i][j]
                 for i in range(0, len(mtrx))] for j in range(0, len(mtrx))]

    for x in range(0, len(mtrx)):
        mtrx_col[x].pop(0)

    sub_mtrx1 = mtrx_col[:]
    sub_mtrx1.pop(0)

    sub_mtrx2 = mtrx_col[:]
    sub_mtrx2.pop(1)

    sub_mtrx3 = mtrx_col[:]
    sub_mtrx3.pop(2)

    sub_mtrx4 = mtrx_col[:]
    sub_mtrx4.pop(3)

    det_mtrx = mtrx[0][0] * det_3x3(sub_mtrx1) - mtrx[0][1] * det_3x3(
        sub_mtrx2) + mtrx[0][2] * det_3x3(sub_mtrx3) - mtrx[0][3] * det_3x3(sub_mtrx4)

    return det_mtrx


def det_5x5(mtrx):
    mtrx_col = [[mtrx[i][j]
                 for i in range(0, len(mtrx))] for j in range(0, len(mtrx))]

    for x in range(0, len(mtrx)):
        mtrx_col[x].pop(0)

    sub_mtrx1 = mtrx_col[:]
    sub_mtrx1.pop(0)

    sub_mtrx2 = mtrx_col[:]
    sub_mtrx2.pop(1)

    sub_mtrx3 = mtrx_col[:]
    sub_mtrx3.pop(2)

    sub_mtrx4 = mtrx_col[:]
    sub_mtrx4.pop(3)

    sub_mtrx5 = mtrx_col[:]
    sub_mtrx5.pop(4)

    det_mtrx = mtrx[0][0] * det_4x4(sub_mtrx1) - mtrx[0][1] * det_4x4(
        sub_mtrx2) + mtrx[0][2] * det_4x4(sub_mtrx3) - mtrx[0][3] * det_4x4(sub_mtrx4) + mtrx[0][4] * det_4x4(sub_mtrx5)

    return det_mtrx


def inv_mtrx():
    while True:
        mtrx1_dim()
        dettt = det_cond2(mtrx1)
        if dettt == 0:
            print("This matrix doesn't have an inverse.")
            break
        det_inv = 1 / dettt
        cofmtrx_t = t_main(m_cofactors(mtrx1))
        det_inv = 1 / det_cond2(mtrx1)
        res_mtrx = [
            [cofmtrx_t[i][j] * det_inv for j in range(0, len(cofmtrx_t[0]))]
            for i in range(0, len(cofmtrx_t))
        ]
        print("The result is:")
        for a in res_mtrx:
            print(*a)
        break


def m_cofactors(m):

    if len(m) == 2:
        return m[0][0] * m[1][1] - m[0][1] * m[1][0]
    else:
        n = len(m)
        rws = len(m)
        cols = len(m[0])
        ele = rws * cols
        v = 0
        minor = zeros_matrix(rws, cols)
        cof = zeros_matrix(rws, cols)

        # ESTO ES PARA HALLAR LA LISTA DE LOS MINORS
        while True:
            for u in range(0, n):
                for x in range(0, n):
                    submtrx = copy.deepcopy(m)
                    for y in range(0, len(submtrx)):
                        submtrx[y].pop(x)
                    if len(submtrx[-1]) == n - 1:
                        submtrx.pop(u)
                    minor[u][x] = submtrx
                    v += 1
            if v <= ele:
                # print(minor)
                break

        # darle signo al cofactor
        for r in range(0, n):
            for c in range(0, n):
                cof[r][c] = (-1)**(r + c)

        # Matrix de cofactores
        m_cof = [[cof[a][b] * det_cond2(minor[a][b])
                  for b in range(0, n)] for a in range(0, n)]

        return m_cof


mtrx1 = []
mtrx2 = []
result = []
res_mtrx = []
m_cof = []
minor = []
cof = []

while True:
    action = str(
        input(
            """1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate a determinant
6. Inverse matrix
0. Exit
Your choice:"""
        )
    )
    if action.isdigit():
        action = int(action)
        if action == 0:
            break
        elif action == 1:
            add_cond()
        elif action == 2:
            esc_mtrx()
        elif action == 3:
            mult_cond()
        elif action == 4:
            transpose()
        elif action == 5:
            mtrx1_dim()
            det_cond(mtrx1)
        elif action == 6:
            inv_mtrx()
            clean_mtrx()
        else:
            print("The operation cannot be performed.")
    else:
        print("The operation cannot be performed.")
