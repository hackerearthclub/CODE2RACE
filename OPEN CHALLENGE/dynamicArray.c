/**
 * @file dynamicArray.c
 * @author Jay Welborn www.github.com/jaywelborn
 *
 * This is a solution to the HackerRank problem "Dynamic Array in C" located
 * at https://www.hackerrank.com/challenges/dynamic-array-in-c/problem
 *
 * This problem dynamically allocates space to store information about how
 * many pages are on each bookshelf of a library.
 *
 * Description:
 * Snow Howler is the librarian at the central library of the city of HuskyLand.
 * He must handle requests which come in the following forms:
 * 1 x y : Insert a book with  pages at the end of the  shelf.
 * 2 x y : Print the number of pages in the  book on the  shelf.
 * 3 x : Print the number of books on the  shelf.
 * Snow Howler has got an assistant, Oshie, provided by the Department of
 * Education. Although inexperienced, Oshie can handle all of the queries of
 * types 2 and 3. Help Snow Howler deal with all the queries of type 1.
 *
 * Input Format: The first line contains an integer , the number of shelves in
 * the library. The second line contains an integer , the number of requests.
 * Each of the following  lines contains a request in one of the three specified
 * formats.
 */

#include <stdio.h>
#include <stdlib.h>

/*
 * This stores the total number of books in each shelf.
 */
int* total_number_of_books;

/*
 * This stores the total number of pages in each book of each shelf.
 * The rows represent the shelves and the columns represent the books.
 */
int** total_number_of_pages;

int main()
{
    int total_number_of_shelves;
    scanf("%d", &total_number_of_shelves);

    total_number_of_books = calloc(total_number_of_shelves, sizeof(int));

    int total_number_of_queries;
    scanf("%d", &total_number_of_queries);

    total_number_of_pages = malloc(total_number_of_shelves * sizeof(int *));
    for (int i = 0; i < total_number_of_shelves; i++) {
        total_number_of_pages[i] = calloc(1100, sizeof(int));
    }

    while (total_number_of_queries--) {
        int type_of_query;
        scanf("%d", &type_of_query);

        if (type_of_query == 1) {
            /*
             * Process the query of first type here.
             */
            int shelf, pages;
            scanf("%d %d", &shelf, &pages);
            total_number_of_books[shelf]++;
            int *book = total_number_of_pages[shelf];
            while (*book != 0)
                book++;
            *book = pages;
                    } else if (type_of_query == 2) {
            int x, y;
            scanf("%d %d", &x, &y);
            printf("%d\n", *(*(total_number_of_pages + x) + y));
        } else {
            int x;
            scanf("%d", &x);
            printf("%d\n", *(total_number_of_books + x));
        }
    }

    if (total_number_of_books) {
        free(total_number_of_books);
    }

    for (int i = 0; i < total_number_of_shelves; i++) {
        if (*(total_number_of_pages + i)) {
            free(*(total_number_of_pages + i));
        }
    }

    if (total_number_of_pages) {
        free(total_number_of_pages);
    }

    return 0;
}
