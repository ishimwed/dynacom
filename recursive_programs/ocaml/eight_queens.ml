let counter = ref 0;;

let possible row col used_rows usedD1 usedD2 =
  not (List.mem row used_rows
       || List.mem (row + col) usedD1
       || List.mem (row - col) usedD2)

let queens_positions n file depth=
  let rec aux row col used_rows usedD1 usedD2 file depth=
    Printf.fprintf file "%d;%d\n" depth row;
    if depth=0 then counter := !counter + 1 else counter := !counter;
    if col > n then [List.rev used_rows]
    else
      (if row < n then aux (row + 1) col used_rows usedD1 usedD2 file (depth+1)
       else [])
      @ (if possible row col used_rows usedD1 usedD2 then
           aux 1 (col + 1) (row :: used_rows) (row + col :: usedD1)
               (row - col :: usedD2) file (depth+1)
         else [])
  in aux 1 1 [] [] [] file depth;;

let main = begin
  for i = 0 to 10 do
    Random.self_init ();
    counter := 0;
    let directory_name = "eight_queens" in
    let is_dir_exist = Sys.file_exists directory_name in
    if not is_dir_exist
      then let _ = Sys.command (Printf.sprintf "mkdir %s" directory_name) in ();
      else ();
    let size = Random.int 12 in
    let filename = Printf.sprintf "./eight_queens/output-%d" size in (*what if filename already exist since we using random number*)
    let file = open_out filename in
    queens_positions size file 0;
    close_out file;
    let file = open_out_gen [Open_append; Open_creat] 0o666 "./eight_queens/traces" in
    Printf.fprintf file "%d;%d\n" size !counter;
    close_out file
  done
end;;

main;;
