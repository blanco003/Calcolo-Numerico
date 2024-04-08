# Congettura di Collaz
Sia $x_0$ un numero intero positivo. Per n = 0, 1, 2, . . . , si consideri
la successione $\{x_n\}$ definita ricorsivamente come segue:

$$
x_{n+1}=
\begin{cases}
{x_n \over 2} &  \qquad \text{se } x_n \text{ è pari} \\
3x_n+1  & \qquad \text{se } x_n \text{ è dispari}
\end{cases}
$$

La congettura di Collaz
afferma che qualsiasi sia il punto iniziale $x_0$, l’algoritmo
raggiunge sempre il valore 1 dopo un numero finito di passi, ovvero:

$$\text{per ogni intero positivo } x_0 \space \space  \text{esiste}\space \space  n \in \mathbb{N} \space \space \text{tale che} \space \space x_n = 1$$

Esercizio : Si scriva una funzione che abbia in input un numero intero positivo $x_0$ e restituisca in output
- il più piccolo intero $n$ tale che $x_n$ = 1;
- una lista x che contenga l’intera sequenza di valori $x_0, x_1,\dots, x_n$.

Suggerimento : Per stabilire se un numero è pari o dispari, può essere utile la function
mod del modulo numpy. Se x e y sono due numeri interi positivi, mod(x, y) restituisce
il resto della divisione tra x e y. Dunque se mod(x, 2) è uguale a 0, x è pari, mentre se
è uguale a 1, allora x è dispari.
