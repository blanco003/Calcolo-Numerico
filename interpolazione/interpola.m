function interpola(f,int,n)
% interpolazione polimoniale di una funzione
%
% Parametri di input
%   f: funzione (eventualmente inline)
% int: intervallo di rappresentazione
%   n: numero di nodi equidistanti che ricoprono l'intervallo int
%
% Esempio (dal command window)
% f1=@(x)(exp(-x).*sin(x))
% interpola(f1,[0,pi],10)

a=int(1);
b=int(2);
x=linspace(a,b,n);
y=f(x); %vettore delle ordinate
xx=linspace(a,b,1000);
yy=lagrange(x,y,xx);
fxx=f(xx);

figure(1)
plot(x,y,'or',xx,fxx,xx,yy)
legend('nodi','f(x)','p(x)')
grid on
title('Interpolazione di lagrange')
xlabel('x')
ylabel('y')
set(gca,'fontsize',24)