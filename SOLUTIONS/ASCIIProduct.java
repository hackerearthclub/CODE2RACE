public static void main(String[] args) {
    String str = "YA";
    int result = 1;

    for (int x = 0; x < str.length(); x++) {
        result = result * (int) str.charAt(x);
    }

    System.out.println(result);
}