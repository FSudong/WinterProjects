import sys,re
from txt2html import util

if __name__ == '__main__':
    fileName = "input.txt"
    resultFile = "result.html"
    fileContent = ""
    html = ""
    with open(fileName, "r") as f:
        fileContent = f.read()

    html = html + '<html><body>'

    title = True
    for block in util.blocks(fileContent):
        block = re.sub(r'\*(.+?)\*',r'<em>\1</em>',block)
        if title:
            html += '<h1>'
            html += block
            html += '</h1>'
            title =False
        else:
            html += '<p>'
            html += block
            html += '</p>'

    html += '</body></html>'


    with open(resultFile,'w') as f:
        f.write(html)