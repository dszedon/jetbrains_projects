lst_formatter = ['plain', 'bold', 'italic', 'inline-code', 'link', 'header', 'new-line']
special_commands = ['!done', '!help']
mrk_dwn = ""

print('$ python markdown-editor.py')

while True:
    formatter = str(input('- Choose a formatter: '))

    if formatter not in lst_formatter and formatter not in special_commands:
        print('Unknown formatting type or command. Please try again')
    else:
        if formatter == '!help':
            print('Available formatters: plain bold italic link inline-code header ordered-list unordered-list line-break')
            print('Special commands: !help !done')
        elif formatter == '!done':
            quit()
        elif formatter == lst_formatter[0]:
            txt = input('- Text: ')
            mrk_dwn = mrk_dwn +  txt
        elif formatter == lst_formatter[1]:
            txt = input('- Text: ')
            mrk_dwn = mrk_dwn + f'**{txt}**'
        elif formatter == lst_formatter[2]:
            txt = input('- Text: ')
            mrk_dwn = mrk_dwn + f'*{txt}*'
        elif formatter == lst_formatter[3]:
            code = input('- Text: ')
            mrk_dwn = mrk_dwn + f'`{code}`'
        elif formatter == lst_formatter[4]:
            label = input('- Label: ')
            url = input('- URL: ')
            mrk_dwn = mrk_dwn + f'[{label}] ({url})\n'
        elif formatter == lst_formatter[5]:
            level = int(input('- Level: '))
            txt = input('- Text: ')
            mrk_dwn = mrk_dwn + '#'*level + f' {txt}' + '\n'
        elif formatter == lst_formatter[6]:
            mrk_dwn = mrk_dwn + "\n"
    
    if formatter == lst_formatter[3]:
        print(f'`{code}`')
    else:
        print(mrk_dwn)
            
            
        
