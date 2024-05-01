import numpy as np

a =[1,2,3] # python list
a = np.array(a)# numpy array
a + 2 # can use four function operator
np.cos(a) # cos
np.sin(a) # sin
a * 2 # is multiply
a ** 2 # is power
b = np.arange(0,10,2)#start from zero to ten with step two
b.size # number of element in an array 
b.itemsize #element size in an array

np.all(b)#return flase  whether at least one element of an array is zero
np.any(b)#return true  whether any element of an array is non-zero  # retrun false when one element of an array is zero

array = np.zeros((3,2)) #if u want one then it'll be np.ones((3,2)) 

#but if u want other number
array_1 = np.full((3,2),99) # np.full((row,column),number)

array_2 = np.random.rand(3,2)# random decimal number
array_3 = np.random.randint(0,10,size=(3,2))# random int number from 0 to 9 with size 3,2
np.random.normal(3,2)# ggenerate number from 3 to 2
np.random.normal(3,2,5) # np.random.normal(loc,scale,size-->can be 2D array)


b.ndim # get dimension #only work with numpy
b.shape # get shape

c = np.identity(3) # one on the main diagonal 

#statistics

#axis 0 is row , axis 1 is column

stats = np.array([[1,2,3],[4,5,6]])
np.min(stats) # min value in matrix
np.max(stats, axis= 1) # max value of every row in matrix  
np.sum(stats) # sum of matrix
np.sum(stats,axis=0)
np.isnat(np.array(["NaT", "2016-01-01"], dtype="datetime64[ns]"))# check not a time value
print(np.isnan([np.log(-1.), 1., np.log(0)]))  # Check if the elements are NaN


#Reorganizing Array
before = np.array([[1,2,3],[4,5,6]])
after = before.reshape((2,3)) # change row and column 

# u need to be same elements number in v1 and v2 to stack
v1 = np.array([2,3,4])
v2 = np.array([4,5,6])
np.vstack([v1,v2,v2]) #vertically stacking array
np.hstack([v1,v2,v2]) # hoorizontal stack

np.multiply(v1,v2)# multipy two array --> can multiply martix
np.corrcoef(v1, v2) # pearson product-moment correlation


#Micellaneous

#load data from file
filedata=np.genfromtxt("test1.txt",delimiter=",") # delimiter is a seperator
filedata = filedata.astype("int") # output as int
#we can also check true or false
filedata>50 # it'll only show true that greater than 50

#Importing simple.csv is accomplished using numpy.loadtxt:
np.loadtxt('simple.csv',delimiter=',',skiprows=1) # <--its gonna cuz I dont have csv file          