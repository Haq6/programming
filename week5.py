def Seq(arr):
    check = 0
    leng = 0
    seq=[]
    for i in range(len(arr)-1):
        check+=1
        
        leng+=1
        
        if(arr[i]>arr[i+1]):
            if(leng>len(seq)):
                seq=[]
                for ele in range(check-leng,check):
                    seq.append(arr[ele])
                
            leng=0

    if(leng+1>len(seq)):
        seq = arr[ check-leng :  ]

    
    return seq

print(Seq([2,5,9,12,2,9,18,64,128,69,2,4,9]))



