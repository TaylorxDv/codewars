#include <stddef.h>
#include <string.h>
#define VOWELS "aeiou"

size_t get_count(const char *s)
{
    int i = 0;
    while(*s != '\0')
    {
        if(strchr(VOWELS, *s) != NULL)  
          i++;
        s++;
    }
    return i;
}
