# Definieren Sie eine Funktion, die die Benutzereingaben (‚o’=Osten, ‚n’=Norden, ‚w’=Westen, ‚s’=Süden) in eine Positionsangabe ( x | y ) umwandelt
def move_char_by_input(chars, char, input):
    # Konvertieren Sie die Zeichenfolge in eine Liste
    char_list = list(chars)
    # Holen Sie den aktuellen Index des Zielzeichens
    old_index = char_list.index(char)
    # Entfernen Sie das Zielzeichen aus der Zeichenliste
    char = char_list.pop(old_index)
    # Berechnen Sie den neuen Index basierend auf der Benutzereingabe
    if input == 'o': # Osten
        new_index = old_index + 1
    elif input == 'n': # Norden
        new_index = old_index - len(char_list) // 2
    elif input == 'w': # Westen
        new_index = old_index - 1
    elif input == 's': # Süden
        new_index = old_index + len(char_list) // 2
    else: # Ungültige Eingabe oder Programm beenden ('b')
        return None
        # Fügen Sie das Zielzeichen an der neuen Position ein
    char_list.insert(new_index, char)
    # Konvertieren Sie die Zeichenliste zurück in eine Zeichenfolge und geben Sie sie zurück
    return ''.join(char_list)