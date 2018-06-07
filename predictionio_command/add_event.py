from predictionio import EventClient
import datetime
import pytz
client = EventClient('5h5crmbnZl4_hd-Ob0Ms9Qgm67ConOJWfoxAxtbGo2nKfTELgV0wj7WW0ho3iN7b', "http://localhost:7070", threads=5, qsize=500)

first_event_properties = {
    "prop1" : 1,
    "prop2" : "value2",
    "prop3" : [1, 2, 3],
    "prop4" : True,
    "prop5" : ["a", "b", "c"],
    "prop6" : 4.56 
    }
now_date = datetime.datetime.now(pytz.utc) # - datetime.timedelta(days=2.7)
current_date = now_date
event_time_increment = datetime.timedelta(days= -0.8)
first_event_response = client.create_event(
    event="buy",
    entity_type="user",
    entity_id="10001",
    target_entity_id="2",
    target_entity_type="item"
    # properties=first_event_properties,
    # event_time = current_date
)