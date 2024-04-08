Si scriva una funzione Python/Matlab che abbia in input una matrice (array a due indici) A quadrata a coefficienti interi, e in output una variabili così definita : 

$$
x=
\begin{cases}
1 &  \qquad \text{se } A \text{ possiede una riga e una colonna uguali} \\
0  & \qquad \text{altrimenti } 
\end{cases}
$$

Esempio. In corisspondenza della matrice

$$A=\begin{pmatrix}  
-2 & -1 & 2\\  
3  &  2 & 3\\  
2  &  3 & 0\\  
\end{pmatrix}$$

il programma dovrà restituire in output il valore x = 1 (confrontare l'ultima riga e colonna di A)