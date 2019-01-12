function beginnerProblem(arrNumber) {
    try {
        if(arrNumber.length  == 1) {
            return arrNumber[0]
        } else {
            let sort = arrNumber.sort();
            let count = 0;
            let arrObj = []
            let now = 0;
                for(let i = 0 ;i<arrNumber.length;i++) {
                    if(arrNumber[i] == arrNumber[i+1]) {
                        now  = arrNumber[i]
                        count++
                    } else {
                        arrObj.push({
                            num: now,
                            count: count
                        })
                        now = 0;
                        count = 0;
                    }
                }
                let current = arrObj[0].num;
                let currentCounter = arrObj[0].count;
                for(num of arrObj) {
                    if(num.count > currentCounter) {
                        current = num.num
                        currentCounter = num.count
                    }
                }
                return current;
        }
    } catch(err) {
        return 'MUST BE AN ARRAY OF NUMBER'
    }
}

let arr1 = [2]
let arr2 = [1,2,3]
let arr3 = [1,1,2]
let arr4 = [9,2,2,3,1,3,9,3,2,3,1,3]
console.log(beginnerProblem(arr4))