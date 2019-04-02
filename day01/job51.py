import re
import urllib.request


headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
}


url = 'https://search.51job.com/list/040000,000000,0000,00,9,99,python,2,1.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=21&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='

req = urllib.request.Request(url, headers=headers)
response = urllib.request.urlopen(req)

html = response.read().decode('gbk')

jobnum_re = '<div class="rt">(.*?)</div>'
coms = re.compile(jobnum_re, re.S)
strs = coms.findall(html)[0]


num_re = '.*?(\d+).*'
number = re.findall(num_re, strs)

jobname_re = '<div class="el">(.*?)</div>'
joblist = re.findall(jobname_re, strs)
print(joblist)
