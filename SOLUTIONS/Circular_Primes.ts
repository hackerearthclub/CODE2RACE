function isPrime(number: number) {
    var prime = number != 1;
    for(var i = 2; i <= Math.sqrt(number); i++) {
        if(number % i == 0) {
            prime = false;
            break;
        }
    }
    return prime;
}

function isCircularPrime(permutations: Array<string>) {
    return permutations.reduce(
        function(accumulator, currentValue, currentIndex, array){
            return accumulator && isPrime(parseInt(currentValue));
        },
        true
    );
}


function permuteString(string: string) {
    function recur(string, prefix) {
        if (string.length === 0) {
            return [prefix];
        } else {
            var out = [];
            for (var i = 0; i < string.length; i++) {
                var pre = string.substring(0, i);
                var post = string.substring(i + 1);
                out = out.concat(recur(pre + post, string[i] + prefix));
            }
            return out;
        }
    }
    var distinct = {};
    recur(string, "").forEach(function(result) {
        distinct[result] = true;
    });
    return Object.keys(distinct);
}

// Main
if (process.argv.length == 3 && !isNaN(process.argv[2])) {
    var sum = 0;
    for (i = 1; i < parseInt(process.argv[2]); i++) {
        if (isCircularPrime(permuteString(i.toString()))) {
            sum += i;
        }
    }
    console.log(sum);
} else {
    console.log("Usage: node Circular_Primes.js N");
    process.exit();
}
