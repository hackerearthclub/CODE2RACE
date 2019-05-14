import Foundation

/*
 This method takes an unsorted array in input & returns the third largest number form Array as input
 Time complexoty: O(n)
 */
func thirdLargetInArray(arr:[Int]) {
    var first:Int = arr[0]
    var second:Int = 0
    var third:Int = 0
    
    for i in 0..<arr.count {
        if arr[i] > first && arr[i] != first {
            third = second
            second = first
            first = arr[i]
        }
        else if arr[i] > second && arr[i] != second && arr[i] != first {
            third = second
            second = arr[i]
        }
        else if arr[i] > third && arr[i] != third && arr[i] != first && arr[i] != second {
            print(second)
            third = arr[i]
            print("Third after changing = \(third)")
        }
    }
    print("Third largest element in array is \(third)")
}

let inputArr = [4,5,3,2,15,7,6,25,13,14,17,8,9,18,17,17,25,26]
thirdLargetInArray(arr: inputArr)
