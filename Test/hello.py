
def matrix_multi():
        
    a_row=2
    a_col=3
    b_row=3
    b_col=4
    
    a=[[1 for row in range(a_col)] for rows in range(a_row)]
    b=[[2 for row in range(b_col)] for rows in range(b_row)]
    
    a[0][0]=0
    b[0][1]=1
    for i in range(a_row):
        for j in range(a_col):
            print "%d %d val: %d" % (i,j,a[i][j])
    # 2x3, 3x2 =2 x2
    
    c_row=a_row
    c_col=b_col
    fixed=a_col
    c=[[0 for row in range(c_col)] for rows in range(c_row)]       
    
    for i in range(c_row):
        for j in range(c_col): 
            for r in range(fixed):
                c[i][j] += (a[i][r]*b[r][j])
                
    for row in c:
        print row
        
def fff():
    
    a=[1,2,3]
    b=[1,3,5]
    c=set()
    
    for i in range(len(a)):
        x=a[i]
        for j in range(len(b)):
            y=b[j]
            if x!=y: 
                tmp=list()
                tmp.append(x)
                tmp.append(y)
                t=frozenset(tmp)
                c.add(t)
            
    print(c)

def ggg():
    
    a=[{1,3},{1,5}]
    b=[{2,3},{2,5}]
    c=list()
    
    for i in range(len(a)):
        x=a[i]
        for j in range(len(b)):
            y=b[j]
            if x!=y: 
                tmp=set()
                tmp=tmp.union(x)
                tmp=tmp.union(y)
                c.append(tmp)
            
    print(c)


if __name__=="__main__":
    
    num=5
    
    matrix_multi()
   # b=[[0 for i in range(5)] for j in range(5)]
    
   # for row in b:
  #      print row
        
   # c=[2,3,4,5,6,7]
   # for i in range(len(c)):
    #    print "%d  %d" % (i, c[i])
    
   # print 1/2.0
   # print "Hello, Python!" 