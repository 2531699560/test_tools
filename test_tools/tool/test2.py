data = [('POST', 'http://www.omegatimor.top', 'NULL'),
 ('POST', 'http://www.omegatimor.top', 'None'),
 ('POST', 'http://www.omegatimor.top', '""'),
 ('POST', 'http://www.omegatimor.top', '0'),
 ('POST', 'http://www.omegatimor.top', '999'),
 ('POST', 'http://www.omegatimor.top', '500')]
data2="POST,http://www.omegatimor.top,NULL;POST,http://www.omegatimor.top,None;POST,http://www.omegatimor.top" \
      ","";POST,http://www.omegatimor.top,0;POST,http://www.omegatimor.top,999;POST,http://www.omegatimor.top,500;"


import os
os.system('python ./test.py %s'%data2)