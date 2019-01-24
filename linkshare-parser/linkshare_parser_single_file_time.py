import json

if __name__ == '__main__':
    parser_point = open("./examples_4_commands/linkshare-parser/linkshare_parser_point_a.json")

    line = parser_point.readlines()

    parser_point_str = ""

    for item in line:
        parser_point_str = parser_point_str + item

    
    parser_point_dict = json.loads(parser_point_str)
    print(parser_point_dict)
    
