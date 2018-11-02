#include <stdio.h>
#include <stdlib.h>

int main(int argc, char const *argv[]) {
	int number_of_cases = 0, number_of_elements = 0, values = 0;

	scanf("%i", &number_of_cases);

	int vet_result_cases[number_of_cases];

	for (int i = 0; i < number_of_cases; ++i) {
		vet_result_cases[i] = 0;
	}

	for (int i = 0; i < number_of_cases; ++i) {
		scanf("%i", &number_of_elements);
		for (int j = 0; j < number_of_elements; ++j) {
			scanf("%i", &values);
			if (values % 2 == 0) {
				vet_result_cases[i] += 1;
			}
		}
	}

	for (int i = 0; i < number_of_cases; ++i) {
		printf("%i\n", vet_result_cases[i]);
	}

	return 0;
}