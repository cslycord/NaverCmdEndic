import sys
import naver_endic_parse as parse
import naver_endic_crawler as crawl

if len(sys.argv) > 1:
    results = crawl.naver_endic_crawler(sys.argv[1])
else:
    word = input()
    results = crawl.naver_endic_crawler(word)

if len(results) >= 1:
    for item in results:
        print(parse.naver_endic_parse(item))
else:
    print('no result exists.')
