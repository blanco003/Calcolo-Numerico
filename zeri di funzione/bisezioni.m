function alpha = bisezioni(f,a,b,tol,itmax)
%Metodo delle successive bisezioni
%Parametri di input:
%    f : funzione di cui ricercare uno zero alpha
%[a,b] : intervallo di lavoro
%  tol : precisione richiesta
%itmax : numero massimo di iterate consentite
%Parametri di output:
%alpha : zero di f

if nargin==4   %nargin conta il numero di parametri di input ricevuti
    itmax=100;
end

fa = f(a);
fb = f(b);
if fa*fb > 0
    error('La funzione non cambia segno agli estremi dell''intervallo')
end

it=0;

while b-a > tol && it<itmax
    it=it+1;
    c = (a+b)/2;
    fc = f(c);

    if fc==0
        alpha = c;
        return
    elseif fa*fc < 0
        b = c;
        fb = fc; %e' possibile eliminare questa assegnazione
    else
        a = c;
        fa = fc;
    end
end

if b-a>tol
    warning('precisione non raggiunta')
end
alpha=c;
