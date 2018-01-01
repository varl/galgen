def build_list(elements):
    htmlList = []
    htmlList.append('<ul>')
    for el in elements:
        htmlList.append('<li>')
        htmlList.append('<div>')
        htmlList.append('<a href="'+el[0]+'"><img src="'+el[1]+'"></a>')
        htmlList.append('<div>')
        htmlList += build_exif_list(el[2])
        htmlList.append('</div>')
        htmlList.append('</div>')
        htmlList.append('</li>')
    htmlList.append('</ul>')
    return htmlList

def build_exif_list(exif):
    exifList = []
    
    exifList.append('<dl>')
    for k, v in exif.items():
        exifList.append('<dt>')
        exifList.append('{}'.format(k))
        exifList.append('</dt>')
        exifList.append('<dd>')
        exifList.append('{}'.format(v))
        exifList.append('</dd>')

    exifList.append('</dl>')
    return exifList

def build_doc(path, images):
    doc = []
    doc.append('<!doctype html>')
    doc.append('<meta charset="utf-8">')
    doc.append('<meta name="viewport" content="width=device-width,initial-scale=1">')
    doc.append('<title></title>')
    doc += build_css()
    doc.append('<article>')
    doc += build_list(images)
    doc.append('</article>')
    doc.append('<script type="text/javascript" src="main.js"></script>')
    return ''.join(doc)

def build_css():
    css = []
    css.append('<style>')
    css.append('body { background-color: #181818; }')
    css.append(('ul { list-style:none;'
                'display: flex;'
                'flex-direction:row;'
                'flex-wrap: wrap;'
                'padding: 0;'
                'margin: 0;'
                'justify-content: center;'
                'align-content: space-around;'
                '}'))
    css.append(('li {'
                'margin: 0.2em;'
                'border-collapse: collapse;'
                '}'))
    css.append(('li > div {'
                'display: flex;'
                'flex-direction: row;'
                'flex-wrap: wrap;'
                '}'))
    css.append(('li > div > div {'
                'padding: 1em;'
                'color: #efefef;'
                'font-family: monospace;'
                'font-size: 16px;'
                '}'))
    css.append('dt { font-weight: 600; color: rebeccapurple; }')
    css.append('a { border: 0.2em solid orange; display: inline-flex; }')
    css.append('a:hover { border: 0.2em solid rebeccapurple; }')
    css.append('img { max-width: 100%; max-height: 100%; }')
    css.append('</style>')
    return css

