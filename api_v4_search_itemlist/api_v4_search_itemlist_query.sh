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
            "searchword":"Manolo Blahnik Hangisi Crystal-Buckle Satin Flat",
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
    "num":500,
    "searchword":"nike",
    "language":"en",
    "blacklist": [651651,712362]
}
' http://96.90.248.211:9124/api/v4/search/itemlist/product


curl -k -H 'Content-Type: application/json' -d '
{
    "user":"230",
    "searchword":"nike",
    "num":8,
    "language":"en",
    "blacklist":[591323,508248,743864,1918717,1919356,1442614,3302464,3941002,7175960,3711640,3475143,16585,975349,980694,1928462,1932952,1951242,1460916,2866178,3406714,3406715,1959606,3299812,7201556,3939291,3939896,326639,1917766,1917798,1917871,1918668,1918709,1918753,1918765,1921373,1953643,1953654,1954483,928218,1289566,724575,3309392,3294723,2688850,2729189,2432476,1969333,3939906,377704,11888,534945,1918681,1919387,724330,724440,743835,1083878,1442517,2329259,1959615,1959616,1959629,3481299,3939867,3941135,3498392,55252,7005,30103,373506,530094,724464,724534,743820,805199,3406713,3406716,7174356,724334,733305,2698466,1952733,733224,2697330,2698770,445445,1918762,2701175,3481975,3476283,1918715,32439,611302,2699232,7115838,3405243,3403949,3398144]
}' http://96.90.248.211:9124/api/v4/search/itemlist/product


curl -k -H 'Content-Type: application/json' -d '
{
    "user":"0",
    "num":50,
    "searchword":"Saint laurent",
    "language":"en"
}
' http://localhost:9124/api/v4/search/itemlist/product




curl -k -H 'Content-Type: application/json' -d '
{
    "productId4":3514632,
    "vendorId":3
}
' http://96.90.248.211:9124/api/v4/metrics/product



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
    "attributeValueIds": "1334385,907698,1806691,907697"
}
' http://96.90.248.211:9124/api/v4/search/itemlist/productbygroup



curl -k -H 'Content-Type: application/json' -d '
{
    "vendorId": 1237,
    "attributeValueIds": "1334385"
}
' http://localhost:9124/api/v4/search/itemlist/productbygroup




curl -k -H 'Content-Type: application/json' -d '
{
    "vendorId": 1237,
    "attributeValueIds": "1334927,1334385"
}
' http://localhost:9124/api/v4/search/itemlist/productbygroup



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
' http://96.90.248.211:9124/api/v4/search/itemlist/productbygroup



screenConditionHandler4Digit("productSaleValue.min", "productSaleValue.max", minPrice, maxPrice, searchQueryHelper);
        screenConditionHandler4Digit("productDiscountValue.min", "productDiscountValue.max", minOff, minOff, searchQueryHelper);



