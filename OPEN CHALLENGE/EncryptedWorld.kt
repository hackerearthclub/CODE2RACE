object Main {

    @JvmStatic
    fun main(args: Array<String>) {
        val offset = 1337

        val helloWorld = "Hello World!"
        val encrypted = encryptString(helloWorld, offset)
        val decrypted = decryptString(encrypted, offset)

        println("Encrypted: $encrypted")
        println("Decrypted: $decrypted")
    }

    fun encryptString(string: String, offset: Int) : String{
        val length = string.length - 1
        var returnString = ""

        for(i in 0..length) {
            var char = string[i]
            char += offset
            returnString += char
        }

        return returnString
    }

    fun decryptString(string: String, offset: Int) : String{
        val length = string.length - 1
        var returnString = ""

        for(i in 0..length) {
            var char = string[i]
            char -= offset
            returnString += char
        }

        return returnString
    }
}
