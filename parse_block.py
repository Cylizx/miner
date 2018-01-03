#!/usr/bin/env python3
import os,json,time
def gen_transaction_html(tr_hash):
    with open('transaction/' + tr_hash + '.json','r') as t:
        tr = json.load(t)
        with open('transaction/'+tr_hash+'.html','w') as f:
            f.write('<html><body><h1>Transaction hash: '+tr_hash+'</h1>')
            for key in tr.keys():
                f.write('<p>'+key+': '+str(tr[key])+'</p>')
            f.write('<a href="/index.html">Back</a>')
            f.write('</body></html>')

def gen_block_html(block_hash):
    with open('block/'+block_hash+'.json','r') as b:
        block = json.load(b)
    with open('block/'+block_hash+'_tlist.json','r') as l:
        tr_list = json.load(l)
    with open('block/'+block_hash+'.html','w') as f:
        f.write('<html><body><h1>Block hash: '+block_hash+'</h1>')
        for key in block.keys():
            if key == 'prev_hash':
                f.write('<p>'+key+': <a href="/block/'+str(block[key])+'.html">'+ str(block[key])+'</a></p>')
            else:
                f.write('<p>'+key+': '+str(block[key])+'</p>')
        f.write('<h2>Transaction List:</h2>')
        for tr_hash in tr_list :
            f.write('<p><a href="/transaction/'+tr_hash+'.html">'+tr_hash+'</p></a>')
            gen_transaction_html(tr_hash)
        f.write('<p><a href="/index.html">Back</a></p>')
        f.write('</body></html>')
    return block['prev_hash']

def gen_index_html():
    latest_hash = ""
    while True:
        time.sleep(5)
        with open('block/head.json','r') as f:
            block_hash = json.load(f)[0]
        if block_hash == latest_hash:
            continue
        else:
            latest_hash = block_hash
            gen_block_html(block_hash)
            os.rename('block/'+block_hash+'.html','index.html')
            prev_hash = block_hash
            while prev_hash != 'aaa':
                prev_hash = gen_block_html(prev_hash)
                try:
                    os.stat('block/'+prev_hash+'.html')
                except:
                    continue
                break
        print('Finish check')



    

if __name__ == '__main__' :
#    gen_block_html('000001edbbdf21fa4d9ec0f9b437d0dcb2d62984845828259104f814c4ab2cd1')
    gen_index_html()
            
            

