# ------------------------------------------------------------------------------------------------
# AUTh - Faculty of Engineering
# School of Electrical and Computer Engineering
#
# Discrete Mathematics
#
# May, 2022
#
# student: Kapetanios Antonios (10417)
# email: kapetaat@ece.auth.gr
# ------------------------------------------------------------------------------------------------



# ------------------------------------------------------------------------------------------------
# Theorem (Erdős–Gallai)
# ======================
# A sequence of non-negative integers d1≥...≥dn can be represented as the degree sequence of a finite simple graph on n vertices if and only if:
# 1) d1+...+dn is even, and
# 2) (the sum of d_i for i in [1,k]) ≤ (k*(k-1) + the sum of min(d_i,k) for i in[k+1,n]) is true for every k in 1≤k≤n.
#
# Source: Choudum, S. A. (1986), "A simple proof of the Erdős–Gallai theorem on graph sequences", Bulletin of the Australian Mathematical Society



# ------------------------------------------------------------------------------------------------
# Algorithm to check if a given sequence is graphic or not
# using the Erdős–Gallai theorem:

# checks if a list of integers contains negative numbers
def contains_neg(lst):
    for i in range(len(lst)):
        if lst[i]<0:
            return True

# checks if the 2nd condition of the Erdős–Gallai theorem is satisfied.
# If the inequality does not hold, it returns False, otherwise it returns True.
def Er_Ga_inequality(k,n,lst):
    left_sum=0
    for i in range(0,k+1,1):
        left_sum=left_sum+lst[i]

    right_sigma=0
    #lists are zero-indexed. Thus in the mathematical expressions k must be replaced by k+1.
    for j in range(k+1,n,1):
        minimum=min(k+1,lst[j])
        right_sigma=right_sigma+minimum

    right_sum=right_sigma+(k+1)*((k+1)-1)
    if left_sum<=right_sum:
        return True

# get sequence from keyboard
print("Enter a sequence of non-negative integers. "
      "Separate each element with spaces "
      "and hit \"Enter\" when finished.")
og_seq=list(map(int, input().split()))
print("Your sequence is: ",og_seq,".",sep='')

# if the sequence is empty, quit the program
if len(og_seq)==0:
    print("The sequence has no elements.")
    quit()

# check if the sum of the elements of the given sequence is even (1st condition of the Erdős–Gallai theorem)
# If the sum is odd, quit the program.
sum=0
for i in range(len(og_seq)):
    sum=sum+og_seq[i]
if sum%2!=0 or contains_neg(og_seq)==True:
    print("The given sequence contains negative numbers or the sum "
    "of its elements is not even and therefore it is not graphic.")
    quit()

# sort the sequence id descending order
seq=list(og_seq)
seq.sort(reverse=True)
print("Your sequence sorted in descending order is: ",seq,".",sep='')

# check if the enequality holds for all k in [1,n]. If not, quit the program.
# (2nd condition of the Erdős–Gallai theorem)
k=0
while k<len(seq):
    if(Er_Ga_inequality(k,len(seq),seq))==True:
        k=k+1
    else:
        print("The enequality of the Erdős–Gallai theorem does not hold for k=",k+1,
              ". Thus, the sequence",seq,"is not graphic.")
        quit()
# ------------------------------------------------------------------------------------------------



# ------------------------------------------------------------------------------------------------
# The sequence is graphic (in any other case the program would have been terminated)

# Algorithm to find the neighborhood of each vertex
# using the reverse process of the Havel-Hakimi algorithm:

# class that implements the vertices of the graph
class vertex:
    vertice_id=-1 
    v_degree=0

    # class constructor
    def __init__(self,vertice_id,v_degree):
        self.vertice_id=vertice_id
        self.v_degree=v_degree
        self.neighbors=list()

    def getID(self):
        return self.vertice_id

    def getDEGREE(self):
        return self.v_degree
    
    # creates an edge between two vertices
    def makeEdge(self,B):
        self.neighbors.append(B.vertice_id)
        B.neighbors.append(self.vertice_id)
# --- end of class ---

vertices_num=len(seq)

# a dictionary to save the occurring sequences after each iteration of Havel-Hakimi algorithm
seq_dic={0:seq}

# use of the Havel-Hakimi algorithm
for i_cnt in range(vertices_num):
    if(seq[0]==0):
        break
    lst=list(seq_dic[i_cnt])
    k=lst[0]
    del lst[0]
    for j in range(0,k,1):
        lst[j]=lst[j]-1
    lst.sort(reverse=True)
    seq_dic[i_cnt+1]=lst
    if(lst[0]==0):
        break
# --- end of the Havel-Hakimi algorithm ---

num_of_iterations=len(seq_dic)

# a list to hold objects of the class "vertex"
vertices=[]

# add to vertices[] the sequence (0,...,0)
for j_cnt in range(len(seq_dic[num_of_iterations-1])):
    vertices.append(vertex(j_cnt,seq_dic[num_of_iterations-1][j_cnt]))

# following the Havel-Hakimi algorithm in reverse order we construct the neighborhoods of the vertices:
for k_cnt in range(num_of_iterations-2,-1,-1):
    lst=seq_dic[k_cnt]
    prev=seq_dic[k_cnt+1]

    # add new vertice. The list vertices[] will be sorted in ascending order
    # in regards to the degree of the vertices.
    new_id=len(lst)-1
    new_v=vertex(new_id,lst[0])
    vertices.append(new_v)

    # update the degree of each vertex
    z=0
    for x in range(len(lst)-1,0,-1):
        vertices[z].v_degree=lst[x]
        z+=1

    # if the number of edges of a vertex is less than its degree then
    # an edge is created between the given vertex and the one with the
    # greatest degree (=the last element of vertices[])
    for y in range(0,len(vertices)-1,1):
        remaining_edges=vertices[y].getDEGREE()>len(vertices[y].neighbors)
        is_connected=not(vertices[len(lst)-1].getID() in vertices[y].neighbors)
        if(remaining_edges==True and is_connected==True):
            vertices[y].makeEdge(vertices[len(lst)-1])
# ------------------------------------------------------------------------------------------------



# ------------------------------------------------------------------------------------------------
# print the neighborhood of each vertex
print("The sequence S:",seq," is graphic. The neighborhoods of the simple graph G, with a degree sequence S, are:",sep='')
for cnt in range(len(vertices)):
    print("v",vertices[cnt].getID(),":{",sep='',end='')
    if(len(vertices[cnt].neighbors)!=0):
        for d in range(0,len(vertices[cnt].neighbors)-1,1):
            print("v",vertices[cnt].neighbors[d],sep='',end=", ")
        print("v",vertices[cnt].neighbors[len(vertices[cnt].neighbors)-1],"}",sep='')
    else:
        print("}",sep='')