curl -k -H 'Content-Type: application/json' -d '
{
    "minOff": 0,
    "spuList": ["pj45f68p","rq49ik2wp","6ow4fdqod","yr2j0wva8","2od9fjo6r","yr2j0k93a","3o6rfr42","wjxafdx4","8wp7tdqy","5k72tejl","o64o0eal","6ow4fggv","3o6rfw8","rq49i88r","778af9lr","kn4pu7p7","kn4pu5wx","yr2j0x88","x523f4n","98ewsdg","lj4ef2p4","an5lupn66","6ow4f5rn","pj45fkol","vjl4fkg2","o64o0kw8","an5luqd8","x523flvp","4dr6sgeo","qn2dueje","qn2duje3","yr2j0493","d9rlfjrx","g94kfjyr","778afyaql","g94kfl85v","rq49ij2dl","d9rlf28jl","2od9f2oq","n64g0k46","4dr6s5gw","an5lu7a6","o64o0nkd","vjl4f9e4","n64g0aep","2od9folyq","pj45frkp","qn2du9g","vjl4fga9","2od9f57n","3o6rf8pr","lj4ef5ykw","kn4puxdor","g94kflagk","n64g0jweo","3o6rf27n6","rq49iexee","n64g0477","j948frqyaa","5k72t3q4","j948fvdq","qn2du879","x523fr4g","n64g0q84","d9rlf99","5k72tkj","98ews84p","e9x6fn42","lj4efjyk","wjxafy62l","kn4pu9q4w","778af3ega","n64g0lokx","x523flr7","4dr6sp29","qn2dun34","lj4ef6q5","pj45f4gd","vjl4f3dp","n64g07nx","o64o0a2w","6ow4fkgl","d9rlfaoj","8wp7tj6x","qn2du7vx","d9rlf8w28","j948fqvpq","6ow4fl72k","g94kfdww","yr2j0yg7","kn4pukl6","j948f8lo","3o6rf8x6","vjl4fr7y","n64g0we4","5k72tekl","j948f2we","yr2j0qwg","kn4puay","778af7xd","yr2j09nkv","qn2du7ng","an5lugx9","3o6rfl4x","n64g0d9v","g94kfogq","e9x6fxo9","n64g0x8g","yr2j0qr5","yr2j0g8p","yr2j0dlwp","98ewsq46","6ow4f8v6","wjxafplj","wjxafqqr","wjxafpa5","2od9fdn","qn2du2o","n64g0axk","pj45f8vrx","g94kf65o3","qn2dua22d","j948fqyyw","3o6rfgnnl","n64g02op","g94kfqep","2od9fd9p","d9rlfaaj","j948fv26","98ews8dx","yr2j057r","rq49i8ek","8wp7tn2p","e9x6fxx4","2od9faap","4dr6svlp5","kn4pu9dda","vjl4f75e","qn2du7eg","5k72tqk3","d9rlfd2p","rq49i6de","rq49iykav","4dr6s395r","n64g0j48r","778afl6wq","x523fo45nw","j948fwl2","yr2j0xgr","vjl4f8a","an5luk9g","2od9f86g","8wp7t56","x523fo79","o64o09pj"]
}
' http://localhost:9124/api/v4/screen/itemlist/productbyselector



curl -k -H 'Content-Type: application/json' -d '
{
    "uniqueIdList": [1416,1427,1429,1444,1445,1456,1477,1479,1487,1516,1543,1600,1604,1618,1619,1417,1418,1423,1432,1451,1459,1463,1478,1492,1495,1526,1528,1547,1562,1565,1567,1602,1606,1433,1449,1474,1481,1489,1509,1511,1551,1558,1559,1571,1578,1583,1590,1605,1413,1414,1421,1422,1435,1440,1460,1471,1476,1482,1496,1502,1522,1544,1560,1584,1589,1599,1608,1611,1613,1431,1453,1462,1468,1470,1472,1473,1490,1512,1529,1534,1538,1545,1550,1553,1570,1579,1580,1588,1594,1597,1601,1610,1612,1409,1426,1437,1441,1454,1484,1485,1491,1498,1505,1507,1515,1519,1575,1581,1592,1607,1616,1410,1411,1412,1415,1425,1430,1439,1450,1483,1493,1497,1499,1510,1513,1521,1532,1541,1548,1549,1555,1556,1561,1569,1572,1585,1586,1591,1603,1609,1615,1434,1436,1446,1447,1457,1458,1466,1467,1486,1500,1504,1506,1514,1517,1520,1524,1525,1527,1546,1573,1582,1598,1614,1419,1442,1448,1452,1455,1465,1469,1475,1503,1518,1531,1536,1537,1539,1540,1542,1554,1557,1563,1564,1566,1576,1593,1595,1617,1420,1424,1428,1438,1443,1461,1464,1480,1488,1494,1501,1508,1523,1530,1533,1535,1552,1568,1574,1577,1587,1596]
}
' http://localhost:9124/api/v4/screen/itemlist/productbyselector




