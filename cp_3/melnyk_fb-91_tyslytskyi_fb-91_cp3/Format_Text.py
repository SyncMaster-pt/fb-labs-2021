import re

def text_format(file_name, gaps = True):
    with open(file_name, encoding="utf8") as file:
        text_str = file.read()
        file.close()
    lower_text = text_str.lower()
    #print(lower_text)
    if (gaps == True):
        ready_text = re.sub(r'[^а-яё ]', '', lower_text)
    else:
        ready_text = re.sub(r'[^а-яё]', '', lower_text)
    #print(ready_text)

    file_to_write = open('format_text.txt', 'w')
    file_to_write.write(ready_text)
    file_to_write.close()

if __name__ == '__main__':
    text_format('text.txt', False)