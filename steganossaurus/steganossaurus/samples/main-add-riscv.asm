
# Disassembly of section .plt:

#0000000000010410 <_PROCEDURE_LINKAGE_TABLE_>:
#   10410:	97 23 00 00 33 03 c3 41 03 be 03 bf 13 03 43 fd     .#..3..A......C.
#   10420:	93 82 03 bf 13 53 13 00 83 b2 82 00 67 00 0e 00     .....S......g...

#0000000000010430 <__libc_start_main@plt>:
#   10430:	00002e17          	auipc	t3,0x2
#   10434:	be0e3e03          	ld	t3,-1056(t3) # 12010 <__libc_start_main@GLIBC_2.27>
#   10438:	000e0367          	jalr	t1,t3
#   1043c:	00000013          	nop

#0000000000010440 <printf@plt>:
#   10440:	00002e17          	auipc	t3,0x2
#   10444:	bd8e3e03          	ld	t3,-1064(t3) # 12018 <printf@GLIBC_2.27>
#   10448:	000e0367          	jalr	t1,t3
#   1044c:	00000013          	nop

#Disassembly of section .text:

#0000000000010450 <_start>:
   10450:	02e000ef          	jal	ra,1047e <load_gp>
   10454:	87aa                	mv	a5,a0
   10456:	00000517          	auipc	a0,0x0
   1045a:	09a50513          	addi	a0,a0,154 # 104f0 <main>
   1045e:	6582                	ld	a1,0(sp)
   10460:	0030                	addi	a2,sp,8
   10462:	ff017113          	andi	sp,sp,-16
   10466:	00000697          	auipc	a3,0x0
   1046a:	10668693          	addi	a3,a3,262 # 1056c <__libc_csu_init>
   1046e:	00000717          	auipc	a4,0x0
   10472:	15670713          	addi	a4,a4,342 # 105c4 <__libc_csu_fini>
   10476:	880a                	mv	a6,sp
   10478:	fb9ff0ef          	jal	ra,10430 <__libc_start_main@plt>
   1047c:	9002                	ebreak

000000000001047e <load_gp>:
   1047e:	00002197          	auipc	gp,0x2
   10482:	38218193          	addi	gp,gp,898 # 12800 <__global_pointer$>
   10486:	8082                	ret
	...

000000000001048a <deregister_tm_clones>:
   1048a:	6549                	lui	a0,0x12
   1048c:	6749                	lui	a4,0x12
   1048e:	00050793          	mv	a5,a0
   10492:	00070713          	mv	a4,a4
   10496:	00f70863          	beq	a4,a5,104a6 <deregister_tm_clones+0x1c>
   1049a:	00000793          	li	a5,0
   1049e:	c781                	beqz	a5,104a6 <deregister_tm_clones+0x1c>
   104a0:	00050513          	mv	a0,a0
   104a4:	8782                	jr	a5
   104a6:	8082                	ret

00000000000104a8 <register_tm_clones>:
   104a8:	6549                	lui	a0,0x12
   104aa:	00050793          	mv	a5,a0
   104ae:	6749                	lui	a4,0x12
   104b0:	00070593          	mv	a1,a4
   104b4:	8d9d                	sub	a1,a1,a5
   104b6:	4035d793          	srai	a5,a1,0x3
   104ba:	91fd                	srli	a1,a1,0x3f
   104bc:	95be                	add	a1,a1,a5
   104be:	8585                	srai	a1,a1,0x1
   104c0:	c599                	beqz	a1,104ce <register_tm_clones+0x26>
   104c2:	00000793          	li	a5,0
   104c6:	c781                	beqz	a5,104ce <register_tm_clones+0x26>
   104c8:	00050513          	mv	a0,a0
   104cc:	8782                	jr	a5
   104ce:	8082                	ret

00000000000104d0 <__do_global_dtors_aux>:
   104d0:	1141                	addi	sp,sp,-16
   104d2:	e022                	sd	s0,0(sp)
   104d4:	8381c783          	lbu	a5,-1992(gp) # 12038 <completed.0>
   104d8:	e406                	sd	ra,8(sp)
   104da:	e791                	bnez	a5,104e6 <__do_global_dtors_aux+0x16>
   104dc:	fafff0ef          	jal	ra,1048a <deregister_tm_clones>
   104e0:	4785                	li	a5,1
   104e2:	82f18c23          	sb	a5,-1992(gp) # 12038 <completed.0>
   104e6:	60a2                	ld	ra,8(sp)
   104e8:	6402                	ld	s0,0(sp)
   104ea:	0141                	addi	sp,sp,16
   104ec:	8082                	ret

