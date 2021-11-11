# request-to-bq
httpリクエストの情報をbqにinsertするpythonスクリプト。cloud runで動かします。

# build
docker build -t request_to_bq:001 .
docker tag request_to_bq:001 gcr.io/gtm-pkdzvlm/request_to_bq:001 
docker push gcr.io/gtm-pkdzvlm/request_to_bq:001

# sample request

https://request-to-bq-n2opciuoba-uc.a.run.app/?request_path=/g/collect&event_name=page_view&query_string=v=2&tid=G-JBMXM05KV6&gtm=2oeb80&_p=1027657087&sr=1792x1120&ul=ja&cid=1024693154.1636615067&_fplc=0&_s=1&dl=https%3A%2F%2Fblog-opt-test.55-inc.jp%2F&dt=計測テスト&sid=1636615067&sct=1&seg=0&en=page_view&_fv=1&_nsi=1&_ss=1&ep.referrer=&ep.user_agent=Mozilla%2F5.0%20(Macintosh%3B%20Intel%20Mac%20OS%20X%2010_15_7)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F94.0.4606.81%20Safari%2F537.36&ep.location_href=https%3A%2F%2Fblog-opt-test.55-inc.jp