#include "kshlib.h"
#include <stdio.h>
#include <string.h>

bool uInt64_isZero ( ll n )
{
    RecTrace _t(n);
   int i;
   char str[256];
   sprintf(str, "%lld", n);
   for (i = 0; i < 8; i++) {
     OpCnt();
     if (str[i] != 0) return 0;
   }

   return 1;
}

int main(int argc, char *argv[]) {
    ksh_init(argc, argv);

    ll n = atoll(argv[1]);
    uInt64_isZero(n);
}
