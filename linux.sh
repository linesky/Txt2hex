printf "\x1bc\x1b[43;37m give me a file to convert to binary? "
read file1
printf "give me a file name binary? "
read file2
nasm $file1 -o $file2
