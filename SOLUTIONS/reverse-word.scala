object ReverseWord extends App {
  def reverseWord(): String = {
    print("Enter a sentence to reverse words order: ")
    val sentence = scala.io.StdIn.readLine()
    println()
    val words = sentence.split(" ")
    val reversed_words = words.reverse
    reversed_words.mkString(" ")
  }
  
  println(reverseWord())
}
