curl -k -H 'Content-Type: application/json' -d '
{
  "params":[
    {
      "searchword":"nike",
      "type": "product",
      "blacklist":[]
    },
    {
      "searchword":"nike",
      "type": "article",
      "blacklistItems":[],
      "fields":[
        {"name": "status", "values":[0]}
      ]
    }
  ],
  "num": 15
 
}
' http://96.90.248.211:9124/api/v4/search/itemlist


com.fasterxml.jackson.databind.JsonMappingException:


2019-01-14 07:34:04.980  WARN 164524 --- [eduler_Worker-1] jinbagIO.util.json.JsonMapper            : write to json string error:JobDetail 'traceWhenFinish.6962023_1547391844762':  jobClass: 'jinbagIO.core.service.quartz.JinbagJobTraceFinished concurrentExectionDisallowed: false persistJobDataAfterExecution: false isDurable: true requestsRecovers: false


com.fasterxml.jackson.databind.JsonMappingException: No serializer found for class org.quartz.JobBuilder and no properties discovered to create BeanSerializer (to avoid exception, disable SerializationFeature.FAIL_ON_EMPTY_BEANS) (through reference chain: org.quartz.impl.JobDetailImpl["jobBuilder"])
	at com.fasterxml.jackson.databind.JsonMappingException.from(JsonMappingException.java:275)
	at com.fasterxml.jackson.databind.SerializerProvider.mappingException(SerializerProvider.java:1110)
	at com.fasterxml.jackson.databind.SerializerProvider.reportMappingProblem(SerializerProvider.java:1135)
	at com.fasterxml.jackson.databind.ser.impl.UnknownSerializer.failForEmpty(UnknownSerializer.java:69)
	at com.fasterxml.jackson.databind.ser.impl.UnknownSerializer.serialize(UnknownSerializer.java:32)
	at com.fasterxml.jackson.databind.ser.BeanPropertyWriter.serializeAsField(BeanPropertyWriter.java:704)
	at com.fasterxml.jackson.databind.ser.std.BeanSerializerBase.serializeFields(BeanSerializerBase.java:690)
	at com.fasterxml.jackson.databind.ser.BeanSerializer.serialize(BeanSerializer.java:155)
	at com.fasterxml.jackson.databind.ser.DefaultSerializerProvider.serializeValue(DefaultSerializerProvider.java:292)
	at com.fasterxml.jackson.databind.ObjectMapper._configAndWriteValue(ObjectMapper.java:3672)
	at com.fasterxml.jackson.databind.ObjectMapper.writeValueAsString(ObjectMapper.java:3048)
	at jinbagIO.util.json.JsonMapper.toJson(JsonMapper.java:72)
	at jinbagIO.core.service.quartz.JinbagQuartzService.scheduleJob(JinbagQuartzService.java:180)
	at jinbagIO.core.service.quartz.JinbagQuartzService.addScheduleJobOnSpecificTimeForDiscoverTaskResponseForever(JinbagQuartzService.java:175)
	at jinbagIO.core.service.quartz.JinbagJob.execute(JinbagJob.java:104)
	at org.quartz.core.JobRunShell.run(JobRunShell.java:202)
	at org.quartz.simpl.SimpleThreadPool$WorkerThread.run(SimpleThreadPool.java:573)

 No serializer found for class org.quartz.JobBuilder and no properties discovered to create BeanSerializer (to avoid exception, disable SerializationFeature.FAIL_ON_EMPTY_BEANS) (through reference chain: org.quartz.impl.JobDetailImpl["jobBuilder"])
	at com.fasterxml.jackson.databind.JsonMappingException.from(JsonMappingException.java:275)
	at com.fasterxml.jackson.databind.SerializerProvider.mappingException(SerializerProvider.java:1110)
	at com.fasterxml.jackson.databind.SerializerProvider.reportMappingProblem(SerializerProvider.java:1135)
	at com.fasterxml.jackson.databind.ser.impl.UnknownSerializer.failForEmpty(UnknownSerializer.java:69)
	at com.fasterxml.jackson.databind.ser.impl.UnknownSerializer.serialize(UnknownSerializer.java:32)
	at com.fasterxml.jackson.databind.ser.BeanPropertyWriter.serializeAsField(BeanPropertyWriter.java:704)
	at com.fasterxml.jackson.databind.ser.std.BeanSerializerBase.serializeFields(BeanSerializerBase.java:690)
	at com.fasterxml.jackson.databind.ser.BeanSerializer.serialize(BeanSerializer.java:155)
	at com.fasterxml.jackson.databind.ser.DefaultSerializerProvider.serializeValue(DefaultSerializerProvider.java:292)
	at com.fasterxml.jackson.databind.ObjectMapper._configAndWriteValue(ObjectMapper.java:3672)
	at com.fasterxml.jackson.databind.ObjectMapper.writeValueAsString(ObjectMapper.java:3048)
	at jinbagIO.util.json.JsonMapper.toJson(JsonMapper.java:72)
	at jinbagIO.core.service.quartz.JinbagQuartzService.scheduleJob(JinbagQuartzService.java:180)
	at jinbagIO.core.service.quartz.JinbagQuartzService.addScheduleJobOnSpecificTimeForDiscoverTaskResponseForever(JinbagQuartzService.java:175)
	at jinbagIO.core.service.quartz.JinbagJob.execute(JinbagJob.java:104)
	at org.quartz.core.JobRunShell.run(JobRunShell.java:202)
	at org.quartz.simpl.SimpleThreadPool$WorkerThread.run(SimpleThreadPool.java:573)





