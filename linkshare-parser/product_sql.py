tables = [
    "anntayloroutlet",
    # "bestbuy",
    "bloomingdales",
    "dillards",
    "finishline",
    "jet",
    "lastcall",
    "loftoutlet",
    "macys",
    "neimanmarcus",
    "nordstrom",
    "saks_v1",
    "saksoff_v1",
    # "yoox"
]

for item in tables:
    # print("alter table product_sku_{} modify column product_url varchar(2000);".format(item))
    # print("alter table product_sku_{} modify column product_title varchar(1000);".format(item))
    # print("alter table product_sku_{} modify column product_keywords varchar(1000);".format(item))
    # print("alter table product_sku_{} modify column product_image_link varchar(2000);".format(item))
    # print("alter table product_{}_price modify column image_url varchar(2000);".format(item))
    print("alter table product_{}_price add column product_title varchar(1000) default null;".format(item))
    print("\n")