curl -k -H 'Content-Type: application/json' -d '
{
  "whitelist":[14777]
}
' http://192.168.1.104:9124/api/v3/search/brochure/follow

[{"articleId":147,"viewCount":0,"status":2,"userId":23,"inTime":1533630359764,"title":"cs","description":"ssss","content":"[{\"index\":0,\"type\":\"text\",\"jinbagId\":null,\"content\":\"dfdfdfdf\"}]","user":{"id":23,"active":true,"email":"HUIQIAN_HU@JINBAG.COM","nickName":"胡11"}}]


DATA-212 [Searchengine-datasource]以streaming方式接收锦囊信息，把锦囊信息写入搜索系统 -+-+-+> 调整代码，添加以streaming方式接收锦囊，并把锦囊信息写入搜索系统的逻辑