curl -k -H 'Content-Type: application/json' -d '
{
    "params":[
        {
            "user":"0",
            "from":0,
            "num":10,
            "searchword":"canada",
            "articleFilter":[],
            "type":"product",
            "language":"en",
            "fields":[
              {"name": "status", "values":[0]}
            ]
        }
    ],
    "num":18
}
' http://96.90.248.211:9124/api/v4/search/itemlist



curl -k -H 'Content-Type: application/json' -d '
{
    "params":[
        {
            "user":"0",
            "from":0,
            "num":10,
            "searchword":"goose",
            "articleFilter":[],
            "type":"article",
            "language":"en"
        }
    ],
    "num":18
}
' http://96.90.248.211:9124/api/v4/search/itemlist



curl -k -H 'Content-Type: application/json' -d '
{
    "user":"0",
    "from":0,
    "num":2,
    "searchword":"goose",
    "articleFilter":[],
    "type":"article",
    "language":"en"
}
' http://96.90.248.211:9124/api/v4/search/itemlist/product


curl -k -H 'Content-Type: application/json' -d '
{
    "params":[
        {
            "user":"0",
            "from":0,
            "num":1000,
            "searchword":"防晒",
            "articleFilter":[],
            "type":"article",
            "language":"en"
        }
    ],
    "num":1
}
' http://96.90.248.211:9124/api/v4/search/itemlist


1240911,2028565,1205717,1388896

1240911,2681349,1318669,9988511


1240911,2681349,1318669,1388896

curl -k -H 'Content-Type: application/json' -d '
{
    "vendorId": 1237,
    "attributeValueIds": "1334385,1633153,1633142,10235459,1633153,4756"
}
' http://96.90.248.211:9124/api/v4/search/itemlist/productbygroup



curl -k -H 'Content-Type: application/json' -d '
{
    "vendorId": 1237,
    "attributeValueIds": "1334927,1334385"
}
' http://96.90.248.211:9124/api/v4/search/itemlist/productbygroup



curl -k -H 'Content-Type: application/json' -d '
{
    "vendorId": 3,
    "attributeValueIds": "907185,1385712,1330585"
}
' http://96.90.248.211:9124/api/v4/search/itemlist/productbygroup


32634


curl -k -H 'Content-Type: application/json' -d '
{
    "vendorId": 3184,
    "attributeValueIds": "32634,1334601,1330623"
}
' http://localhost:9124/api/v4/search/itemlist/productbygroup



screenConditionHandler4Digit("productSaleValue.min", "productSaleValue.max", minPrice, maxPrice, searchQueryHelper);
        screenConditionHandler4Digit("productDiscountValue.min", "productDiscountValue.max", minOff, minOff, searchQueryHelper);



