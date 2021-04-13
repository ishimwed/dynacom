#include "kshlib.h"
typedef  unsigned char uchar;

void int_to_uchar(int* r, uchar* in, int size)
{
  RecTrace _t(size);
  int i,
    max_r=r[0],
    min_r=r[0];

  for (i=0; i<size; i++)
    {
      OpCnt();
      if ( r[i] > max_r )
        max_r=r[i];
      if ( r[i] < min_r )
        min_r=r[i];
    }

  /*printf("min=%d max=%d\n",min_r,max_r);*/

  max_r-=min_r;

  for (i=0; i<size; i++){
    OpCnt();
    in[i] = (uchar)((int)((int)(r[i]-min_r)*255)/max_r);
  }
}

int main(int argc, char *argv[]) {
    ksh_init(argc, argv);

    int n = atoi(argv[1]);
    int * a;
    FOR(i, 1, n)
    a[i] = rnd.next(0, int(1e6));
    uchar  *in;
    int_to_uchar(a, in, n);
}
