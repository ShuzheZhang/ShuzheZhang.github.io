import re,base64,mimetypes,sys,os
page=sys.argv[1]; out=sys.argv[2]; root=os.path.dirname(page)
html=open(page).read()
css=open('style.css').read()+"\n"+open('post.css').read()
def uri(m):
    p=os.path.join(root,m.group(2)); mt=mimetypes.guess_type(p)[0] or 'application/octet-stream'
    return '%s="data:%s;base64,%s"'%(m.group(1),mt,base64.b64encode(open(p,'rb').read()).decode())
html=re.sub(r'(src|poster)="((?:media|figures)/[^"]+)"',uri,html)
html=re.sub(r'<link rel="stylesheet" href="\.\./\.\./style\.css">\s*<link rel="stylesheet" href="\.\./\.\./post\.css">','<style>\n'+css+'\n</style>',html)
head=re.search(r'<head>(.*?)</head>',html,re.S).group(1); body=re.search(r'<body>(.*?)</body>',html,re.S).group(1)
head=re.sub(r'\s*<meta charset[^>]*>|\s*<meta name="viewport"[^>]*>','',head)
open(out,'w').write(head.strip()+'\n'+body.strip()+'\n'); print(out, os.path.getsize(out))
