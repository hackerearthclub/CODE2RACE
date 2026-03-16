import java.util.*;

public class WaitForIt {

    static final long MOD = 1000000007;

    static long modPow(long base, long exp) {
        long result = 1;
        base %= MOD;

        while (exp > 0) {
            if ((exp & 1) == 1)
                result = (result * base) % MOD;

            base = (base * base) % MOD;
            exp >>= 1;
        }

        return result;
    }

    static long gcd(long a, long b) {
        while (b != 0) {
            long t = a % b;
            a = b;
            b = t;
        }
        return a;
    }

    static long solve(long A, long B, long N) {

        long ans = 0;

        for (long i = 1; i <= N; i++) {
            for (long j = 1; j <= N; j++) {

                long g = gcd(i, j);

                long term = (modPow(A, g) - modPow(B, g)) % MOD;
                if (term < 0) term += MOD;

                ans = (ans + term) % MOD;
            }
        }

        return ans;
    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int T = sc.nextInt();

        while (T-- > 0) {

            long A = sc.nextLong();
            long B = sc.nextLong();
            long N = sc.nextLong();

            System.out.println(solve(A, B, N));
        }

        sc.close();
    }
}