curl -k -H 'Content-Type: application/json' -d '
{
    "minOff": 0,
    "spuList": ["pj45f68p","rq49ik2wp","6ow4fdqod","yr2j0wva8","2od9fjo6r","yr2j0k93a","3o6rfr42","wjxafdx4","8wp7tdqy","5k72tejl","o64o0eal","6ow4fggv","3o6rfw8","rq49i88r","778af9lr","kn4pu7p7","kn4pu5wx","yr2j0x88","x523f4n","98ewsdg","lj4ef2p4","an5lupn66","6ow4f5rn","pj45fkol","vjl4fkg2","o64o0kw8","an5luqd8","x523flvp","4dr6sgeo","qn2dueje","qn2duje3","yr2j0493","d9rlfjrx","g94kfjyr","778afyaql","g94kfl85v","rq49ij2dl","d9rlf28jl","2od9f2oq","n64g0k46","4dr6s5gw","an5lu7a6","o64o0nkd","vjl4f9e4","n64g0aep","2od9folyq","pj45frkp","qn2du9g","vjl4fga9","2od9f57n","3o6rf8pr","lj4ef5ykw","kn4puxdor","g94kflagk","n64g0jweo","3o6rf27n6","rq49iexee","n64g0477","j948frqyaa","5k72t3q4","j948fvdq","qn2du879","x523fr4g","n64g0q84","d9rlf99","5k72tkj","98ews84p","e9x6fn42","lj4efjyk","wjxafy62l","kn4pu9q4w","778af3ega","n64g0lokx","x523flr7","4dr6sp29","qn2dun34","lj4ef6q5","pj45f4gd","vjl4f3dp","n64g07nx","o64o0a2w","6ow4fkgl","d9rlfaoj","8wp7tj6x","qn2du7vx","d9rlf8w28","j948fqvpq","6ow4fl72k","g94kfdww","yr2j0yg7","kn4pukl6","j948f8lo","3o6rf8x6","vjl4fr7y","n64g0we4","5k72tekl","j948f2we","yr2j0qwg","kn4puay","778af7xd","yr2j09nkv","qn2du7ng","an5lugx9","3o6rfl4x","n64g0d9v","g94kfogq","e9x6fxo9","n64g0x8g","yr2j0qr5","yr2j0g8p","yr2j0dlwp","98ewsq46","6ow4f8v6","wjxafplj","wjxafqqr","wjxafpa5","2od9fdn","qn2du2o","n64g0axk","pj45f8vrx","g94kf65o3","qn2dua22d","j948fqyyw","3o6rfgnnl","n64g02op","g94kfqep","2od9fd9p","d9rlfaaj","j948fv26","98ews8dx","yr2j057r","rq49i8ek","8wp7tn2p","e9x6fxx4","2od9faap","4dr6svlp5","kn4pu9dda","vjl4f75e","qn2du7eg","5k72tqk3","d9rlfd2p","rq49i6de","rq49iykav","4dr6s395r","n64g0j48r","778afl6wq","x523fo45nw","j948fwl2","yr2j0xgr","vjl4f8a","an5luk9g","2od9f86g","8wp7t56","x523fo79","o64o09pj"]
}
' http://96.90.248.211:9124/api/v4/screen/itemlist/productbyselector



curl -k -H 'Content-Type: application/json' -d '
{
    "spuList": ["yysp44n","gjs488j","nvs37g6","7kskp6q","2as68w6","e5sd9dv","66sk5jn","gjs48rl","xxso8o4p","lasj3gel","oes5wkej","4qs5d69","66sk5kw","66spd3o9","pask7d24","3es94nqv","66sk584","e5sd9nk","66spvx59","qes8r9ae","66sk594","aws8k72","qes4e7y","7kskpxq","jvs69d9k","2as9gkpp","yysroa6d","5dsp6oaj","jvs32k3","oes8ee5","4qs5d28","pas25e4a","7ks75p6","oes8ejl","kjsg8go","8dsao58","kjsp93p8","pask7rdp","qes4e49","yysp499","kjsdj8o","e5sgyed6","oes5dp4p","xxsonavw","aws8key","las6ggvn","wosr2n4n","rrs9eevl","oes5x982","oes8ell","lasoqva","paseae3","aws8k8y","qes8y2al","oes5dyj9","5dspg56k","lasjg87r","8dsaoaj","66sk5d8","3espkwjl","96s8a932","nvsydg87","kjsokdp5","xxsvkw5","awsgva3w","66spnodg","rrs9e4wv","lasole4","96slx43","96s5vk4p","gjsnkjjk","oesgl7qa","jvs6dnjg","kjspa6pr","5dsp9jyq","rrsd6xy","v6sgx35","nvs374r","gjs48q8","desevew5","kjspqyoq","awsgqg4p","wosok9p","yysp4p3","yys7yw6o","66sgaok6","awsw7747","kjsg8el","3espeo4n","awswyrjv","rrs9en4v","xxspegj5","nvsner2w","xxsla27","awseex7","des56kk","desekox4","jvs6ejr2","gjsnexjl","awsgnx8g","pasea57","oesgld2y","e5sg7559","7ksdl97d","nvsnjy47","7ksd4a5y","awse34v","rrsd6w4","66snv53","nvsyy2jd","gjsnw6oq","awse9ke","2as643y","2as5l95","desno6g8","3es9d9lq","lasp9d3","7kskvd3","lasj873n","oes3y22","awse72g","gjsdloy","lasp8xl","3esxkxw","qes8ydng","8dsvdq72","e5sgjlov","pask7ela","kjs6w64","v6srd77q"]
}
' http://96.90.248.211:9124/api/v4/screen/itemlist/productbyselector



