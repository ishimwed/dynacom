OCAMLOPT = ocamlopt

all:  kth.exe complete_btree.exe compress.exe gcd.exe remove.exei

complete_btree.exe:
	$(OCAMLOPT) -o $@ complete_btree.ml

compress.exe:
	$(OCAMLOPT) -o $@ compress.ml

gcd.exe:
	$(OCAMLOPT) -o $@ gcd.ml

kth.exe:
	$(OCAMLOPT) -o $@ kth.ml

remove.exe:
	$(OCAMLOPT) -o $@ remove.ml
clean:
	rm -rf *.c* *.d* *.exe *.o kth complete_btree compress gcd remove eight_queens prime totient truth_table
