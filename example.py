import growattServer
import json
import yaml
import datetime

api = growattServer.GrowattApi()

login_response = api.login('ooandioo', 'oobieneoo0706')

plant_list = yaml.load(json.dumps(api.plant_list(login_response['userId'])))
print("Plants: " + str(plant_list))

plant_info = yaml.load(json.dumps(api.plant_info(plant_list['data'][0]['plantId'])))
print("Plant Info: " + str(plant_info))

dt = datetime.datetime.now() - datetime.timedelta(days=1)
plant_detail = yaml.load(json.dumps(api.plant_detail(plant_list['data'][0]['plantId'], growattServer.Timespan(1), dt)))
print("Plant Detail from " + str(dt) + ": " + str(plant_detail))

inv_list = yaml.load(json.dumps(api.inverter_list(plant_list['data'][0]['plantId'])))
print("Inverters: " + str(inv_list))

inv_detail = yaml.load(json.dumps(api.inverter_detail(inv_list[0]['deviceAilas'])))
print("Inverter Details: " + str(inv_detail))

dt = datetime.datetime.now() - datetime.timedelta(minutes=5)
inv_hist = yaml.load(json.dumps(api.inverter_data(inv_list[0]['deviceAilas'], dt)))
print("Inverter Data from " + str(dt) + ": " + str(inv_hist))
