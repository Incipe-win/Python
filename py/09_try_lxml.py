from lxml import etree

text = """<meta http-equiv="content-type" content="text/html; charset=UTF-8"/>
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <meta name="keywords" content="Online Judge, vjudge, OJ, Virtual Judge, Replay Contest, ICPC, OnlineJudge, JudgeOnline, Coding, Algorithm, ç«èµ, ç®æ³, POJ, ZOJ, UVALive, SGU, URAL, HUST, SPOJ, HDU, HYSBZ, UVA, CodeForces, Z-Trening, Aizu, LightOJ, UESTC, NBUT, FZU, CSU, SCU, ACdream, CodeChef, CF::Gym, OpenJudge, Kattis, HihoCoder, HIT, HRBUST, EIJudge, AtCoder, HackerRank, 51Nod" />
        <meta name="author" content="chaoshxxu" />
        <meta name="robots" content="index, follow" />
        <link rel="shortcut icon" href="/static/images/logo.ico" />
        <link rel="stylesheet" type="text/css" href="/static/bundle/vendor.e3a31bdeb78251ccb839.css" />
        <link rel="stylesheet" type="text/css" href="/static/bundle/app.aece4150ea939365b39c.css" />
            <title>HNCU2020ACM热身 - Virtual Judge</title>
            <meta property="og:url" content="https://vjudge.net/contest/374471"/>
            <meta property="og:type" content="website"/>
            <meta property="og:title" content="HNCU2020ACM热身 - Virtual Judge"/>
            <meta property="og:description" content="Contest [HNCU2020ACM热身] in Virtual Judge"/>
            <meta property="og:image" content="https://vjudge.net//static/images/logo.ico"/>
        </head>"""

html = etree.HTML(text)
print(html)
# print(etree.tostring(html).decode())
ret = html.xpath("/html/head/link/@href")
print(ret)