00000000000104ee <frame_dummy>:
   104ee:	bf6d                	j	104a8 <register_tm_clones>

00000000000104f0 <main>:
   104f0:	1141                	addi	sp,sp,-16
   104f2:	e406                	sd	ra,8(sp)
   104f4:	e022                	sd	s0,0(sp)
   104f6:	0800                	addi	s0,sp,16
   104f8:	0001                	nop
   104fa:	0001                	nop
   104fc:	8086                	mv	ra,ra
   104fe:	0001                	nop
   10500:	0001                	nop
   10502:	0001                	nop
   10504:	0001                	nop
   10506:	0001                	nop
   10508:	0001                	nop
   1050a:	0001                	nop
   1050c:	0001                	nop
   1050e:	0001                	nop
   10510:	0001                	nop
   10512:	0001                	nop
   10514:	0001                	nop
   10516:	0001                	nop
   10518:	0001                	nop
   1051a:	0001                	nop
   1051c:	0001                	nop
   1051e:	0001                	nop
   10520:	0001                	nop
   10522:	0001                	nop
   10524:	0001                	nop
   10526:	0001                	nop
   10528:	0001                	nop
   1052a:	0001                	nop
   1052c:	0001                	nop
   1052e:	0001                	nop
   10530:	0001                	nop
   10532:	0001                	nop
   10534:	0001                	nop
   10536:	0001                	nop
   10538:	0001                	nop
   1053a:	0001                	nop
   1053c:	0001                	nop
   1053e:	0001                	nop
   10540:	0001                	nop
   10542:	0001                	nop
   10544:	0001                	nop
   10546:	0001                	nop
   10548:	0001                	nop
   1054a:	0001                	nop
   1054c:	0001                	nop
   1054e:	0001                	nop
   10550:	0001                	nop
   10552:	0001                	nop
   10554:	0001                	nop
   10556:	67c1                	lui	a5,0x10
   10558:	5c878513          	addi	a0,a5,1480 # 105c8 <__libc_csu_fini+0x4>
   1055c:	ee5ff0ef          	jal	ra,10440 <printf@plt>
   10560:	4781                	li	a5,0
   10562:	853e                	mv	a0,a5
   10564:	60a2                	ld	ra,8(sp)
   10566:	6402                	ld	s0,0(sp)
   10568:	0141                	addi	sp,sp,16
   1056a:	8082                	ret

000000000001056c <__libc_csu_init>:
   1056c:	7139                	addi	sp,sp,-64
   1056e:	f822                	sd	s0,48(sp)
   10570:	f04a                	sd	s2,32(sp)
   10572:	00002417          	auipc	s0,0x2
   10576:	89e40413          	addi	s0,s0,-1890 # 11e10 <__frame_dummy_init_array_entry>
   1057a:	00002917          	auipc	s2,0x2
   1057e:	89e90913          	addi	s2,s2,-1890 # 11e18 <__do_global_dtors_aux_fini_array_entry>
   10582:	40890933          	sub	s2,s2,s0
   10586:	fc06                	sd	ra,56(sp)
   10588:	f426                	sd	s1,40(sp)
   1058a:	ec4e                	sd	s3,24(sp)
   1058c:	e852                	sd	s4,16(sp)
   1058e:	e456                	sd	s5,8(sp)
   10590:	40395913          	srai	s2,s2,0x3
   10594:	00090f63          	beqz	s2,105b2 <__libc_csu_init+0x46>
   10598:	89aa                	mv	s3,a0
   1059a:	8a2e                	mv	s4,a1
   1059c:	8ab2                	mv	s5,a2
   1059e:	4481                	li	s1,0
   105a0:	601c                	ld	a5,0(s0)
   105a2:	8656                	mv	a2,s5
   105a4:	85d2                	mv	a1,s4
   105a6:	854e                	mv	a0,s3
   105a8:	0485                	addi	s1,s1,1
   105aa:	9782                	jalr	a5
   105ac:	0421                	addi	s0,s0,8
   105ae:	fe9919e3          	bne	s2,s1,105a0 <__libc_csu_init+0x34>
   105b2:	70e2                	ld	ra,56(sp)
   105b4:	7442                	ld	s0,48(sp)
   105b6:	74a2                	ld	s1,40(sp)
   105b8:	7902                	ld	s2,32(sp)
   105ba:	69e2                	ld	s3,24(sp)
   105bc:	6a42                	ld	s4,16(sp)
   105be:	6aa2                	ld	s5,8(sp)
   105c0:	6121                	addi	sp,sp,64
   105c2:	8082                	ret

00000000000105c4 <__libc_csu_fini>:
   105c4:	8082                	ret
