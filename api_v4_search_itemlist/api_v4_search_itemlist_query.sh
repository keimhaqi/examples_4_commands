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
            "type":"article",
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
    "params":[
        {
            "user":"0",
            "from":0,
            "num":1000,
            "searchword":"nike",
            "articleFilter":[],
            "type":"product",
            "language":"en"
        }
    ],
    "num":1000
}
' http://localhost:9124/api/v4/search/itemlist



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