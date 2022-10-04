import json
import folium
from datetime import datetime
from time import sleep
import imgkit
# [{'mmsi': 19000000000, 'ts': 1483434251000, 'lat': 22.46288, 'lon': 91.68675, 'vesselId': '59999999999999999999999'}]
config = imgkit.config(wkhtmltoimage='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltoimage.exe')
options = {'format': 'png', 'width': 670, 'disable-smart-width': ''}

def convert_timestamp(ts :int, tf :int):
    ts = ts/1000
    ts_format = '%Y-%m-%d %H:%M:%SZ'
    if tf == 0:
        ts_format = '%d/%b/%Y %H:%M'

    elif tf == 3:
        ts_format = '%d/%b/%Y %H:%M'

    elif tf == 6:
        ts_format = '%d/%b/%Y %H:%M'

    else:
        ts_format = '%d/%b/%Y %H:%M'


    date_time = datetime.utcfromtimestamp(ts).strftime(ts_format)

    return f"Time: {date_time}"


# def render_all_map():
#
#     with open('datapoints_json.json') as f:
#
#         data = json.load(f)
#         tf = 0
#         # 3 months
#         if data[-1]['ts'] - data[0]['ts'] < 7889229:
#             tf = 0
#         # 3- 6 months
#         elif  data[-1]['ts'] - data[0]['ts'] < 1314871:
#             tf = 3
#
#         # 6-12 months
#         elif data[-1]['ts'] - data[0]['ts'] < 31556926:
#             tf = 6
#
#         # over 12 months
#         else:
#             tf = 12
#
#         m = folium.Map(location=[data[0]['lat'], data[0]['lon']], zoom_start=3)
#         folium.Marker(location=[data[0]['lat'], data[0]['lon']], color="blue", popup=f"{convert_timestamp(data[0]['ts'], tf)}").add_to(m)
#         for i in data[1:7]:
#             folium.Circle(radius=2, location=[i['lat'], i['lon']], color="crimson", fill=False, popup=f"{i['lat']},{i['lon']}").add_to(m)
#         folium.Marker(location=[data[-1]['lat'], data[-1]['lon']], color="blue",popup=f"{convert_timestamp(data[-1]['ts'],tf)}").add_to(m)
#         m.save(f"./html/index_{i['ts']}.html")


def render_single_map():

    with open('datapoints_json.json') as f:

        data = json.load(f)
        tf = 0
        # 3 months
        if data[-1]['ts'] - data[0]['ts'] < 7889229:
            tf = 0
        # 3- 6 months
        elif  data[-1]['ts'] - data[0]['ts'] < 1314871:
            tf = 3

        # 6-12 months
        elif data[-1]['ts'] - data[0]['ts'] < 31556926:
            tf = 6

        # over 12 months
        else:
            tf = 12
        counter = 0
        for x in range(1500,1501):

            counter = x
            print(counter)
            m = folium.Map(location=[data[0]['lat'], data[0]['lon']], zoom_start=3)
            #keep y one item behind
            for y in data[0:counter-1]:
                # path
                folium.Circle(radius=1, location=[y['lat'], y['lon']], color='blue',opacity=0.4, fill=False,
                              popup=f"{convert_timestamp(y['ts'], tf)}").add_to(m)


            folium.Marker(location=[data[x]['lat'], data[x]['lon']], icon=folium.Icon(color="purple"), popup=f"{convert_timestamp(data[x]['ts'], tf)}").add_to(m)

            for i in data[counter:]:
                # first marker
                folium.Marker(location=[data[0]['lat'], data[0]['lon']], icon=folium.Icon(color="blue"), popup=f"START: {convert_timestamp(data[0]['ts'], tf)}").add_to(m)
                # path
                folium.Circle(radius=1, location=[i['lat'], i['lon']], color='#555',opacity=0.4, fill=False, popup=f"{convert_timestamp(i['ts'], tf)}").add_to(m)
                # last marker
                folium.Marker(location=[data[-1]['lat'], data[-1]['lon']],  icon=folium.Icon(color="blue"), popup=f"END: {convert_timestamp(data[-1]['ts'],tf)}").add_to(m)
        filename = f"./html/index_{data[x]['ts']}.html"
        m.save(filename)
        # sleep(10)
        # imgkit.from_file(filename, './html/out.png', config=config, options=options)


def convert_map_to_img():
    pass


def build_video():
    pass


render_single_map()



