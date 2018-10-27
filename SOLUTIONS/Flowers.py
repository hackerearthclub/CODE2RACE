from sys import stdin, stdout

MAX = 100005
MOD = pow(10, 9) + 7

t, k = map(int, raw_input().strip().split())
inp = stdin.readlines()
out = []

dp = [1 for i in xrange(MAX)]

for i in xrange(k, MAX): dp[i] = (dp[i - 1] + dp[i - k]) % MOD

pre = [0 for i in xrange(MAX + 1)]
for i in xrange(1, MAX + 1): pre[i] = (pre[i - 1] + dp[i - 1]) % MOD

for line in inp:
    a, b = map(int, line.strip().split())
    ans = (pre[b + 1] - pre[a]) % MOD
    out.append(str(ans))

stdout.write("\n".join(out))