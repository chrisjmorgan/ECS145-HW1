def tda(imgFile,nr,nc,thresholds):
    try:
        with open(imgFile) as f:
            imgstr = f.read()
    except:
        print("File open error")
    imgStr2Int = [int (i) for i in imgstr.split()]
    print(rowCount(imgStr2Int,nr,nc,thresholds))
    print(columnCount(imgStr2Int,nr,nc,thresholds))

#-------------------------------------------------

def rowCount(threshList,nr,nc,thresholds):
    rowCount = []
    tmpCount = 0        
    notif = 0
    for i in range(nc*nr):
        if threshList[i] > thresholds and notif == 0:
            notif = 1
            tmpCount = tmpCount + 1
        elif threshList[i] <= thresholds:
            notif = 0
        if ((i+1)%nc == 0):
            notif = 0
            rowCount.append(tmpCount)
            tmpCount = 0
    return(rowCount)

#-------------------------------------------------    

def columnCount(imgStr2Int,nr,nc,thresholds):
    rowCount = []
    tmpCount = 0
    notif = 0
    for i in range(nc):
        for n in range(nr):
            if imgStr2Int[i+n*nc] > thresholds and notif == 0:
                notif = 1
                tmpCount = tmpCount + 1
            elif imgStr2Int[i+n*nc] <= thresholds:
                notif = 0
            if ((n+1)%nr == 0):
                notif = 0
                rowCount.append(tmpCount)
                tmpCount = 0
    return(rowCount)

#-------------------------------------------------

def diagonalCount(imgStr2Int,nr,nc,thresholds):







tda('imgFile',3,4,10)






    
