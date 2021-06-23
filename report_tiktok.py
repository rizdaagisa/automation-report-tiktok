import requests
def report():
	url = "https://www.tiktok.com/node/report/reasons_put?aid=1988&app_name=tiktok_web&device_platform=web&referer=https:%2F%2Fwww.google.com%2F&root_referer=https:%2F%2Fwww.google.com%2F&user_agent=Mozilla%2F5.0+(Windows+NT+10.0%3B+Win64%3B+x64)+AppleWebKit%2F537.36+(KHTML,+like+Gecko)+Chrome%2F87.0.4280.88+Safari%2F537.36&cookie_enabled=true&screen_width=1000&screen_height=900&browser_language=en-US&browser_platform=Win32&browser_name=Mozilla&browser_version=5.0+(Windows+NT+10.0%3B+Win64%3B+x64)+AppleWebKit%2F537.36+(KHTML,+like+Gecko)+Chrome%2F87.0.4280.88+Safari%2F537.36&browser_online=true&ac=4g&timezone_name=Asia%2FBangkok&page_referer=https:%2F%2Fwww.tiktok.com%2Fen%2F&priority_region=ID&verifyFp=verify_kivz0y7z_If1PClcn_v5o9_4yfb_9JTO_PhZwwx9lb448&appId=1180&region=ID&appType=t&isAndroid=false&isMobile=false&isIOS=false&OS=windows&did=6905337879108290050&tt-web-region=ID&uid=6785869228451316738"
	headers = { 'accept': 'application/json, text/plain, */*',
'accept-encoding': 'gzip, deflate, br',
'accept-language' : 'en-US,en;q=0.9,id;q=0.8',
'content-length': '104',
'content-type' : 'application/json',
'cookie': 'tt_webid_v2=6905337879108290050; tt_webid=6905337879108290050; ttwid=1%7CV_3s1PMcB2GdoEr5k8ju2apH1QXD5YsxiecIqLxD6rI%7C1607774273%7C36ada7bd9ec35857ba8ff6bf07df7055d7a9269f617d19d77c888d7d5f99a9b6; passport_csrf_token=e203ba2c4911fd5d5f592ccc0b509708; odin_tt=ba283be0998971301498f4a25f332ad2e21e29096aa58044ec98696ba4a2fd14c9743f16a4d65852efec30edb9f20b6fcb8f5fa50be0ebad4057e258ab94248f; passport_auth_status=62c6c03a04dbe01ad17b542f5123f5d5%2C; passport_auth_status_ss=62c6c03a04dbe01ad17b542f5123f5d5%2C; sid_guard=d696b7323dc877533826155bf047c259%7C1607774284%7C5184000%7CWed%2C+10-Feb-2021+11%3A58%3A04+GMT; uid_tt=115603fd8da6fdafbe335fa03b05a2427573a89d1d52f97c785c6c68083fe554; uid_tt_ss=115603fd8da6fdafbe335fa03b05a2427573a89d1d52f97c785c6c68083fe554; sid_tt=d696b7323dc877533826155bf047c259; sessionid=d696b7323dc877533826155bf047c259; sessionid_ss=d696b7323dc877533826155bf047c259; store-idc=alisg; store-country-code=id; MONITOR_WEB_ID=97e54c0c-6f65-4598-a151-febacb6123b9; tt_csrf_token=xetdwEu-Vb8-UvXmw-YZF0pX; s_v_web_id=verify_kivz0y7z_If1PClcn_v5o9_4yfb_9JTO_PhZwwx9lb448',
'origin': 'https://www.tiktok.com',
'referer': 'https://www.tiktok.com/@maheswarashima/video/6905679425136856322?lang=en',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-origin',
'tt-csrf-token': 'xetdwEu-Vb8-UvXmw-YZF0pX',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
	}
	payload = {"reason":1001,"object_id":"6905679425136856322","owner_id":"6878137083081802753","report_type":"video"}
	with requests.Session() as s:
		r=s.post(url,data=payload,headers=headers)
		print(r)

report()