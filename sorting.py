class Sorting:
    def __init__(self,array,arr_size):
        self.array=array
        self.arr_size=arr_size
    def swap(self,list,ind1,ind2):
        self.list=list
        self.ind1=ind1
        self.ind2=ind2
        list[ind1],list[ind2]=list[ind2],list[ind1]
    def selection_sort(self):
        for i in range(self.arr_size-1):
            min=self.array[i]
            loc=i
            for j in range(i+1,self.arr_size):
                if self.array[j]<min:
                    min=self.array[j]
                    loc=j
            self.swap(self.array,i,loc)
        #return self.array
    def bubble_sort(self):
        Sorting.__init__(self)
        for i in range(self.arr_size-1):
            flag=0
            for j in range(i,self.arr_size-1):
                if self.array[j]>self.array[j+1]:
                    self.swap(self.array,j,j+1)
                    flag=1
            if flag==0:
                break
        #return self.array
    def insertion_sort(self):
        for i in range(1,self.arr_size):
            k=self.array[i]
            j=i-1
            while j>=0 and self.array[j]>k:
                self.array[j+1]=self.array[j]
                j-=1
            self.array[j+1]=k
        #return self.array
    def insertion_sort1(self):
        for i in range(1,self.arr_size):
            for j in range(0,i):
                flag=0
                if self.array[i-j]<=self.array[i-j-1]:
                    self.swap(self.array,(i-j),i-j-1)
                    flag=1
                if flag==0:
                    break
        #return self.array
    def merge(self,array,lb,mid,ub):
        self.array=array
        self.lb=lb
        self.mid=mid
        self.ub=ub
        n1=mid-lb+1
        n2=ub-mid
        L=[None]*n1
        R=[None]*n2
        for i in range(0,n1):
            L[i]=array[lb+i]
        for j in range(0,n2):
            R[j]=array[mid+1+j]
        i,j=0,0
        k=lb
        while i<n1 and j<n2:
            if L[i]<=R[j]:
                array[k]=L[i]
                i+=1
            else:
                array[k]=R[j]
                j+=1
            k+=1
        while i<n1:
            array[k]=L[i]
            i+=1
            k+=1
        while j<n2:
            array[k]=R[j]
            j+=1
            k+=1
    def merge_sort(self,array,lb,ub):
        self.array=array
        self.lb=lb
        self.ub=ub
        if lb<ub:
            mid=lb+(ub-lb)//2
            self.merge_sort(array,lb,mid)
            self.merge_sort(array,mid+1,ub)
            self.merge(array,lb,mid,ub)
    def maxHeapify(self,heap,root,heap_size):
        self.heap=heap
        self.root=root
        self.heap_size=heap_size
        l_child=root*2
        r_child=root*2+1
        if l_child<=heap_size and heap[root]<heap[l_child]:
            largest=l_child
        else:
            largest=root
        if r_child<=heap_size and heap[r_child]>heap[largest]:
            largest=r_child
        if largest!=root:
            self.swap(heap,root,largest)
            self.maxHeapify(heap,largest,heap_size)
    def build_Maxheap(self,array,heap_size):
        self.array=array
        self.heap_size=heap_size
        mid=heap_size//2
        while mid<=heap_size:
            self.maxHeapify(array,heap_size-mid,heap_size)
            mid+=1
    def heap_sort(self,array,ub):
        self.array=array
        self.ub=ub
        heap_size=ub
        self.build_Maxheap(array,ub)
        for i in range(0,ub):
            self.swap(array,0,ub-i)
            heap_size-=1
            self.maxHeapify(array,0,heap_size)
    def partition(self,array,lb,ub):
        self.array=array
        self.lb=lb
        self.ub=ub
        pivot=array[ub]
        i=lb-1
        for j in range(0,ub):
            if array[j]<=pivot:
                i+=1
                self.swap(array,i,j)
        self.swap(array,i+1,ub)
        return i+1
    def quick_sort(self,array,lb,ub):
        self.array=array
        self.lb=lb
        self.ub=ub
        if lb<ub:
            mid=self.partition(array,lb,ub)
            self.quick_sort(array,lb,mid-1)
            self.quick_sort(array,mid+1,ub) 
#main program   
array_size=int(input("Enter the size of an array:"))
in_arr=[None]*array_size
for i in range(0,array_size):
    in_arr[i]=int(input("Enter a value:"))
print("Array before sorting is:\n",in_arr)
sorted_array=Sorting(in_arr,array_size)
print("For sorting the array press 1\n To exist the program press 2")
user_in=int(input("Enter your option:"))
if user_in==1:
    print("Kindly choose by which method you want to sort-\n1.Selection Sort\n2.Bubble Sort\n3.Insertion Sort\n4.Merge Sort\n5.Heap Sort\n6.Quick Sort")
    user_ch=int(input("Enter your choice in numeric form:"))
    if user_ch==1:
        sorted_array.selection_sort()
        print("Array after Selection sort is:\n",in_arr)
    elif user_ch==2:
        sorted_array.bubble_sort()
        print("Array after bubble sort is:\n",in_arr)
    elif user_ch==3:
        sorted_array.insertion_sort()
        print("Array after insertion sort is:\n",in_arr)
    elif user_ch==4:
        sorted_array.merge_sort(in_arr,0,len(in_arr)-1)
        print("Array after merge sort is:\n",in_arr)
    elif user_ch==5:
        sorted_array.heap_sort(in_arr,len(in_arr)-1)
        print("Array after heap sort is:\n",in_arr)
    elif user_ch==6:
        sorted_array.quick_sort(in_arr,0,len(in_arr)-1)
        print("Array after quick sort is:\n",in_arr)
    else:
        print("You entered wrong choice.\nTHANK YOU!")
else:
    print("Thank you")