
main:     file format elf64-littleriscv


Disassembly of section .plt:

00000000000103c0 <_PROCEDURE_LINKAGE_TABLE_>:
   103c0:	97 23 00 00 33 03 c3 41 03 be 03 c4 13 03 43 fd     .#..3..A......C.
   103d0:	93 82 03 c4 13 53 13 00 83 b2 82 00 67 00 0e 00     .....S......g...

00000000000103e0 <__libc_start_main@plt>:
   103e0:	00002e17          	auipc	t3,0x2
   103e4:	c30e3e03          	ld	t3,-976(t3) # 12010 <__libc_start_main@GLIBC_2.27>
   103e8:	000e0367          	jalr	t1,t3
   103ec:	00000013          	nop

Disassembly of section .text:

00000000000103f0 <_start>:
   103f0:	02e000ef          	jal	ra,1041e <load_gp>
   103f4:	87aa                	mv	a5,a0
   103f6:	00000517          	auipc	a0,0x0
   103fa:	09a50513          	addi	a0,a0,154 # 10490 <main>
   103fe:	6582                	ld	a1,0(sp)
   10400:	0030                	addi	a2,sp,8
   10402:	ff017113          	andi	sp,sp,-16
   10406:	00000697          	auipc	a3,0x0
   1040a:	0f868693          	addi	a3,a3,248 # 104fe <__libc_csu_init>
   1040e:	00000717          	auipc	a4,0x0
   10412:	14870713          	addi	a4,a4,328 # 10556 <__libc_csu_fini>
   10416:	880a                	mv	a6,sp
   10418:	fc9ff0ef          	jal	ra,103e0 <__libc_start_main@plt>
   1041c:	9002                	ebreak

000000000001041e <load_gp>:
   1041e:	00002197          	auipc	gp,0x2
   10422:	3e218193          	addi	gp,gp,994 # 12800 <__global_pointer$>
   10426:	8082                	ret
	...

000000000001042a <deregister_tm_clones>:
   1042a:	6549                	lui	a0,0x12
   1042c:	6749                	lui	a4,0x12
   1042e:	00050793          	mv	a5,a0
   10432:	00070713          	mv	a4,a4
   10436:	00f70863          	beq	a4,a5,10446 <deregister_tm_clones+0x1c>
   1043a:	00000793          	li	a5,0
   1043e:	c781                	beqz	a5,10446 <deregister_tm_clones+0x1c>
   10440:	00050513          	mv	a0,a0
   10444:	8782                	jr	a5
   10446:	8082                	ret

0000000000010448 <register_tm_clones>:
   10448:	6549                	lui	a0,0x12
   1044a:	00050793          	mv	a5,a0
   1044e:	6749                	lui	a4,0x12
   10450:	00070593          	mv	a1,a4
   10454:	8d9d                	sub	a1,a1,a5
   10456:	4035d793          	srai	a5,a1,0x3
   1045a:	91fd                	srli	a1,a1,0x3f
   1045c:	95be                	add	a1,a1,a5
   1045e:	8585                	srai	a1,a1,0x1
   10460:	c599                	beqz	a1,1046e <register_tm_clones+0x26>
   10462:	00000793          	li	a5,0
   10466:	c781                	beqz	a5,1046e <register_tm_clones+0x26>
   10468:	00050513          	mv	a0,a0
   1046c:	8782                	jr	a5
   1046e:	8082                	ret

0000000000010470 <__do_global_dtors_aux>:
   10470:	1141                	addi	sp,sp,-16
   10472:	e022                	sd	s0,0(sp)
   10474:	8301c783          	lbu	a5,-2000(gp) # 12030 <completed.0>
   10478:	e406                	sd	ra,8(sp)
   1047a:	e791                	bnez	a5,10486 <__do_global_dtors_aux+0x16>
   1047c:	fafff0ef          	jal	ra,1042a <deregister_tm_clones>
   10480:	4785                	li	a5,1
   10482:	82f18823          	sb	a5,-2000(gp) # 12030 <completed.0>
   10486:	60a2                	ld	ra,8(sp)
   10488:	6402                	ld	s0,0(sp)
   1048a:	0141                	addi	sp,sp,16
   1048c:	8082                	ret

