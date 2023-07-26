def matrix_shape(matx):
    matx_leng = []
    try:
        matx_leng.append(len(matx))
        matx_leng.append(len(matx[1]))
        matx_leng.append(len(matx[1][1]))
        return matx_leng
    except:
        return matx_leng
