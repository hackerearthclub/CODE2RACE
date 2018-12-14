import java.util.Scanner;

class Best_Numbers{
	public static void main(String ... a){
		Scanner sc = new Scanner(System.in);
		
		//number of test cases
		System.out.print("Number of Test cases: ");
		int x = sc.nextInt();
		
		//number of elements
		for(int i=0; i<x; i++){
			System.out.print("number of elements: ");
			int y = sc.nextInt();
			
			//create a array object with the size of number of element
			int arr[] = new int[y];
			int sum =0;
			
			//element put into an array
			for(int j=0; j<y; j++){
				arr[j] = sc.nextInt();
			}
			
			//find the best numbers
			System.out.print("Best numbers are: ");
			for(int k:arr){
				if(k%2 == 0){
					System.out.print(k+" ");
					sum++;
				}
			}
			System.out.println("\nfrequency: "+sum);
			if(sum == 0)
				System.out.println("No best Numbers"); //print something else
		}
		
		
	}
}
