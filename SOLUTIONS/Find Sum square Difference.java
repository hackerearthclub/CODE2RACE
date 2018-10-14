iimport java.util.stream.IntStream;

class Solution {

    public static void main(String[] args) throws IOException {
        BufferedReader reader=new BufferedReader(new InputStreamReader(System.in));
        int T=Integer.parseInt(reader.readLine());
        while(T-->0){
            int i=Integer.parseInt(reader.readLine());
            System.out.println(
                    Math.abs(IntStream.rangeClosed(1,i)
                            .map(p->(int)Math.pow(p, 2)).sum()
                            -(int)Math.pow(IntStream.rangeClosed(1,i).sum(),2)));
            
        }
    }
}

