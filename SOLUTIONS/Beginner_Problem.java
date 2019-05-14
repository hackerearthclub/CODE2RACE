import java.util.*;

class Main{

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int test;
		int nbrOfElm;
		int frequency;
		test = in.nextInt();
		int [] output = new int[test];
		for (int i = 0;i<test ;i++ ) {
			nbrOfElm = in.nextInt();
			int [] elements = new int[nbrOfElm];
			frequency = 0;
			for (int j = 0;j<nbrOfElm ;j++ ) {
				elements[j] = in.nextInt();
				if (elements[j] % 2 == 0) {
					frequency++;
				}
			}
			output[i] = frequency;
		}
		System.out.println();
		for(int i : output)
			System.out.println(i);
	}
}