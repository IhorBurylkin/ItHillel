import codecs, re

def delete_html_tags(html_file="draft.html", result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as infile:
        text = infile.read()

    without_tags = re.sub(r'<[^>]+>', '', text) 
    result = [line + '\n' for line in without_tags.splitlines() if line.strip()]

    with codecs.open(result_file, 'w', 'utf-8') as outfile:
        outfile.write(''.join(result))

delete_html_tags()