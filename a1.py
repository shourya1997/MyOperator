import re

if __name__ == "__main__":
    
    log_file_path = input()
    
    # ignore line
    ignore_line = r'^Customer Support: Hello, In case you need any help, I am right here. :\)'  # regex of line 
    ignore_line_reg = re.compile(ignore_line)

    # Extracting visitors to identify context
    author = r'^.*?:'
    author_reg = re.compile(author)

    visitor = r'^Visitor.\d+:'
    visitor_reg = re.compile(visitor) # Extracting 'Visitor XXXXX'

    visitor_number = r'\d+:$'
    visitor_number_reg = re.compile(visitor_number) # Extracting 'XXXXX'

    # Extracting dialogue from lines
    dialogue = r':.*'
    dialogue_reg = re.compile(dialogue)

    author_temp = ''
    visitor_temp = 0
    convo = ''
    m=[]
    with open(log_file_path, 'r') as file:
        for line in file:
            dialogue = ''
            if ignore_line_reg.match(line) == None:
                
                author = author_reg.match(line).group(0)
                # print(author)
                # visitor = visitor_reg.match(author).group(0)
                # visitor = visitor_number_reg.findall(visitor)
                # visitor = ''.join(visitor)
                # visitor_number = int(visitor[:-1])

                dialogue = dialogue_reg.findall(line)
                dialogue = ''.join(dialogue)
                dialogue = dialogue[1:]

                if author_temp == '':
                    author_temp = author
                    convo = '' + dialogue
                elif author == author_temp:
                    convo = convo + dialogue + ', '
                elif author != author_temp:
                    author_temp = author
                    if convo != '':
                        convo = convo + ':::' + dialogue
                    else:
                        convo = convo + dialogue + ', '

                    m.append(convo)                        
                    convo=''
            else:
                # print("ignored line")
                continue

f = open("q1.txt", "w")
s=''
for i in m :
    s+=i+'\n'
f.write(s)
f.close()