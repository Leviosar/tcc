# ISA

A ISA do RISC-V na verdade é um conjunto de conjuntos base e extensões, facilitando a modularização para implementações. Como a ideia é trabalhar apenas em algumas instruções, o Decoder não precisa cobrir todas os conjuntos, mas uma abrangência maior pode facilitar o processo de desenvolvimento do algoritmo e de novas otimizações.

No capítulo 2.2 do RISC-V Unprivileged ISA V20191213 estão descritos os formatos de instrução utilizados como base para desenvolver o decoder.

# C Extension

A extensão C do RISC-V introduz instruções compactas de 16 bits para reduzir o tamanho do código. Essa extensão é a prova de que otimização deixa a ISA uma bagunça desgraçada, já que nelas temos extensões de tamanhos diferentes