curl -k -H 'Content-Type: application/json' -d '
{
    "minOff": 40,
    "spuList": ["ey5wt6kjp","ryrwt7ne4","k9j6fo598","47qjtgewg","wwogipk8o","ypy5u743j","nqv91y75p","2gajcnawa","7pk6u8j42","apw4ug7nx","gyjptjodd","47qjtg6ge","k9j6feov7","dne7too7o","9q631rgkg","dne7to8wn","nqv91a4j9","k9j6fve8j","ryrwt84ag","k9j6f2x7w","nqv91ky4y","47qjtpg63","7pk6ux84k","qwe7ix8gv","qwe7i7exn","7pk6u6vld","qwe7i7jap","k9j6fqarj","47qjt6pj2","qwe7i7x9a","2gajcw3gq","onert22jk","jdvgcoxkw","9q631la77","wwogio7lj","3kejhnda3","ypy5udwv3","apw4u66x5","47qjt99w4","ypy5u9edp","xrxo0dvv2","3kejh2dvr","47qjtve3r","apw4udvkl","apw4ua72n","6k6jhvk6d","47qjt3k8a","ypy5u6gvl","p7avt9je7","dne7tqj5y","9q631a3lw","k9j6fyvxo","6k6jhnv4y","k9j6fyglj","3kejhkd7l","v76ytv25r","5wdjiglxr","dne7t7axy","k9j6fw274","3kejhkqlw","5wdjiwljy","7pk6uar5d","apw4upo2e","6k6jh4yaq","onertv8w4","qwe7ik4vg","ypy5u2e8r","47qjtg8e6v","p7avtkq4xx","lra50j2v5v","47qjtglv6k","jdvgcrrn33","5wdjiyy4xq","v76ytarwgk","ypy5u7r5nx","ypy5u7rqn6","v76yta2nqv","5wdjiy3aqy","onertgrw5l","jdvgcr4xra","onertgrgd7","ypy5u7ll9l","3kejh9ael3","6k6jhgjw7v","onertg969g","ypy5u7qeyv","9q63154yqk","gyjptjovwv","2gajcn8w9n","47qjtg657y","lra50jo2q2","ryrwt7porj","2gajcnej4y","onertgkxxk","7pk6u8xkwd","2gajcndgd","9q6315r25","wwogip55r","ey5wt6qvo","8qdj1yky3","ey5wt65ql","2gajcnw4w","6k6jhg29g","dne7td3vk","ryrwta6kd","lra50exeo","p7avt6dgd","qwe7iwv84","7pk6u2wk7","v76yt2ope","wwogi5jll","xrxo0dx6d","ypy5u9d9w","9q631kl4g","47qjtved5","wwogiy53x","7pk6u5r4e","5wdji2nyd","2gajcgee3","47qjtkp5v","k9j6fykvq","9q6317vvv","p7avtg9l9","xrxo0xa9p","5wdji8lxl","v76ytn2y3","jdvgclen7","47qjtwr5g","ypy5udgd4","ryrwtwaa2","xrxo05vaa","onertww3q","dne7tkgde","apw4u778j","2gajcw2jn","ey5wtvn73","qwe7i75ga","onert2dd3","dne7tge2a","lra504jkj","p7avtr26y","3kejh8pyr","apw4u7oal","v76ytdkne","ey5wtld7w","wwogiv2yy","5wdjiydx54","apw4ugj2w7","ryrwt7qrvr","47qjtgg9gp","onertg96kk","onertgrg77","qwe7idwvga","qwe7idj8oe","xrxo0owyo7","lra50jj5r2","qwe7ideqor","gyjptj8y2x","2gajcn8any","2gajcn8aj3","p7avtk3l27","ey5wt6nre7","qwe7idx476","jdvgcroyvd","onertglxp7","xrxo0oalv8","8qdj1yr782","8qdj1y3lyd","apw4uge37y","gyjptjprj4","apw4ugvgo","6k6jhgwv8","8qdj1ynqr","2gajcn4o5","v76yta72r","ryrwt7l44","v76yta3gq","qwe7idxpr","3kejh98qw","nqv91y449","9q631o52j","2gajcqqpw","3kejha5ae","47qjtepj7","lra50e478","lra50eo5y","apw4ur6yv","7pk6u2l9e","47qjt4jg2","3kejhy725","ey5wt54r4","xrxo06orx","7pk6ux85k","7pk6ux8oo","5wdjirayv","ey5wtvvol","apw4u73lx","p7avt5475","xrxo09a3k","3kejh74re","nqv914yqx","v76yt3p9e","ryrwtr5qr","gyjptd5de","dne7tplp3","3kejh3vnx","9q631lgon","apw4u8okr","ey5wtpal8","gyjpty4dg","ey5wtppna","lra50dxqg","ypy5u9v38","dne7t87xv","nqv91jdv2","k9j6fjele","nqv91jgjq","k9j6fjryk","ey5wtwj3v","dne7tr34k","ey5wt2kek","5wdjik2vo","gyjptw43l","2gajckkoy","p7avtgdv9","8qdj18eev","8qdj1wkol","6k6jh6q85","p7avtlopg","lra5057dx","qwe7i3l2o","dne7t93e2","9q631gvlk","9q631grx6","gyjpt5794","xrxo0qvdn","wwogiv5jx","8qdj196qq","7pk6u8q2gv","v76ytaenvw","ypy5u7nkkk","ey5wt6gqn8","8qdj1yvd5g","k9j6fo5y76","k9j6fo5ng8","v76yta2eka","lra50jjo8n","k9j6fo8kqj","2gajcnnl6a","6k6jhgglkn","gyjptjj6yj","8qdj1yy9px","onertgaxk4","apw4ugx6wd","5wdjiy86y6","ey5wt6ejj5","lra50jv2ad","nqv91ykrly","ryrwt7y9x3","lra50jk64l","jdvgcro7vq","8qdj1y4aln","dne7tnj58y","9q63153pr4","9q63153pw7","qwe7idnd64","7pk6u8vpwe","qwe7idn5ke","k9j6fo8xke","xrxo0oax5o","47qjtgwp6q","jdvgcrya5a","p7avtvdvd","dne7tvepw","gyjptyad8","dne7tv5k9","lra50wqro","8qdj1e2je","qwe7iardp","ey5wtw86k","7pk6u496n","dne7tq5o7","ey5wt2d5p","47qjtk273","v76yt49v9","v76yt4kl7","dne7t2owj","lra509ro3","2gajcljoo","nqv91r6pr","dne7tnoqn","7pk6u8pvv","9q63154ek","k9j6foqy2","2gajcne3n","47qjtgp2a","lra50jv4g","7pk6u86g8","onert9ogv","47qjtedg2","7pk6u2yqw","qwe7iw2lj","6k6jhj7yx","apw4ur2ge","p7avt6a86","k9j6feaap","ryrwtao3n","xrxo0wd4l","apw4uxkkn","2gajc63pw","apw4u8onr","8qdj123yg","qwe7i26k3","ypy5udlgk","5wdjixgnp","apw4u6635","2gajcw46e","6k6jh8a7g","47qjt62kd","p7avt5r9o","xrxo0967y","wwogi96da","2gajcw94w","qwe7i78nq","3kejh897j","onertjgx6","k9j6fv28x","ypy5uyo7n","8qdj1k47a","dne7t8ype","apw4uondv","xrxo0q8kp","gyjpt5784","onertv9ky","8qdj19a24","2gajcx6x4","onertgqxll","k9j6fo3lpd","dne7tnnaaa","ypy5u77qa7","ryrwt72957","3kejh94dgj","k9j6fo8vwk","gyjptj8pg9","gyjptj3xjy","apw4ugrr83","qwe7idwd29","ypy5u7lg92","5wdjiyvjoa","5wdjiyojrj","qwe7id7x55","7pk6u86xgn","2gajcnwp4y","7pk6u8gll9","dne7tnjr63","k9j6foad7x","lra50j4do6","5wdjiyrae5","5wdjiyrned","lra50j4ovv","2gajcn4e58","5wdjiylkgy","5wdjiyajd3","apw4ug84k4","8qdj1ydd7","apw4ugv7q","gyjptj2wp","ryrwt76pv","apw4ugvj4","3kejh9a2q","qwe7id7na","onertgjdq","xrxo0w849","9q631oe4j","ryrwtaw3k","47qjte474","2gajcq3vp","9q631ope9","9q631opk9","ryrwtaeqx","47qjtevl3","5wdji33x5","3kejh78kg","k9j6fqaxn","ypy5uqvn4","xrxo09a2y","apw4u7vda","v76yt38p5","nqv91kvae","qwe7ixd2g","lra504jdq","jdvgcorqa","v76ytnw6n","dne7tgd3x","2gajca8e3","6k6jh2ek2","v76yt5d5d","apw4u8ax8","v76yt62kk","jdvgcyl97","onertw82d","ey5wtpwen","3kejhvjx2","p7avtv4av","ey5wtydek","p7avtvd45","ey5wtypyy","ey5wty7re","47qjtvaj2","7pk6ulvkl","5wdjikv8o","2gajcjgv7","lra50ar2a","apw4uayqy","47qjt3y33","9q631ayvg","xrxo0gj22","k9j6fywok","5wdjik23o","qwe7ir34j","p7avt9lxg","ypy5u6pl9","lra508vp6","xrxo04qn6","47qjtqny3","9q631donj","5wdji5va9","9q6319gl8","k9j6fxoj3","6k6jh4k3a","5wdjiyddvv","onertgga3x","nqv91yy4yr","apw4ugrg2y","3kejh993ex","9q63155e5x","k9j6fo3dpv","v76ytar8en","7pk6u8xyge","qwe7idxv4d","ypy5u73xvo","p7avtk3qpp","xrxo0ollex","lra50jxnqp","7pk6ul2vo","lra50w8oo","47qjt37gr","6k6jhnj47","ypy5uj6p5","qwe7ialpy","apw4uap28","xrxo0exdk","ypy5u6jll","9q6317x52","ryrwt5ap7","6k6jhlj3x","nqv91r4nx","apw4up7v3","9q6315xq9","apw4ugkd8","xrxo0ow8y","k9j6foaak","apw4urw6a","qwe7iplry","v76ytk46g","jdvgc5p9g","47qjte836","8qdj15awr","qwe7iw28n","7pk6u2y93","8qdj1526a","qwe7iw77y","dne7toja8","3kejhd8ke","5wdji3nqw","lra50ed84","47qjte2yw","qwe7iq8ga","8qdj1rwar","6k6jhe422","ey5wtrwol","47qjtwk9e","ey5wtpkp4","nqv91oyya","xrxo05lyd","3kejhn3l3","47qjt63ox","nqv9144r6","47qjt6pve","9q63143dx","k9j6fq7v2","k9j6fqv7x","dne7tkan3","3kejh7q8e","47qjt6457","6k6jh9p7d","lra50n628","dne7ta3nd","nqv91qly9","apw4u5qly","6k6jh9jj3","47qjtoeyg","p7avt3ajq","onertj5lk","7pk6u6rr2","qwe7iknjn","dne7tl43n","8qdj19pj2","5wdji59lx","dne7tl7wd","gyjptjxvgl","5wdjiydd8x","p7avtkqpxo","ryrwt7qo7q","lra50jld6k","xrxo0oovxd","6k6jhggk6o","lra50jjv5g","dne7tnorrq","ypy5u7lxjp","47qjtge5q6","ypy5u7l97v","k9j6fo5yl9","onertgeadw","ey5wt69n4x","dne7tnn25d","wwogipp4og","v76ytaadkk","8qdj1y339l","v76ytanxkk","qwe7id5naw","wwogip6p4e","3kejh9lwyw","6k6jhgqddr","apw4uge2oe","8qdj1yjxx6","47qjtgoyaq","k9j6fo2jn8","v76ytawp48","3kejh98v3r","2gajcne6we","8qdj1yagpj","7pk6uj2ew","qwe7i67ya","2gajcae2y","ypy5u3735","p7avtrk9n","ypy5u3r5d","apw4u3j9n","k9j6fq2d4","2gajcwekw","2gajcwr5a","gyjptpg54","xrxo0loqd","p7avteq4w","3kejh378d","nqv918xl5","5wdjixneg","nqv9183w8","5wdji6d9o","apw4u2gwg","jdvgcx73r","onert4yww","47qjt2n4y","ey5wtj4qx","gyjptl3rr","apw4udr4j","dne7tnavg","gyjptj22j","3kejh9r2k","qwe7idnpg","gyjptj3qd","apw4ug75d","6k6jhg88y","apw4ug73d","ypy5u7q6w","ryrwt7p7l","jdvgc5noy","6k6jhj7kq","ey5wt4dap","k9j6fedr6","dne7toyg2","dne7ta57v","3kejhq2eg","47qjt3vgq","k9j6f9rd7","apw4u4ary","lra508edp","ryrwt58wd","jdvgcpv6w","dne7t9kad","ryrwtkx86","3kejh5wge","xrxo0qv9x","ypy5u7nvan","ypy5u7nxpo","apw4ugje2k","ey5wt63rw3","k9j6foongl","6k6jhgg4g7","2gajcnqx2w","ey5wt6gdld","ryrwt79kqp","47qjtg6x37","ypy5u7qg38","ryrwt7xy69","nqv91ykx69","2gajcne4a2","2gajcna3jn","apw4ug5qq7","onertgk52w","47qjtg7lnq","3kejh9q8wd","8qdj1y5ajo","gyjptj34ra","gyjptj334j","9q6315va7y","dne7tnalda","8qdj1yjggv","p7avtk4vkr","nqv91ywr54","7pk6u8gr4g","k9j6fo6j4x","47qjtg5l27","47qjtg7wwr","qwe7idqxe9","6k6jhge28w","2gajcn5ejd","ey5wt6rjx9","apw4ugkvp","2gajcn8en","lra50j25n","3kejh9a5g","2gajcnwao","2gajcnweo","ryrwt7xrg","7pk6u865g","apw4uqpwv","9q631r929","7pk6u2knx","6k6jhj35o","47qjte2k4","dne7to87e","v76yt259x","xrxo0w3xn","wwogi58gw","7pk6u2gj7","qwe7ink2v","47qjt4j6g","8qdj1kn8j","2gajcaw3w","jdvgcwvd7","7pk6ujxeg","ypy5uqr57","apw4u7w5x","qwe7i78y3","k9j6fq5vx","xrxo09ep9","8qdj1d4gw","ryrwtxp48","v76yt95od","xrxo062dp","qwe7iqak5","5wdjiagde","p7avtpopd","wwogioxal","ypy5upnp8","7pk6uk4n6","ey5wtd27d","ey5wtyg48","3kejhvk3a","k9j6fj8rj","ey5wtjrej","dne7t2xn6","ey5wtawp4","xrxo07g5y","jdvgcnewj","7pk6u462w","wwogilnop","p7avtxwk7","2gajcjpdg","dne7tq9qn","onertyro3","nqv91edrp","9q6317vew","lra507odj","wwogiv2pg","onertg5wl5","dne7tnwplj","2gajcnq68j","apw4ugr8k9","jdvgcr8w6y","k9j6fovl6k","p7avtkrne9","xrxo0o6dv8","ryrwt7p8qo","6k6jhg522r","xrxo0olndp","qwe7idqx79","7pk6u87x4w","gyjptj9l6l","p7avtk5r7p","lra50j33ew","8qdj1y35xk","xrxo09j4g","ryrwtxgra","qwe7i7r8e","onert2a9q","nqv914a4p","wwogi9965","apw4u739x","2gajcwelo","gyjptopx9","7pk6ux86e","k9j6faolq","ryrwtp7ka","7pk6ugjpn","nqv91a2ld","v76yt7k4y","apw4ueao3","jdvgcleyv","ryrwtrvrk","onert8ge6","apw4u877o","dne7t5lol","ey5wtp4k8","jdvgcx6ko","47qjt957d","47qjt955d","2gajcoo58","apw4u2lj6","wwogiygl3","k9j6foex4","xrxo0o8jw","jdvgcr5q5","ypy5u7qxv","onertg27d","7pk6u8xxv","dne7tonvo","ryrwtn4p8","qwe7iwgve","3kejhdnq5","xrxo0w5ry","apw4ur68l","5wdji36q3","apw4ur2ra","2gajcq37n","2gajcq3l8","9q631opgq","dne7tovdp","gyjpt96n9","47qjt43qv","47qjtnxnn","2gajcldpo","7pk6ua5k8","wwogi4eor","jdvgcqer2","qwe7ia636","qwe7ia58d","qwe7ianxy","wwogiln9g","qwe7irgr8","lra50a5pd","6k6jhnk7o","v76ytq8yk","6k6jho5w8","qwe7iowpd","dne7t7x4k","v76yt83ww","3kejhw4k3","k9j6fx57v","dne7tld3a","3kejhwdjj","apw4uod8e","apw4ugjnqj","wwogipx53q","8qdj1yp29l","qwe7idgv8x","nqv91yvlx2","lra50jjv8o","gyjptjj9ry","ey5wt66erg","wwogip5rr4","apw4ugr6w2","ypy5u7rypk","onertggp85","ryrwt76987","k9j6fo8k7n","lra50jyo84","p7avtk2xen","9q6315xq6w","wwogip9qdd","ey5wt6vxqn","2gajcnw2jq","wwogipapgp","onertgk4gw","gyjptjqdw9","ey5wt6nd58","2gajcne6wq","p7avtkrglx","apw4ug5jej","7pk6u8g9a2","lra50jp4v5","5wdjiyar65","qwe7idqxan","qwe7id43ag","5wdjier4v","2gajcwelw","ypy5u37w6","qwe7inkqv","2gajc5nxw","47qjtwa82","9q631w7nj","47qjt5o7v","9q631llll","qwe7i2wp6","qwe7i2257","qwe7iv4q9","5wdji6xng","onertxj67","5wdjijg6v","jdvgcdj5o","apw4ugka8","dne7tnaer","lra50jvyn","wwogip954","gyjptjo8n","xrxo0o9kd","wwogip96r","47qjtg6wn","ryrwt7xek","7pk6u864g","p7avtkr4r","9q631oyqq","onertr9xp","9q631r2g2","lra50ejxo","ey5wt4p2y","dne7toxq3","jdvgckx7g","47qjtepy7","ey5wt72o7","ryrwtj9lj","ypy5ukjp4","ryrwtgx6d","nqv9165yk","9q6316aoy","2gajcjkpa","apw4ua9l3","3kejhe3vg","jdvgceqk9","6k6jho85r","lra508e43","ey5wtl3ge","gyjpt5xn4","apw4uoqrp","k9j6fx58k","ypy5u2gvj","3kejhwk2x","k9j6fo37wl","2gajcny3y9","lra50je465","apw4ugrvl5","lra50jejd5","k9j6foedor","6k6jhgj3g4","7pk6u82wjg","dne7tnnlpy","5wdjiyda5e","ypy5u7e9qa","47qjtgx27l","k9j6fokpra","nqv91y2vv6","9q6315vd7k","onertgj8av","lra50j4xvd","apw4ug322j","dne7tnpvw6","k9j6fo6aqo","nqv91yxk63","dne7tnj4rx","8qdj1ydxqe","ey5wt6q59v","ey5wt6e42n"]
}
' http://localhost:9124/api/v4/screen/itemlist/productbyselector



curl -k -H 'Content-Type: application/json' -d '
{
    "minOff": 40,
    "spuList": ["dne7to87e", "2gajcnawa"]
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