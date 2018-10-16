#include <algorithm>
#include <cstring>
#include <ctime>
#include <iostream>
#include <unordered_map>
#include <vector>
#define THRESHOLD 1000000

bool is_prime_arr[THRESHOLD];

// Sieve of eratosthenes prime check
// Filling the is_prime_arr with true if index is prime
void init_sieve_of_eratosthenes() {
  memset(is_prime_arr, true, sizeof is_prime_arr);

  for (int p = 2; p * p < THRESHOLD; p++) {
    // If prime[p] is not changed, then it is a prime
    if (is_prime_arr[p] == true) {
      // Update all multiples of p
      for (int i = p * 2; i < THRESHOLD; i += p)
        is_prime_arr[i] = false;
    }
  }
}

// Simple prime check
// Runtime: O(n^0.5)
bool is_prime_naive(int x) {
  if (x == 0 || x == 1)
    return false;
  for (int i = 2; i * i <= x; ++i) {
    if (x % i == 0)
      return false;
  }
  return true;
}

// Using sieve of eratosthenes if x < THRESHOLD
// Else use naive
bool is_prime(int x) {
  if (x >= THRESHOLD)
    return is_prime_naive(x);
  return is_prime_arr[x];
}

// Simplifying the problem by transforming primes to 1, and non-primes to -1.
// Now the problem is finding the longest contiguous sub-array with possitive
// sum.
// Runtime: O(n)
int solve(const std::vector<int> &data) {

  // Final result.
  int ans = 0;
  // Holds the sum of elements [0 .. i]
  int prefix_sum = 0;
  // This map stores all the (prefix sums, index) till the current index.
  std::unordered_map<int, int> prev_pref_sum;

  for (size_t i = 0; i < data.size(); ++i) {
    // Simplifying the problem to 1, -1.
    prefix_sum += is_prime(data[i]) ? 1 : -1;

    // if true, this is the longest subarray so far.
    if (prefix_sum > 0)
      ans = i + 1;
    else if (prev_pref_sum.find(prefix_sum - 1) != prev_pref_sum.end()) {
      ans = std::max(ans, (int)i - prev_pref_sum[prefix_sum - 1]);
    }

    // Store the current sum if not already there.
    if (prev_pref_sum.find(prefix_sum) == prev_pref_sum.end())
      prev_pref_sum[prefix_sum] = i;
  }

  return ans;
}

// Generate a random data vector of fixed size
// with a 33.33% chance of primes.
std::vector<int> gen_rand_data(int arr_size) {
  std::vector<int> rand_data(arr_size);
  std::generate(rand_data.begin(), rand_data.end(),
                []() { return rand() % 3 + 7; });
  return std::forward<std::vector<int>>(rand_data);
}

// Used for comparing the result of the suggested sol
// Runtime: O(n^2)
int solve_naive(const std::vector<int> &data) {
  int ans = 0;

  for (size_t i = 0; i < data.size(); ++i) {
    int primes_cnt = 0;
    for (size_t j = i; j < data.size(); ++j) {
      primes_cnt += is_prime(data[j]);
      if (j - i + 1 < primes_cnt * 2)
        ans = std::max(ans, (int)(j - i + 1));
    }
  }
  return ans;
}

// Test the validity using random generated data.
void test_random_data(int cnt, int arr_size) {
  std::cout << "Testing on random data of size: " << arr_size << "\n";
  size_t failed_cnt = 0;
  for (int i = 0; i < cnt; ++i) {
    auto rand_data = gen_rand_data(arr_size);
    auto naive_sol = solve_naive(rand_data);
    auto sol = solve(rand_data);
    if (sol != naive_sol) {
      ++failed_cnt;
      std::cout << "Mismatch, naive_sol: " << naive_sol << ", your_sol: " << sol
                << "\n";
    }
  }
  std::cout << "Testing finished, failed " << failed_cnt << "/" << cnt << ".\n";
}

// Test the efficiency of the solution.
void benchmark_random_data(int cnt, int arr_size) {
  std::cout << "Benchmarking on random data of size: " << arr_size << "\n";
  std::cout << "Running your solution " << cnt
            << " number of times against random data.\n";
  const clock_t begin_time = clock();
  for (int i = 0; i < cnt; ++i) {
    gen_rand_data(arr_size);
  }
  float time_elapsed = float(clock() - begin_time) / CLOCKS_PER_SEC;
  std::cout << "Benchmarking finished, time elapsed: " << time_elapsed
            << " seconds.\n";
  std::cout << "Average time per execution: " << time_elapsed / cnt << "\n";
}

// Test using stdin.
void test_user_inp() {
  int n;
  std::cin >> n;

  std::vector<int> v(n);
  for (size_t i = 0; i < n; ++i) {
    std::cin >> v[i];
  }

  std::cout << solve(v) << '\n';
}

int main() {
  init_sieve_of_eratosthenes();

  test_random_data(1000, 500);
  benchmark_random_data(10, 5000000);
}
