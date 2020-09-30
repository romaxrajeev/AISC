male(b).
male(d).
male(f).
female(a).
female(c).
female(e).

married(a,b).
married(c,d).

parents(c,a).
parents(c,b).
parents(e,c).
parents(e,d).
parents(f,d).
parents(f,d).

soninlaw(Person1,Person2):- male(Person1),married(X,Person1),parents(X,Person2).

grandfather(Person1,Person2):- male(Person2),parents(Person1,X),parents(X,Person2).

sister(Person1,Person2):- female(Person2),parents(Person1,X),parents(Person2,X).
