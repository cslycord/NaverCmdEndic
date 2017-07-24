def naver_endic_parse(item):
    resulttext = '';
    if len(item.findAll('h3')) > 0 :
        #There wass no word class in the search result, the skip    
        type = item.findAll('h3')[0].get_text('', strip=True)
        resulttext += '<'+type+'>\n'
    body = item.findAll('dt', attrs={'class':'meanClass'})    
    for meaning in body:
        mean = meaning.findAll('em')
        for li in mean:
            span = li.findAll('span')
            for s in span:
                classes = dict(s.attrs)['class']
                if classes != ['blind']:
                    resulttext += s.get_text('', strip=True)
            resulttext += '\n'   
    return resulttext
    
