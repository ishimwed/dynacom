open Printf
type 'a binary_tree =
    | Empty
    | Node of 'a * 'a binary_tree * 'a binary_tree;;

let counter = ref 0;;

let rec size tree = match tree with
  | Empty -> 0
  | Node(_, l, r) -> 1 + size l + size l
;;

let rec random_list size l:int list=
  if size=0 then l
  else begin
  let x = (Random.int 500) in
  let li = x :: l in
    random_list (size - 1) li
  end

let rec inorder tree file depth =
  fprintf file "%d;%d\n" depth (size tree);
  if depth=0 then counter := !counter + 1 else counter := !counter;

  match tree with
  | Empty -> []
  | Node (v, l, r) -> inorder l file (depth+1) @ (v :: inorder r file (depth+1))
;;

let rec preorder tree file depth =
  fprintf file "%d;%d\n" depth (size tree);
  if depth=0 then counter := !counter + 1 else counter := !counter;

  match tree with
  | Empty -> []
  | Node (v, l, r) -> v :: (preorder l file (depth+1) @ preorder r file (depth+1))
;;

let rec insert tree x =
  match tree with
    | Empty -> Node(x, Empty, Empty)
    | Node(y, l, r) ->
       if x = y then tree
       else if x < y then Node(y, insert l x, r)
       else Node(y, l, insert r x)
;;

let construct l:int list = List.fold_left insert Empty l;;


let main = begin
  for i = 0 to 50 do
    Random.self_init ();
    counter := 0;
    let directory_name = "postorder" in
    let is_dir_exist = Sys.file_exists directory_name in
    if not is_dir_exist
      then let _ = Sys.command (sprintf "mkdir %s" directory_name) in ();
      else ();
    let size = Random.int 500 in
    let filename = sprintf "./postorder/output-%d" size in (*what if filename already exist since we using random number*)
    let file = open_out filename in
    let l = random_list size in
    let tree = construct l in
    preorder tree file 0;
    close_out file;
    let file = open_out_gen [Open_append; Open_creat] 0o666 "./postorder/traces" in
    fprintf file "%d;%d\n" size !counter;
    close_out file
  done
end;;

main;;
