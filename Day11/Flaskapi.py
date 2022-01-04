from flask import Flask, jsonify
app = Flask(__name__)
@app.route('/horoscope/<string:n>')
def horo(n):
    import urllib.request
    from bs4 import BeautifulSoup as bs
    import re
    import pandas as pd    

    page = urllib.request.urlopen("https://www.horoscope.com/us/index.aspx")
    soup = bs(page)

    names = soup.body.findAll('a')
    function_names= re.findall('id="src-hp-.\w+',str(names))
    function_names=[item[11:] for item in function_names]

    description=soup.body.find_all('p')
    function_usage=[]

    for item in description:
     item=item.text
     item=item.replace('/n','')
     function_usage.append(item)
    s = 0

    for i in range(0,12):
        if function_names[i] == n:
            s = i


    date = function_usage[:12]
    data = {'Zodiac': function_names[s], 'Date': date[s]}
    
    
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)


