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
' http://localhost:9124/api/v4/search/itemlist



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
    "num":10,
    "searchword":"goose",
    "articleFilter":[],
    "type":"article",
    "language":"en"
}
' http://localhost:9124/api/v4/search/itemlist/product


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
    "vendorId": 37731,
    "attributeValueIds": "1240911,2681349,1318669,1388896"
}
' http://localhost:9124/api/v4/search/itemlist/productbygroup


curl -k -H 'Content-Type: application/json' -d '
{
    "minOff": 55,
    "minPrice": 25,
    "maxPrice": 55,
    "spuList": ["ww4xo1l","ey2x5c6a","p7o4acpa","jdw4vf7a","ryd4rc7ap","2g2dah99g","gya4jcn9l","ryd4rc9o9","9qpe6sylv","v72l6cjq6","nqy4vsdev","ww4xo1q2q","9qpe6syd6","nqy4vs27o","v72l6ck72","xra2xs8rl","ww4xo1n3l","ey2x5ckrg","lrp4aselq","47arqce5k","qw52e17","6k7w6fwl","ryd4rcw5","gya4jcly","ey2x5cww","ww4xo127","6k7w6fgg6","nqy4vsn2d","p7o4ac2re","gya4jcv8e","jdw4vf8ej","7pw8kt997","8q8pdsnn2","gya4jc7d7","2g2dahdgl","nqy4vso","p7o4acw","qw52e1d7","lrp4as2d","xra2xsax","jdw4vf36","ww4xo1p5x","ypq2yt7lg","3k46efpgg","ryd4rc9jr","ww4xo1q5a","apd5wtnkw","ryd4rc28k","gya4jc77w","lrp4as2n4","nqy4vsg7l","ey2x5c42d","nqy4vsgpx","5wq7d13ww","3k46ef8j","p7o4acra","8q8pds35","p7o4acn4","5wq7d194","dnvrecno5","3k46ef9r9","nqy4vsy4n","nqy4vsy3q","jdw4vf669","8q8pdsv7j","5wq7d1p6v","7pw8ktejl","8q8pdsnpd","lrp4as2ye","5wq7d1va7","ypq2ytgd5","apd5wtrx9","8q8pds58e","lrp4asqlp","ypq2yte8","ey2x5crq","5wq7d1wp","5wq7d1ydp","lrp4asjjw","nqy4vsy2l","9qpe6s5o4","v72l6cr5j","8q8pdsn4p","2g2dahdvv","8q8pdsn25","gya4jc38x","ryd4rcayo","ong4ecrxx","7pw8kt2ay","lrp4ase53","v72l6c2","jdw4vfr6q","jdw4vfr2p","2g2dahnaj","qw52e1dae","qw52e1878","5wq7d1q7g","apd5wtnxv","apd5wtq38","gya4jc7yo","3k46efdl9","ryd4rcav7","7pw8kt2on","7pw8kt85","ypq2ytv5","nqy4vsxy","7pw8ktkj","ww4xo1g7","qw52e1kx","jdw4vfrkp","9qpe6s547","ey2x5c6dd","2g2dahnka","ypq2ytrvo","lrp4as6go","ryd4rc94r","ey2x5cxxn","5wq7d1qa3","7pw8ktend","v72l6cjv6","6k7w6fw8l","dnvrecdl9","6k7w6fjn9","ww4xo15vg","v72l6ca2","v72l6col","gya4jcjn3","ey2x5c6q5","6k7w6fg9r","7pw8kt8j9","jdw4vf689","nqy4vsn7d","ww4xo1r36","9qpe6syyk","ong4ecnld","47arqcxvv","7pw8kteav","ryd4rcnq3","dnvrecdw2","apd5wtqgn","ryd4rcnyx","apd5wtq84","gya4jc3jk","ong4ecrg6","qw52e1wk5","v72l6cxew","8q8pdsonv","lrp4as4","k984jtg","apd5wtg5","v72l6cya","47arqcro","v72l6ca54","lrp4as665","ryd4rc9ne","2g2dah2eq","gya4jcvrv","ypq2ytg7j","ypq2ytggj","nqy4vs24p","5wq7d1vgj","ryd4rcnkq","qw52e1wnv","2g2dahq5j","nqy4vs7dr","gya4jc878","apd5wtkq2","gya4jc5","3k46ef3d","nqy4vsynl","ryd4rc7ao","xra2xsorq","ong4ecgd5","p7o4ac25e","ong4ecn58","7pw8kte3d","gya4jc7x4","p7o4acjpk","47arqcl53","v72l6c264","9qpe6sodn","2g2dahqr2","7pw8ktdvx","ong4ec593"]
}
' http://localhost:9124/api/v4/screen/itemlist/productbyselector

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