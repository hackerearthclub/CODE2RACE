import java.util.*

fun main(args: Array<String>) {
    val scanner = Scanner(System.`in`)
    val n = scanner.nextLine().toInt()

    for (i in 0 until n) {
        val number = scanner.nextLine().toInt()
        var squareSum = 0
        var sum = 0
        for (j in 1..number) {
            squareSum += j * j
            sum += j
        }
        val sumSquare = sum * sum
        val difference = squareSum - sumSquare
        println((if (difference > 0) difference else -difference).toString())
    }
    scanner.close()
}