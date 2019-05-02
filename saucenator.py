import utility as ul

ul.clear()
print(r"""
       _   _            _        _ 
      | | | |          | |      (_)
 _ __ | |_| | ___ _ __ | |_ __ _ _ 
| '_ \|  _  |/ _ | '_ \| __/ _` | |
| | | | | | |  __| | | | || (_| | |
|_| |_\_| |_/\___|_| |_|\__\__,_|_|
                                   
                                   
""")
while True:
    sauce = input("Type in your six magic numbers from reddit:\n")
    numCheckResult = ul.numCheck(sauce)
    if numCheckResult == 'pass':
        lenResult = ul.lengthChecker(sauce, 6)
        if lenResult == 'pass':
            break
        elif lenResult == 'short':
            print('The magic numbers that you put in, are too short. Please try again.')
        elif lenResult == 'long':
            print('The magic numbers that you put in, are too long. Please try again.')

    elif numCheckResult == 'fail':
        print("Only numbers please.")

result = "https://nhentai.net/g/" + sauce + "/"
print("Here's the link. Copied to clipboard\n" + result)
ul.cwopy(result)
ul.anyKey()
