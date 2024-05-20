function det=laplace(A)

% calcola il determinante di una matrice (quadrata)
%  mediante la regola di laplace applicata nella prima riga

% Parametri di input : 
% A: matrice quadrata

% Parametri di output : 
% det: determinante di A

[m,n]=size(A);

if m~=n 
    error('matrice non quadrata')
end

if n==1
    det=A;
else
    det=0;
    for j=1:n

        % metodo abbreviato
        A1j=A(2:m,[1:j-1,j+1:n]);

        % metodo corretto ma con più righe
        % A1j = A;
        % A1j(1,:) = [];
        % A1j(:,j) = [];

        det=det+(-1)^(1+j)*A(1,j)*laplace(A1j);
    end
end

