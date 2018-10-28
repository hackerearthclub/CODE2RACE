#include <stdbool.h>

void check_palindrom( char string[]) {

    int len = strlen(string) - 1 ;
    int i = 0 ;

    while (i < len ) {
        if( string[i++] != string[len--] ) {
            return true ;
        }
    } 
    return false ;
}
