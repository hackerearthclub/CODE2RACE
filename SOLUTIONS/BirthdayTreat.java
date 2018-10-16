import java.util.Arrays;

class BirthdayTreat {
    public static void main(String[] args) {
        runTest(new int[]{1, 2, 3, 4, 5}, 3);
        runTest(new int[]{5, 4, 3, 2, 1}, 3);
        runTest(new int[]{1, 3, 4, 5, 2}, 3);
    }

    public static int getNumChocolatesMoved(int[] giftPackets) {
        int sumChocolates = 0, output = 0;
        for (int packet : giftPackets) {
            sumChocolates += packet;
        }
        int averageNum = sumChocolates / giftPackets.length;
        for (int packet : giftPackets) {
            if (packet > averageNum) {
                output += (packet - averageNum);
            }
        }
        return output;
    }

    public static void runTest(int[] testCase, int expectedValue) {
        System.out.println("Test case: " + Arrays.toString(testCase) + ". Expected result: " + Integer.toString(expectedValue));
        System.out.print("Actual: ");
        int result = getNumChocolatesMoved(testCase);
        if (result == expectedValue) {
            System.out.print(Integer.toString(result) + ". PASS\n");
        }
        else {
            System.out.print(Integer.toString(result) + ". FAIL\n");
        }
    }
}
