# L3_ISEI_S5-Intelligence_Artificielle

## Parties non fonctionnelles :

Dans ce projet, les points suivants ne sont pas fonctionnels :
<br><br>
### Calcul de x :
La fonction sigmoide est ici l'une des fonction d'activaiton utilisée. Elle s'écrit : 
```
s(x) = 1 / (1 + exp(-x))
```
En observant les résultats de x lors de l'execution du porgramme, on peut constater que x est toujours positif. Or si x est dans l'intervalle [0; +infini], s(x) = 0. On a donc 1 / 1 = 1, donc s(x) renverra toujours 1. <br>
De plus, en appliquant la fonction de la tangeante hyperbolique, une erreur persisite, car x est trop grand pour que la fonction soit calculée.<br><br>
Le calcul de x est donc dans ce programme erroné, faussant ainsi tout l'apprentissage et la déduction de résultats du neurone.
<br><br>
### Mise à jour des poids :
Avant de mettre les poids à jour, il est nécessaire de vérifier si cela est nécessaire. Le calcul de x étant erroné, cette fonctionnalité ne peut pas être testée, et n'a donc pas été implémentée.
<br><br>
### Multicouches :
Ce programme crée autant de couches qu'indiquées dans le fichier de configuration, mais ne permet pas de lier les différentes sorties entre elles. La partie multicouche n'est donc ici pas fonctionnelle.
