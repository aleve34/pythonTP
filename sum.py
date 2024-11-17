def additionner(arg1, arg2):
    """
    Additionne deux nombres et retourne le résultat.

    :param arg1: Premier nombre à additionner (float)
    :param arg2: Deuxième nombre à additionner (float)
    :return: La somme de arg1 et arg2 (float)
    """
    return arg1 + arg2

def main():
    """
    Fonction principale qui appelle 'additionner' avec des valeurs d'exemple.
    Elle affiche également le résultat dans la console.
    """
    result = additionner(5, 10)
    print(f"Le résultat de l'addition est : {result}")
    
if __name__ == '__main__':
    main()
