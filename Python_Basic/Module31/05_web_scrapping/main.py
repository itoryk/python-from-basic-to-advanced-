import re

tags = '<h3 text=r>Latest News</h3><h3 text=v>Useful Links</h3><h3 text=v>Search</h3><h3 text=v>Heading 3</h3>'

print(re.findall(r'<h3 .*?>(.*?)</h3>', tags))


with open('examples.html', 'r') as f:
    text = f.read()



