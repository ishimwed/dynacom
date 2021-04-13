#include "kshlib.h"

#define max_malloc_probes 20
#define malloc_probe_size 64000

long heap_available(ll x){
  RecTrace _t(x);
  long avail = 0;
	void *probes[max_malloc_probes];
	uint n;
	for ( n = 0; n < max_malloc_probes; n++ )
	  { if ( (probes[n] = malloc(malloc_probe_size)) == 0 )
	      break;
	    // if_debug2('a', "[a]heap_available probe[%d]=0x%lx\n",
		  //     n, (ulong)probes[n]);
	    avail += malloc_probe_size;
      OpCnt();
	  }
	while ( n ){
    OpCnt();
    free(probes[--n]);
  }
	return avail;
}

int main(int argc, char *argv[]) {
    ksh_init(argc, argv);

    ll n = atoll(argv[1]);
    heap_available(n);
}
