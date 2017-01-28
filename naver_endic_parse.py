def naver_endic_parse(item):
    resulttext = '';
    type = item.findAll('h3')[0].get_text('', strip=True)
    body = item.findAll('dt', attrs={'class':'meanClass'})
    resulttext += '<'+type+'>\n'
    #if len(head) >= 1:
    #    resulttext += head[0].get_text('', strip=True)
    #    resulttext += '\n'
    if len(body) >= 1:
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
    
