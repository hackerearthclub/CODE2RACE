object SumOfFactorialDigits extends App {
  def readT(): Int = {
    val inp = scala.io.StdIn.readLine()
    try {
      inp.trim.toInt
    } catch {
      case _: Exception => throw new RuntimeException("Error occurred while reading number of test cases: please enter a valid value")
    }
  }

  def readCases(t: Int, list: List[Int] = List.empty[Int]): List[Int] = {
    if (t == list.length) {
      return list
    }

    val inp = scala.io.StdIn.readLine()
    try {
      val value2insert = inp.trim.toInt
      if (value2insert < 0 && value2insert > 1000) {
        throw new RuntimeException("0≤ N ≤ 1000")
      }

      readCases(t, list :+ value2insert)
    } catch {
      case _: Exception => throw new RuntimeException("Error occurred while reading cases: please enter a valid value and/or number that is greater than 0")
    }
  }

  def factorial(n: Int): Int = {
    if (-1 < n && n <= 1) 1
    else n * factorial(n - 1)
  }

  def calculateDigitsSum(n: Int): Int = {
    val digits: String = n.toString
    digits.split("").map(_.toInt).sum
  }

  def sumFactorialDigits: List[Int] = {
    val t = readT()

    val numbers: List[Int] = if (t < 1 && t > 100) {
      throw new RuntimeException("1≤ T ≤ 100")
    } else {
      readCases(t)
    }

    numbers.map(factorial).map(calculateDigitsSum)
  }

  sumFactorialDigits.foreach(println)
}
