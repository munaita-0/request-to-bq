# request-to-bq
httpリクエストの情報をbqにinsertするpythonスクリプト。cloud runで動かします。

# build
docker build -t request_to_bq:001 .
docker tag request_to_bq:001 gcr.io/gtm-pkdzvlm/request_to_bq:001 
docker push gcr.io/gtm-pkdzvlm/request_to_bq:001