000000000001048e <frame_dummy>:
   1048e:	bf6d                	j	10448 <register_tm_clones>

0000000000010490 <main>:
   10490:	1141                	addi	sp,sp,-16
   10492:	e422                	sd	s0,8(sp)
   10494:	0800                	addi	s0,sp,16
   10496:	0001                	nop
   10498:	0001                	nop
   1049a:	8086                	mv	ra,ra
   1049c:	0001                	nop
   1049e:	0001                	nop
   104a0:	0001                	nop
   104a2:	0001                	nop
   104a4:	0001                	nop
   104a6:	0001                	nop
   104a8:	0001                	nop
   104aa:	0001                	nop
   104ac:	0001                	nop
   104ae:	0001                	nop
   104b0:	0001                	nop
   104b2:	0001                	nop
   104b4:	0001                	nop
   104b6:	0001                	nop
   104b8:	0001                	nop
   104ba:	0001                	nop
   104bc:	0001                	nop
   104be:	0001                	nop
   104c0:	0001                	nop
   104c2:	0001                	nop
   104c4:	0001                	nop
   104c6:	0001                	nop
   104c8:	0001                	nop
   104ca:	0001                	nop
   104cc:	0001                	nop
   104ce:	0001                	nop
   104d0:	0001                	nop
   104d2:	0001                	nop
   104d4:	0001                	nop
   104d6:	0001                	nop
   104d8:	0001                	nop
   104da:	0001                	nop
   104dc:	0001                	nop
   104de:	0001                	nop
   104e0:	0001                	nop
   104e2:	0001                	nop
   104e4:	0001                	nop
   104e6:	0001                	nop
   104e8:	0001                	nop
   104ea:	0001                	nop
   104ec:	0001                	nop
   104ee:	0001                	nop
   104f0:	0001                	nop
   104f2:	0001                	nop
   104f4:	4781                	li	a5,0
   104f6:	853e                	mv	a0,a5
   104f8:	6422                	ld	s0,8(sp)
   104fa:	0141                	addi	sp,sp,16
   104fc:	8082                	ret

00000000000104fe <__libc_csu_init>:
   104fe:	7139                	addi	sp,sp,-64
   10500:	f822                	sd	s0,48(sp)
   10502:	f04a                	sd	s2,32(sp)
   10504:	00002417          	auipc	s0,0x2
   10508:	90c40413          	addi	s0,s0,-1780 # 11e10 <__frame_dummy_init_array_entry>
   1050c:	00002917          	auipc	s2,0x2
   10510:	90c90913          	addi	s2,s2,-1780 # 11e18 <__do_global_dtors_aux_fini_array_entry>
   10514:	40890933          	sub	s2,s2,s0
   10518:	fc06                	sd	ra,56(sp)
   1051a:	f426                	sd	s1,40(sp)
   1051c:	ec4e                	sd	s3,24(sp)
   1051e:	e852                	sd	s4,16(sp)
   10520:	e456                	sd	s5,8(sp)
   10522:	40395913          	srai	s2,s2,0x3
   10526:	00090f63          	beqz	s2,10544 <__libc_csu_init+0x46>
   1052a:	89aa                	mv	s3,a0
   1052c:	8a2e                	mv	s4,a1
   1052e:	8ab2                	mv	s5,a2
   10530:	4481                	li	s1,0
   10532:	601c                	ld	a5,0(s0)
   10534:	8656                	mv	a2,s5
   10536:	85d2                	mv	a1,s4
   10538:	854e                	mv	a0,s3
   1053a:	0485                	addi	s1,s1,1
   1053c:	9782                	jalr	a5
   1053e:	0421                	addi	s0,s0,8
   10540:	fe9919e3          	bne	s2,s1,10532 <__libc_csu_init+0x34>
   10544:	70e2                	ld	ra,56(sp)
   10546:	7442                	ld	s0,48(sp)
   10548:	74a2                	ld	s1,40(sp)
   1054a:	7902                	ld	s2,32(sp)
   1054c:	69e2                	ld	s3,24(sp)
   1054e:	6a42                	ld	s4,16(sp)
   10550:	6aa2                	ld	s5,8(sp)
   10552:	6121                	addi	sp,sp,64
   10554:	8082                	ret

0000000000010556 <__libc_csu_fini>:
   10556:	8082                	ret
