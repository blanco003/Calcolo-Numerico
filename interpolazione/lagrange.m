function yy=lagrange(x,y,xx)
% Determina il polinomio interpolante di Lagrange pn(x)
% nei punti (x(i),y(i)), e lo valuta nei punti xx(i) 
%
% Parametri di input
%  x: vettore dei nodi
%  y: vettore delle ordinate
% xx: vettore di ascisse in cui valutare pn(x)
%
% Parametri di output
% yy: vettore delle valutazioni di pn(x) nelle ascisse xx(i)

n=length(x); %numero di nodi
yy=0;
for k=1:n
    Lk=1;
    for i=1:n
       if k~=i % oppure not(k==i)
          Lk=Lk.*(xx-x(i))/(x(k)-x(i)); 
       end
    end
    yy=yy+Lk*y(k);
end




