import codecs

def delete_html_tags(html_file="draft.html", result_file='cleaned.txt'):
    result = []
    
    with codecs.open(html_file, 'r', 'utf-8') as infile: 
        for line in infile.readlines():
            tags = ''.join([char for char in line if char not in "<>"])
            result.append(tags) if tags.strip() else None

    with codecs.open(result_file, 'w', 'utf-8') as outfile:
            outfile.write(''.join(result))

delete_html_tags()