def sing(num_bottles):
    #TODO: Add your code to achieve the desired output and pass the challenge. 
    #NOTE: The f String method of String Interpolation does not work. 
    lyrics = []
    for num in range(num_bottles, 0, -1):
        lyrics.append('{num} bottles of beer on the wall, {num} bottles of beer.'.format(num = num))
        lyrics.append('Take one down and pass it around, {num} bottles of beer on the wall.'.format(num = num - 1))
        lyrics.append('')
        
    return lyrics