import java.util.*;
import java.io.*;
import java.lang.StringBuilder;

public class VideoPosts
{
	public static void main(String[] args)
	{
		Scanner in = new Scanner(new BufferedReader(new InputStreamReader(System.in)));

		int numVideos = in.nextInt();
		int numPosts = in.nextInt();

		int totalSeconds = 0;
		List<Integer> list = new ArrayList<>();

		for(int i = 0; i < numVideos; i++)
		{
			int videoLength = in.nextInt();
			totalSeconds += videoLength;
			list.add(videoLength);		
		}		

		if(totalSeconds % numPosts != 0)
		{
			System.out.println("No");
		}
		else
		{
			boolean solutionExists = true;
			int i = 0;
			StringBuilder builder = new StringBuilder();
			int durationPerPost = totalSeconds / numPosts;
			int numVideoPerPost = 0;
			while(solutionExists && i < list.size())
			{
				durationPerPost -= list.get(i);
				numVideoPerPost++;

				if(durationPerPost == 0)
				{
					builder.append(numVideoPerPost).append(" ");
					durationPerPost = totalSeconds / numPosts;
					numVideoPerPost = 0;
				}

				if(durationPerPost < 0)
				{
					solutionExists = false;
				}					
				i++;
			}

			if(solutionExists)
			{
				builder.insert(0, "Yes ");
				String output = builder.toString();
				System.out.println(output.substring(0, output.length()-1));
			}
			else
			{
				System.out.println("No");
			}
		}
	}
}
