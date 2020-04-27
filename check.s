.data
.word 7, 7, 8, 5, 2
.globl main

la $a0, 0x10000000 
lw $a1, 0($a0)
lw $a2, 0($a0)
beq $a1,$a2,label
add $a3,$a1,$a2
label:
add $a2,$a4,$a1
lw $a2,4($a0)
addi $a2,$a2,1