curl -k -H 'Content-Type: application/json' -d '
{
    "spuList": ["ww4xo1l","ey2x5c6a","p7o4acpa","jdw4vf7a","ryd4rc7ap","2g2dah99g","gya4jcn9l","ryd4rc9o9","9qpe6sylv","v72l6cjq6","nqy4vsdev","ww4xo1q2q","9qpe6syd6","nqy4vs27o","v72l6ck72","xra2xs8rl","ww4xo1n3l","ey2x5ckrg","lrp4aselq","47arqce5k","qw52e17","6k7w6fwl","ryd4rcw5","gya4jcly","ey2x5cww","ww4xo127","6k7w6fgg6","nqy4vsn2d","p7o4ac2re","gya4jcv8e","jdw4vf8ej","7pw8kt997","8q8pdsnn2","gya4jc7d7","2g2dahdgl","nqy4vso","p7o4acw","qw52e1d7","lrp4as2d","xra2xsax","jdw4vf36","ww4xo1p5x","ypq2yt7lg","3k46efpgg","ryd4rc9jr","ww4xo1q5a","apd5wtnkw","ryd4rc28k","gya4jc77w","lrp4as2n4","nqy4vsg7l","ey2x5c42d","nqy4vsgpx","5wq7d13ww","3k46ef8j","p7o4acra","8q8pds35","p7o4acn4","5wq7d194","dnvrecno5","3k46ef9r9","nqy4vsy4n","nqy4vsy3q","jdw4vf669","8q8pdsv7j","5wq7d1p6v","7pw8ktejl","8q8pdsnpd","lrp4as2ye","5wq7d1va7","ypq2ytgd5","apd5wtrx9","8q8pds58e","lrp4asqlp","ypq2yte8","ey2x5crq","5wq7d1wp","5wq7d1ydp","lrp4asjjw","nqy4vsy2l","9qpe6s5o4","v72l6cr5j","8q8pdsn4p","2g2dahdvv","8q8pdsn25","gya4jc38x","ryd4rcayo","ong4ecrxx","7pw8kt2ay","lrp4ase53","v72l6c2","jdw4vfr6q","jdw4vfr2p","2g2dahnaj","qw52e1dae","qw52e1878","5wq7d1q7g","apd5wtnxv","apd5wtq38","gya4jc7yo","3k46efdl9","ryd4rcav7","7pw8kt2on","7pw8kt85","ypq2ytv5","nqy4vsxy","7pw8ktkj","ww4xo1g7","qw52e1kx","jdw4vfrkp","9qpe6s547","ey2x5c6dd","2g2dahnka","ypq2ytrvo","lrp4as6go","ryd4rc94r","ey2x5cxxn","5wq7d1qa3","7pw8ktend","v72l6cjv6","6k7w6fw8l","dnvrecdl9","6k7w6fjn9","ww4xo15vg","v72l6ca2","v72l6col","gya4jcjn3","ey2x5c6q5","6k7w6fg9r","7pw8kt8j9","jdw4vf689","nqy4vsn7d","ww4xo1r36","9qpe6syyk","ong4ecnld","47arqcxvv","7pw8kteav","ryd4rcnq3","dnvrecdw2","apd5wtqgn","ryd4rcnyx","apd5wtq84","gya4jc3jk","ong4ecrg6","qw52e1wk5","v72l6cxew","8q8pdsonv","lrp4as4","k984jtg","apd5wtg5","v72l6cya","47arqcro","v72l6ca54","lrp4as665","ryd4rc9ne","2g2dah2eq","gya4jcvrv","ypq2ytg7j","ypq2ytggj","nqy4vs24p","5wq7d1vgj","ryd4rcnkq","qw52e1wnv","2g2dahq5j","nqy4vs7dr","gya4jc878","apd5wtkq2","gya4jc5","3k46ef3d","nqy4vsynl","ryd4rc7ao","xra2xsorq","ong4ecgd5","p7o4ac25e","ong4ecn58","7pw8kte3d","gya4jc7x4","p7o4acjpk","47arqcl53","v72l6c264","9qpe6sodn","2g2dahqr2","7pw8ktdvx","ong4ec593"]
}
' http://localhost:9124/api/v4/screen/itemlist/product

curl -k -H 'Content-Type: application/json' -d '
{
    "spuList": ["ww4xo1l"]
}
' http://localhost:9124/api/v4/screen/itemlist/product

curl -k -H 'Content-Type: application/json' -d '
{
    "params":
    [
        {
            "user":"0",
            "from":0,
            "num":10,
            "searchword":"Canada",
            "blacklist":[10859412,6712504,192270,204327,182354,201722,7679228,204295,205560,199204,178962,179606,179589,6711258,179432,178959,204975,8148076,6825026,2570298,10859170,132314,437061,436906,9312100,10859168,373265,10859338,10859378,129160,129159,129157,10859342,10859340,436920],

            "articleFilter":[],
            "type":"product",
            "language":"en"
        },
        {
            "user":"0",
            "blacklistItems":[1030],
            "from":0,
            "num":10,
            "searchword":"Canada",
            "articleFilter":[],
            "type":"article",
            "language":"en"
        }
    ],
"num":18
}
' http://localhost:9124/api/v4/search/itemlist