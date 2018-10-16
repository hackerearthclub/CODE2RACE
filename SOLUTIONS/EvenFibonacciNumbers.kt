import java.util.*

fun main(args: Array<String>) {
    val s = Scanner(System.`in`)
    var cases = s.nextLine().toInt()
    while (cases > 0) {
        val max = s.nextLine().toInt()
        if (max < 2) {
            println("0")
        } else {
            var fib1 = 1
            var fib2 = 2
            var sum = 2
            while (true) {
                val temp = fib2
                fib2 = 2 * fib1 + 3 * fib2
                fib1 = fib1 + 2 * temp
                if (fib2 >= max) {
                    break
                }
                sum += fib2
            }
            println(sum)
        }
        --cases
    }
}