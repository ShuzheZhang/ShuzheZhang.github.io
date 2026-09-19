import re,base64,mimetypes,sys
out_path=sys.argv[1]
html=open('index.html').read(); css=open('style.css').read()
def uri(m):
    attr=m.group(1); p=m.group(2); mt=mimetypes.guess_type(p)[0] or 'application/octet-stream'
    return '%s="data:%s;base64,%s"'%(attr,mt,base64.b64encode(open(p,'rb').read()).decode())
html=re.sub(r'(src|poster)="(assets/[^"]+)"',uri,html)
html=html.replace('<link rel="stylesheet" href="style.css">','<style>\n'+css+'\n</style>')
head=re.search(r'<head>(.*?)</head>',html,re.S).group(1); body=re.search(r'<body>(.*?)</body>',html,re.S).group(1)
head=re.sub(r'\s*<meta charset[^>]*>|\s*<meta name="viewport"[^>]*>','',head)
open(out_path,'w').write(head.strip()+'\n'+body.strip()+'\n'); print(out_path)
