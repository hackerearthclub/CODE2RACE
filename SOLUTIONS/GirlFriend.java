import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.Scanner;

public class GirlFriend 
{	
	private HashMap<Integer, Node> nodeLookup = new HashMap<Integer, Node>();
	
	public static class Response {
		int distance;
		boolean exists;
		Response(int d, boolean e)
		{
			this.distance = d;
			this.exists = e;
		}
		
		public void setExists(boolean p)
		{
			this.exists = p;
		}
		
		public void setDistance(int d)
		{
			this.distance = d;
		}
		
		public int getDistance()
		{
			return this.distance;
		}
	}
	
	public static class Node {
		private int id;
		LinkedList<Node> children = new LinkedList<Node>();
		private Node(int nodeid)
		{
			this.id = nodeid;
		}
	}
	
	private Node getNode(int id)
	{
		return nodeLookup.get(id);
	}
	
	public void addEdge(int source, int destination)
	{
		Node s = getNode(source);
		Node d = getNode(destination);
		s.children.add(d);
	}
	
	public Response hasPathDFS(int source, int destination)
	{
		Node s = getNode(source);
		Node d = getNode(destination);
		HashSet<Integer> visited = new HashSet<Integer>();
		
		return hasPathDFS(s, d, visited, new Response(0, false));
	}
	
	public Response hasPathDFS(Node source, Node destination, HashSet<Integer> visited, Response r)
	{
		
		// if the node is already visited, it means that no path exists from source to destination
		if(visited.contains(source.id))
		{
			r.setExists(false);
			return r;
		}
		
		// add node to visited set
		visited.add(source.id);
		
		// if the source node is the destination
		if(source == destination)
		{
			r.setExists(true);
			return r;
		}
		

		// check if a path exists from any child of source to destination
		for(Node child : source.children)
		{
			if(hasPathDFS(child, destination, visited, r).exists)
			{
				r.setDistance(r.getDistance() + 1);
				r.setExists(true);
				return r;
			}
		}
		
		// no path exists from any child of source to destination	
		return r;
	}
	
	public static void main(String[] args) 
	{
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		GirlFriend graph = new GirlFriend();
		int countries = sc.nextInt();

		for(int i = 0; i < countries - 1; i++)
		{
			int a = sc.nextInt();
			int b = sc.nextInt();
			
			if(!graph.nodeLookup.containsKey(a))
			{
				Node x = new Node(a);
				graph.nodeLookup.put(a, x);
			}
			if(!graph.nodeLookup.containsKey(b))
			{
				Node y = new Node(b);
				graph.nodeLookup.put(b, y);
			}
				
			graph.addEdge(a,  b);
			graph.addEdge(b,  a);
		}

		int girls = sc.nextInt();
		int girlFriend = -1, distance = -1;
		for(int i = 0; i < girls; i++)
		{
			int girl = sc.nextInt();
			Response r = graph.hasPathDFS(1, girl);
			if(r.exists)
			{
				if(distance == -1)
				{
					girlFriend = girl;
					distance = r.distance;
				}
				else if(r.distance < distance) 
				{
					girlFriend = girl;
					distance = r.distance;
				}
				else if(r.distance == distance)
				{
					if(girl < girlFriend)
					{
						girlFriend = girl;
					}
				}
			}
		}
		System.out.println(girlFriend);
	}
}
