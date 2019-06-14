import time
import crawler
import os
import urllib
import tqdm
import json
import urllib.request
import sys

def crawl_and_save(tag, out_path, num=100):
    if not os.path.isdir(out_path):
        os.makedirs(out_path)
        
    data_raw = crawler.get_posts_by_hashtag(tag, num)
    crawler.output(data_raw, os.path.join(out_path, tag + '.json'))

    #print(data_raw)
    i = 1
    for data in data_raw:
        urllib.request.urlretrieve(data['img_url'],os.path.join(out_path,data['img_url'].split('/')[-1].split('.jpg')[0]+'.jpg'))
        print(i,"번째 사진 ",data['img_url'].split('/')[-1].split('.jpg')[0]+'.jpg',"다운로드 완료!")
        i+=1;

if __name__ == '__main__':
    TAG='된장찌개'
    num = 100
    if(len(sys.argv)>=3):
        TAG = str(sys.argv[1])
        num = int(sys.argv[2])
        print("검색어 : ",TAG," 총 ",num,"회")
    else:
        print("매개변수가 없습니다.")
        sys.exit(0)
    out_path='./' + TAG
    st = time.time()
    crawl_and_save(TAG, out_path, num)
    print('tatal time: ', time.time() -st)