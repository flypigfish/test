from __builtin__ import int
from copy import deepcopy

class matrix:
    
    init_matrix = [[]]
    init_vector = [[]]
    num_nodes=0
    input_data=""
    num_iteration=2
    
    def __init__(self, input_path):
        self.input_data=input_path
        print self.input_data
    
    def get_init_matrix(self):
        
        try:
            f = open(self.input_data,"r")
        except IOError:
            print "Fail to open input file"
            exit(-1)
    
        # allocate initial matrix
        self.num_nodes = (int)(f.readline())
        out_prob = 1/float(self.num_nodes)
  
        self.init_matrix = [[1 for row in range(self.num_nodes)] for rows in range(self.num_nodes)]
        self.init_vector = [[out_prob for row in range(1)] for rows in range(self.num_nodes)]
        
   
    def page_rank(self):
        pass
    
    def do_page_rank(self):
        self.get_init_matrix()
        self.page_rank()
       # self.print_rank()
        self.matrix_multiplication()
        
    def print_rank(self):

        print "Vector"
        for row in self.init_vector:
            print row[0]
    
    def matrix_multi_once(self, mat_a,mat_b, mat_a_row, mat_a_col, mat_b_row, mat_b_col):
        
        c=[[0 for row in range(mat_b_col)] for rows in range(mat_a_row)]
        
        for i in range(mat_a_row):
            for j in range(mat_b_col):
                for r in range(mat_a_col):
                    c[i][j] += (mat_a[i][r]*mat_b[r][j])
                    
        return c

    def matrix_multiplication(self):
        
        result=deepcopy(self.init_matrix)
        for i in range(self.num_iteration):
            result = self.matrix_multi_once(mat_a=result, mat_b=result, mat_a_row=self.num_nodes,
                                            mat_a_col=self.num_nodes,mat_b_row=self.num_nodes,mat_b_col=self.num_nodes)
    
        print result        
        return result
    
    
    
if __name__ == "__main__":
    
    prank=matrix("tiny.txt")
    prank.do_page_rank()
    
   
   
