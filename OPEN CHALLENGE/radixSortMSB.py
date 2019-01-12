from __future__ import print_function

def radixsort_msd(array,place):
    if(len(array)<1):
        return []
    if(len(array)==1):
        return [array[0]]
    bucket_list = []
    for i in range(0,10):
        bucket_list.append([])
    for x in array:
        msd = int((x/(10**place))%10)
        bucket_list[msd].append(x)

    for y in range(0,len(array)):
        #print y
        bucket_list[y] = radixsort_msd(bucket_list[y],place-1)

    new_list = []
    for sublist in bucket_list:
        if(len(sublist)>0):
            for item in sublist:
                new_list.append(item)
    return new_list

if __name__ == "__main__":


    a = [329,105,115,190,364,305,207]
    final_list = radixsort_msd(a,3)
    print(final_list)
