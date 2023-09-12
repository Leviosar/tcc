	.cpu arm7tdmi
	.eabi_attribute 20, 1
	.eabi_attribute 21, 1
	.eabi_attribute 23, 3
	.eabi_attribute 24, 1
	.eabi_attribute 25, 1
	.eabi_attribute 26, 1
	.eabi_attribute 30, 6
	.eabi_attribute 34, 0
	.eabi_attribute 18, 4
	.file	"main.c"
	.text
	.align	2
	.global	main
	.syntax unified
	.arm
	.fpu softvfp
	.type	main, %function
main:
	@ Function supports interworking.
	@ args = 0, pretend = 0, frame = 0
	@ frame_needed = 1, uses_anonymous_args = 0
	@ link register save eliminated.
	str	fp, [sp, #-4]!
	add	fp, sp, #0
	.syntax divided
@ 4 "main.c" 1
	nop
@ 0 "" 2
@ 5 "main.c" 1
	nop
@ 0 "" 2
@ 6 "main.c" 1
	nop
@ 0 "" 2
@ 7 "main.c" 1
	nop
@ 0 "" 2
@ 8 "main.c" 1
	nop
@ 0 "" 2
@ 9 "main.c" 1
	nop
@ 0 "" 2
@ 10 "main.c" 1
	nop
@ 0 "" 2
@ 11 "main.c" 1
	nop
@ 0 "" 2
@ 12 "main.c" 1
	nop
@ 0 "" 2
@ 13 "main.c" 1
	nop
@ 0 "" 2
@ 14 "main.c" 1
	nop
@ 0 "" 2
@ 15 "main.c" 1
	nop
@ 0 "" 2
@ 16 "main.c" 1
	nop
@ 0 "" 2
@ 17 "main.c" 1
	nop
@ 0 "" 2
@ 18 "main.c" 1
	nop
@ 0 "" 2
@ 19 "main.c" 1
	nop
@ 0 "" 2
@ 20 "main.c" 1
	nop
@ 0 "" 2
@ 21 "main.c" 1
	nop
@ 0 "" 2
@ 22 "main.c" 1
	nop
@ 0 "" 2
@ 23 "main.c" 1
	nop
@ 0 "" 2
@ 24 "main.c" 1
	nop
@ 0 "" 2
@ 25 "main.c" 1
	nop
@ 0 "" 2
@ 26 "main.c" 1
	nop
@ 0 "" 2
@ 27 "main.c" 1
	nop
@ 0 "" 2
@ 28 "main.c" 1
	nop
@ 0 "" 2
@ 29 "main.c" 1
	nop
@ 0 "" 2
@ 30 "main.c" 1
	nop
@ 0 "" 2
@ 31 "main.c" 1
	nop
@ 0 "" 2
@ 32 "main.c" 1
	nop
@ 0 "" 2
@ 33 "main.c" 1
	nop
@ 0 "" 2
@ 34 "main.c" 1
	nop
@ 0 "" 2
@ 35 "main.c" 1
	nop
@ 0 "" 2
@ 36 "main.c" 1
	nop
@ 0 "" 2
@ 37 "main.c" 1
	nop
@ 0 "" 2
@ 38 "main.c" 1
	nop
@ 0 "" 2
@ 39 "main.c" 1
	nop
@ 0 "" 2
@ 40 "main.c" 1
	nop
@ 0 "" 2
@ 41 "main.c" 1
	nop
@ 0 "" 2
@ 42 "main.c" 1
	nop
@ 0 "" 2
@ 43 "main.c" 1
	nop
@ 0 "" 2
@ 44 "main.c" 1
	nop
@ 0 "" 2
@ 45 "main.c" 1
	nop
@ 0 "" 2
@ 46 "main.c" 1
	nop
@ 0 "" 2
@ 47 "main.c" 1
	nop
@ 0 "" 2
@ 48 "main.c" 1
	nop
@ 0 "" 2
	.arm
	.syntax unified
	mov	r3, #0
	mov	r0, r3
	add	sp, fp, #0
	@ sp needed
	ldr	fp, [sp], #4
	bx	lr
	.size	main, .-main
	.ident	"GCC: (GNU) 7.2.0"
