{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Correction TP n°6 : Fonctions 1/2\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "___________________________________________________________________________\n",
    "## Fonction de calcul du volume du ballon de rugby\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Consulter l'article de wikipedia donnant le volume d'un [ellipsoïde de révolution](https://fr.wikipedia.org/wiki/Ellipso%C3%AFde_de_r%C3%A9volution#Volume_int.C3.A9rieur).\n",
    "\n",
    "Ecrire une fonction `volumeRugby(H, L)` qui détermine le volume d'un ballon de rugby de hauteur `H` et de largeur `L`. On écrira explicitement la formule utilisée par Wikipedia, avec ses variables et après avoir fait le lien avec les variables `H` et `L`.\n",
    "\n",
    "On importera `pi` avec le module math.\n",
    "\n",
    "Appliquer à un ballon standard de tailles $H = 29 \\text{cm}$ et $L=  19 \\text{cm}$, de volume environ 5,5 litres.\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Correction\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5.48155558173859\n"
     ]
    }
   ],
   "source": [
    "from math import pi\n",
    "\n",
    "def volumeRugby(H, L):\n",
    "    p=H/2\n",
    "    q=L/2\n",
    "    V=4/3*pi*p*q**2\n",
    "    return V\n",
    "\n",
    "H=2.9\n",
    "L=1.9\n",
    "\n",
    "print(volumeRugby(H, L))\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "___________________________________________________________________________\n",
    "## Implémenter la fonction `max`\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Écrire une fonction `maxi` qui renvoie le maximum de deux nombres `a` et `b` passés en paramètre.\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Correction\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3\n",
      "3\n",
      "3\n"
     ]
    }
   ],
   "source": [
    "def maxi(a,b):\n",
    "    if a>=b:\n",
    "        return a\n",
    "    else:\n",
    "        return b\n",
    "    \n",
    "print(maxi(3,2))\n",
    "\n",
    "\n",
    "# Variante\n",
    "\n",
    "def maxi(a,b):\n",
    "    if a>b:\n",
    "        return a\n",
    "    return b\n",
    "    \n",
    "print(maxi(3,2))\n",
    "\n",
    "# Variante\n",
    "\n",
    "def maxi(a,b):\n",
    "    if a>b:\n",
    "        ret= a\n",
    "    else:\n",
    "        ret = b\n",
    "    return ret\n",
    "    \n",
    "print(maxi(3,2))\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "___________________________________________________________________________\n",
    "## Implémenter la fonction *valeur absolue*\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Écrire une fonction `val_abs` qui retourne la valeur absolue d'un nombre `x` passé en paramètre.\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Correction\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2 2 0\n"
     ]
    }
   ],
   "source": [
    "def val_abs(x):\n",
    "    if x<0:\n",
    "        return -x\n",
    "    else:\n",
    "        return x\n",
    "\n",
    "print(val_abs(2), val_abs(-2), val_abs(0))\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "___________________________________________________________________________\n",
    "## Fonction pour année bissextile\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Écrire une fonction `estBissextile` qui prend en paramètre un entier `a` et retourne `True` si l'année `a` est bissextile (`False` sinon). Pour rappel, une année `a` est bissextile si le booléen suivant\n",
    "\n",
    "`(a%4==0 and a%100!=0) or a%400==0`\n",
    "\n",
    "vaut `True`.\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Correction\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "False True True\n"
     ]
    }
   ],
   "source": [
    "def estBissextile(a):\n",
    "    return (a%4==0 and a%100!=0) or a%400==0\n",
    "print(estBissextile(2019), estBissextile(2020), estBissextile(2000))\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "___________________________________________________________________________\n",
    "## Fonctions Celsius <-> Fahrenheit\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "1) La formule de conversion de degrés Fahrenheit vers des degrés Celsius est\n",
    "\n",
    "$$c=\\frac{5}{9}(f-32) $$\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "a) Écrire une fonction `f2c(f)` qui prend en paramètre une température $f$ (en degrés Fahrenheit) et qui renvoie sa conversion $c$ (en degrés Celsius).\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "b) Combien font $451^\\circ F$ et $0 ^\\circ F$ en $^\\circ C$ ?\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "2) La formule de conversion de degrés Celsius vers des degrés Fahrenheit est  $$f=\\frac{9}{5}c+32 $$\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "a) Écrire une fonction `c2f(c)` qui prend en paramètre une température $c$ (en degrés Celsius) et qui renvoie sa conversion $f$ (en degrés Fahrenheit)\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "b) Combien font $42^\\circ C$ et $-273,15 ^\\circ C$ en $^\\circ F$ ?\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "3) Pour trois valeurs `x` qui vous choisirez librement, vérifiez que `c2f(f2c(x))` et `f2c(c2f(x))` sont proches de `x`.\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Correction\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "232.7777777777778 -17.77777777777778\n",
      "-459.66999999999996 32.0\n",
      "0 0.0 0.0\n",
      "451 451.00000000000006 451.00000000000006\n",
      "42 42.00000000000001 42.0\n"
     ]
    }
   ],
   "source": [
    "def f2c(f):\n",
    "    return 5/9*(f-32)\n",
    "\n",
    "def c2f(c):\n",
    "    return 9/5 * c + 32\n",
    "\n",
    "print(f2c(451), f2c(0))\n",
    "print(c2f(-273.15), c2f(0))\n",
    "\n",
    "for x in [0, 451, 42]:\n",
    "    print(x, f2c(c2f(x)), c2f(f2c(x)))\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "___________________________________________________________________________\n",
    "## Calcul d'une durée\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "1) Écrire une fonction `hms_to_s(h, m, s)` qui retourne en secondes une durée exprimée en heures, minutes et secondes. Vérifier que 1h30m = 5400s et 3h20m15s = 12015s.\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "2) Écrire une fonction `s_to_hms(sec)` qui prend en paramètre une durée exprimée en secondes et la retourne exprimée en heures, minutes et secondes sous forme de liste [h, m, s]. Vérifier que `s_to_hms(5400)` retourne la liste `[1, 30, 0]`, et que `s_to_hms(12015)` retourne la liste `[3, 20, 15]`.\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "3) Écrire une fonction `afficher_temps` capable d'afficher une liste [h, m, s] sous la forme `h heures m minutes et s secondes`. Par exemple, `afficher_temps([2, 42, 16])` affiche `2 heures 42 minutes et 16 secondes`.\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "4) Sans définir de nouvelle fonction, écrire un code, tenant de préférence sur une seule ligne, qui affiche le temps écoulé comme à la question précédente entre 13h58m et 15h31m30s.\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Correction\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5400 12015\n"
     ]
    }
   ],
   "source": [
    "def hms_to_s(h,m,s):\n",
    "    return h*3600+m*60+s\n",
    "print(hms_to_s(1,30,0), hms_to_s(3,20,15))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 30, 0] [3, 20, 15]\n",
      "1 h 33 m 30 s\n"
     ]
    }
   ],
   "source": [
    "    def s_to_hms(s):\n",
    "        heures=s//3600\n",
    "        r=s-3600*heures\n",
    "        minutes=r//60\n",
    "        secondes=r-60*minutes\n",
    "        \n",
    "        return [heures, minutes, secondes]\n",
    "    print(s_to_hms(5400), s_to_hms(12015))\n",
    "    def afficher_temps(hms):\n",
    "        print(hms[0],'h',hms[1],'m',hms[2],'s')\n",
    "    afficher_temps(s_to_hms(hms_to_s(15,31,30)-hms_to_s(13,58,0)))\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "___________________________________________________________________________\n",
    "## Équation du second degré (version fonction)\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "On rappelle ci-dessous un code de résolution et d'affichage des solutions d'une équation du second degré $ax^2+bx+c=0$ mais n'utilisant ni fonction ni liste :\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2 solutions distinctes :\n",
      "x1 = 0.3333333333333333\n",
      "x2 = 0.5\n"
     ]
    }
   ],
   "source": [
    "a = 6\n",
    "b = -5\n",
    "c = 1\n",
    "delta = b*b -4*a*c\n",
    "if delta >0:\n",
    "    print(\"2 solutions distinctes :\")\n",
    "    print(\"x1 =\", (-b - delta**0.5)/(2.*a))\n",
    "    print(\"x2 =\", (-b + delta**0.5)/(2.*a))\n",
    "elif delta == 0:\n",
    "    print(\"une seule solution\")\n",
    "    print(\"x =\", (-b)/(2.*a))\n",
    "else:\n",
    "    print(\"Aucune solution\")\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Vous devez adapter ce code pour les questions ci-dessous.\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "1) Ecrire une fonction `resoudre_2nd_degre(a, b, c)` qui résout dans l'ensemble des nombres réels l'équation du second degré. La fonction prend en paramètre $\\mathtt{a, b, c}$ les coefficients supposés entiers de l'équation $\\mathtt{ax^2+bx+c=0}$ et renvoie une **liste** de solutions, éventuellement vide.\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "2) Ecrire une fonction d'affichage `afficher_solutions(a, b, c)` des solutions. La fonction affichage doit utiliser la fonction précédente.\n",
    "\n",
    "Voici un exemple de comportements du code à écrire :\n",
    "\n",
    "    a = 6 b = -5 c = 1 :\n",
    "    \n",
    "    2 solutions distinctes :\n",
    "    x1 = 0.3333333333333333\n",
    "    x2 = 0.5\n",
    "    ----------------------------------------------\n",
    "    a = 4 b = -12 c = 9 :\n",
    "    \n",
    "    une seule solution\n",
    "    x = 1.5\n",
    "    ----------------------------------------------\n",
    "    a = 6 b = 7 c = 7 :\n",
    "          \n",
    "    Aucune solution\n",
    "    ----------------------------------------------\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Correction\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def resoudre_2nd_degre(a, b, c):\n",
    "    delta = b*b -4*a*c\n",
    "    if delta >0:\n",
    "        d=delta**0.5\n",
    "        x1=(-b - d)/(2.*a)\n",
    "        x2=(-b + d)/(2.*a)\n",
    "        return [x1, x2]\n",
    "    else:\n",
    "        if delta == 0:\n",
    "            return [-b/(2.*a)]\n",
    "        else:\n",
    "            return []\n",
    "\n",
    "\n",
    "def afficher_solutions(a, b, c):\n",
    "    L=resoudre_2nd_degre(a,b,c)\n",
    "    n=len(L)\n",
    "    if n==2:\n",
    "        print(\"2 solutions distinctes :\")\n",
    "        print(\"x1 =\", L[0])\n",
    "        print(\"x2 =\", L[1])\n",
    "    else:\n",
    "        if n == 1:\n",
    "            print(\"une seule solution\")\n",
    "            print(\"x =\", L[0])\n",
    "        else:\n",
    "            print(\"Aucune solution\")\n",
    "\n",
    "for (a,b, c) in [[6, -5, 1], [4, -12, 9], [6, 7, 7]]:\n",
    "    print(\"a =\", a, \"b =\", b, \"c =\", c, \":\")\n",
    "    print()\n",
    "    afficher_solutions(a, b, c)\n",
    "    print(\"----------------------------------------------\")\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "___________________________________________________________________________\n",
    "## Fonction binomiale\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "1) Écrire une fonction `factorielle` qui renvoie la valeur factorielle de `n` où `n` étant passé en paramètre. Par exemple $1!=1$ et $5!=120$. On convient que $0!=1$. On écrira une version de la fonction factorielle utilisant une boucle `for`.\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "2) On rappelle que si $n$ et $p$ sont des entiers positifs ou nuls, le coefficient binomial est défini par\n",
    "\n",
    "$$\\binom{n}{p}=\\begin{cases}\\displaystyle\\frac{n!}{p!(n-p)!}& \\text{si } 0\\leq p\\leq n\\\\0& \\text{sinon}\\end{cases}$$\n",
    "\n",
    "Ecrire une fonction `binomial(n, p)` qui renvoie le coefficient binomial ci-dessus.\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "3) Ecrire une fonction `pascal` qui vérifie l'identité  de Pascal : $\\binom{n}{p}+\\binom{n}{p+1}=\\binom{n+1}{p+1}$ valable pour tous entiers $n, p\\geq 0$. Vérifier l'identité pour tous les entiers $n$ et $p$ entre 0 et 100.\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "4) Ecrire une fonction `maxBinomial(n)` qui renvoie la valeur maximale de tous les coefficients binomiaux  $\\binom{n}{0}, \\binom{n}{1}, \\binom{n}{2}, \\cdots , \\binom{n}{n}$\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "5) Ecrire une fonction `verifMaxBinomial(n)` qui vérifie que la valeur maximale de tous les coefficients binomiaux $\\binom{n}{0}, \\binom{n}{1}, \\binom{n}{2}, \\cdots, \\binom{n}{n}$ est $\\binom{n}{m}$ où $m$ est le quotient la division entière de $n$ par 2.\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Correction\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "reglePascal pour N =  100  :  True\n",
      "verif Max binomial pour n =  1  :  True\n",
      "verif Max binomial pour n =  2  :  True\n",
      "verif Max binomial pour n =  3  :  True\n",
      "verif Max binomial pour n =  4  :  True\n",
      "verif Max binomial pour n =  5  :  True\n",
      "verif Max binomial pour n =  6  :  True\n",
      "verif Max binomial pour n =  7  :  True\n",
      "verif Max binomial pour n =  8  :  True\n",
      "verif Max binomial pour n =  9  :  True\n",
      "verif Max binomial pour n =  10  :  True\n",
      "verif Max binomial pour n =  11  :  True\n",
      "verif Max binomial pour n =  12  :  True\n",
      "verif Max binomial pour n =  13  :  True\n",
      "verif Max binomial pour n =  14  :  True\n",
      "verif Max binomial pour n =  15  :  True\n",
      "verif Max binomial pour n =  16  :  True\n",
      "verif Max binomial pour n =  17  :  True\n",
      "verif Max binomial pour n =  18  :  True\n",
      "verif Max binomial pour n =  19  :  True\n",
      "verif Max binomial pour n =  20  :  True\n",
      "verif Max binomial pour n =  21  :  True\n",
      "verif Max binomial pour n =  22  :  True\n",
      "verif Max binomial pour n =  23  :  True\n",
      "verif Max binomial pour n =  24  :  True\n"
     ]
    }
   ],
   "source": [
    "def factorielle(n):\n",
    "    fact=1\n",
    "    for i in range(1,n+1):\n",
    "        fact=fact*i\n",
    "    return fact\n",
    "\n",
    "def binomial(n,p):\n",
    "    if 0<=p<=n:\n",
    "        return factorielle(n)//(factorielle(p)*factorielle(n-p))\n",
    "    else:\n",
    "        return 0\n",
    "\n",
    "def maxBinomial(n):\n",
    "    maxi=1\n",
    "    for p in range(1, n+1):\n",
    "        b=binomial(n, p)\n",
    "        if b>maxi:\n",
    "            maxi=b\n",
    "    return maxi\n",
    "\n",
    "def verifMaxBinomial(n):\n",
    "    return maxBinomial(n)==binomial(n, n//2)\n",
    "\n",
    "def pascal(n, p):\n",
    "    return binomial(n+1,p+1)==binomial(n,p)+binomial(n,p+1)\n",
    "    \n",
    "N=100\n",
    "\n",
    "reglePascal=True\n",
    "\n",
    "for n in range(N):\n",
    "    for p in range(N):\n",
    "        if not pascal(n,p):\n",
    "            reglePascal=False\n",
    "\n",
    "print(\"reglePascal pour N = \",N,\" : \",reglePascal)\n",
    "\n",
    "for n in range(1,25):\n",
    "    print(\"verif Max binomial pour n = \",n,\" : \",verifMaxBinomial(n))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 1
}
