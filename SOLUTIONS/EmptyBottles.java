import java.util.Scanner;

public class EmptyBottles
{
	public int noBottles;
	public int[] bottles;

	public EmptyBottles(int noBottles, int[] bottles)
	{
		this.noBottles = noBottles;
		this.bottles = bottles;
	}

	public int calculateTotalWater()
	{
		int total = 0;
		for (int i = 0; i<this.noBottles; i++)
		{
			total += this.bottles[i];
		}
		return total;
	}

	public static int calculateBottleNo(int total)
	{
		int answer = 0;
		int remainder = 0;
		int quotient = 0;
		quotient = total/100;
		answer += quotient;
		return answer;
	}


	public static void main(String[] args)
	{
		//Initialising Variables===================
		Scanner sc = new Scanner(System.in);
		int numberOfTests = Integer.parseInt(sc.nextLine());
		EmptyBottles[] tests = new EmptyBottles[numberOfTests];
		for (int i = 0; i < numberOfTests; i++)
		{
			int nB = Integer.parseInt(sc.nextLine());
			String[] bArray = sc.nextLine().split(" ");
			int[] bArrayInt = new int[nB];
			for (int j=0; j<nB; j++)
			{
				bArrayInt[j] = Integer.parseInt(bArray[j]);
			}

			tests[i] = new EmptyBottles(nB,bArrayInt);

		}
		sc.close();
		//Initialising Variables===================
		for (int b = 0; b < numberOfTests; b++)
		{
			System.out.println(calculateBottleNo(tests[b].calculateTotalWater()));
		}
	}
}