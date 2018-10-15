import org.codehaus.groovy.runtime.InvokerHelper
import java.io.BufferedReader
import java.io.InputStreamReader

class ReverseWord extends Script {
  def run() {
    println  "Input:"

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in))

    br.withCloseable {
      String str = br.readLine()

      println(str.split('\\s').reverse().join(' '))
    }
  }
  static void main(String[] args) {
    InvokerHelper.runScript(ReverseWord, args)
  }
}
