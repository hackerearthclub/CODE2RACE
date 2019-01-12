import java.util.*;
import java.io.*;
import java.math.BigInteger;

class NUMBGAME
{

    static int mod = (int) (1e9+7);
    static InputReader in;
    static PrintWriter out;
    static int[] freq;
    static int cnt;
    static boolean[] vis;
    static ArrayList<Integer>[] g;
    
    static void dfs(int u) {
        vis[u] = true;
        cnt += freq[u];
        for(int v: g[u])
            if(!vis[v])
                dfs(v);
    }
    
    static void solve() 
    {
        in = new InputReader(System.in);
        out = new PrintWriter(System.out); 
        
        int t = in.nextInt();
        
        while(t-- > 0){
            String A = in.readString();
            int n = A.length();
            int m = in.nextInt();
            
            int[] pre = new int[n + 1];
            int[] suf = new int[n + 1];

            for(int i = 0; i < n; i++) {
                int x = (int)(A.charAt(i) - '0');
                pre[i + 1] = (pre[i] * 10 + x) % m;
            }
            
            freq = new int[m];
            int[] pow = new int[n + 1];
            pow[0] = 1;
            for(int i = 1; i <= n; i++)
                pow[i] = (pow[i - 1] * 10) % m;
            
            for(int i = 0; i < n; i++) {
                int x = ((pre[i] - pre[i + 1] + m)* pow[n - i - 1]) % m + pre[n];
                freq[x % m]++;
            }
            
            g = new ArrayList[m];
            
            for(int i = 0; i < m; i++)
                g[i] = new ArrayList<>();
            
            for(int i = 0; i < m; i++) {
                for(int j = 0; j < m; j++) {
                    if(freq[j] == 0) continue;
                    g[(i * pow[n - 1] + j) % m].add(i);
                }
            }
            
            vis = new boolean[m];
            cnt = 0;
            dfs(0);
            
            out.println(cnt);
        }
        
        out.close(); 
    }
    
    static long add(long a, long b) {
        return (a + b) % mod;
    }
    
    static long mul(long a, long b) {
        return (a * b) % mod;
    }
    
    static long sub(long a, long b) {
        return (a - b + mod) % mod;
    } 
    
    public static void main(String[] args)
    {
        new Thread(null ,new Runnable(){
            public void run()
            {
                try{
                    solve();
                } catch(Exception e){
                    e.printStackTrace();
                }
            }
        },"1",1<<26).start();
    }
    
    static class Pair implements Comparable<Pair>
    {

        int x,y;
        int i;
        
        Pair (int x, int y)
        {
                this.x = x;
                this.y = y;
        }

        public int compareTo(Pair o)
        {
            return -Integer.compare(this.x, o.x);
        }

        public boolean equals(Object o)
        {
            if (o instanceof Pair)
            {
                Pair p = (Pair)o;
                return p.x == x && p.y==y;
            }
            return false;
        }

        @Override
        public String toString()
        {
            return x + " "+ y + " "+i;
        }

        /*public int hashCode()
        {
            return new Long(x).hashCode() * 31 + new Long(y).hashCode();
        }*/

    } 

    
    static String rev(String s){
        StringBuilder sb=new StringBuilder(s);
        sb.reverse();
        return sb.toString();
    }
    
    static long gcd(long x,long y)
    {
        if(y==0)
                return x;
        else
                return gcd(y,x%y);
    }

    static int gcd(int x,int y)
    {
        if(y==0)
                return x;
        else 
                return gcd(y,x%y);
    }

    static long pow(long n,long p,long m)
    {
         long  result = 1;
          if(p==0){
            return 1;
          }
          
        while(p!=0)
        {
            if(p%2==1)
                result *= n;
            if(result >= m)
               result %= m;
            p >>=1;
            n*=n;
            if(n >= m)
                n%=m;
        }
        
        return result;
    }

    static long pow(long n,long p)
    {
        long  result = 1;
          if(p==0)
            return 1;

        while(p!=0)
        {
            if(p%2==1)
                result *= n;	    
            p >>=1;
            n*=n;	    
        }
        return result;
    }

    static void debug(Object... o)
    {
            System.out.println(Arrays.deepToString(o));
    }

    static class InputReader
    {

        private final InputStream stream;
        private final byte[] buf = new byte[8192];
        private int curChar, snumChars;
        private SpaceCharFilter filter;

        public InputReader(InputStream stream)
        {
                this.stream = stream;
        }

        public int snext()
        {
                if (snumChars == -1)
                        throw new InputMismatchException();
                if (curChar >= snumChars)
                {
                        curChar = 0;
                        try
                        {
                                snumChars = stream.read(buf);
                        } catch (IOException e)
                        {
                                throw new InputMismatchException();
                        }
                        if (snumChars <= 0)
                                return -1;
                }
                return buf[curChar++];
        }

        public int nextInt()
        {
                int c = snext();
                while (isSpaceChar(c))
                {
                        c = snext();
                }
                int sgn = 1;
                if (c == '-')
                {
                        sgn = -1;
                        c = snext();
                }
                int res = 0;
                do
                {
                        if (c < '0' || c > '9')
                                throw new InputMismatchException();
                        res *= 10;
                        res += c - '0';
                        c = snext();
                } while (!isSpaceChar(c));
                return res * sgn;
        }

        public long nextLong()
        {
                int c = snext();
                while (isSpaceChar(c))
                {
                        c = snext();
                }
                int sgn = 1;
                if (c == '-')
                {
                        sgn = -1;
                        c = snext();
                }
                long res = 0;
                do
                {
                        if (c < '0' || c > '9')
                                throw new InputMismatchException();
                        res *= 10;
                        res += c - '0';
                        c = snext();
                } while (!isSpaceChar(c));
                return res * sgn;
        }

        public int[] nextIntArray(int n)
        {
                int a[] = new int[n];
                for (int i = 0; i < n; i++)
                {
                        a[i] = nextInt();
                }
                return a;
        }

        public long[] nextLongArray(int n)
        {
                long a[] = new long[n];
                for (int i = 0; i < n; i++)
                {
                        a[i] = nextLong();
                }
                return a;
        }

        public String readString()
        {
                int c = snext();
                while (isSpaceChar(c))
                {
                        c = snext();
                }
                StringBuilder res = new StringBuilder();
                do
                {
                        res.appendCodePoint(c);
                        c = snext();
                } while (!isSpaceChar(c));
                return res.toString();
        }

        public String nextLine()
        {
                int c = snext();
                while (isSpaceChar(c))
                        c = snext();
                StringBuilder res = new StringBuilder();
                do
                {
                        res.appendCodePoint(c);
                        c = snext();
                } while (!isEndOfLine(c));
                return res.toString();
        }

        public boolean isSpaceChar(int c)
        {
                if (filter != null)
                        return filter.isSpaceChar(c);
                return c == ' ' || c == '\n' || c == '\r' || c == '\t' || c == -1;
        }

        private boolean isEndOfLine(int c)
        {
                return c == '\n' || c == '\r' || c == -1;
        }

        public interface SpaceCharFilter
        {
                public boolean isSpaceChar(int ch);
        }

    }
}
