import SoftLayer
import json

def main(args):
	name = args
	namejson = name
	virtualGuestName = namejson["vsiname"]
	print("VSI Name: " + virtualGuestName)
	power = namejson["poweraction"]
	print("Power Action: " + power)
	ibmcloud_iaas_user = namejson["username"]
	print("Username: " + ibmcloud_iaas_user)
	ibmcloud_iaas_key = namejson["key"]
	print("API Key: " + ibmcloud_iaas_key)

	username = ibmcloud_iaas_user
	key = ibmcloud_iaas_key

	client = SoftLayer.Client(username=username, api_key=key)

	try:

		virtualGuests = client['SoftLayer_Account'].getVirtualGuests()
		print(virtualGuests)
	except SoftLayer.SoftLayerAPIError as e:
		print("Unable to retrieve hardware. ")

	virtualGuestId = namejson["vsiid"]
	# for virtualGuest in virtualGuests:
	# 	if virtualGuest['hostname'] == virtualGuestName:
	# 		virtualGuestId = virtualGuest['id']
	# 		print("VSI ID:" + str(virtualGuestId))
	if power == "off":
		virtualMachines = client['SoftLayer_Virtual_Guest'].powerOff(id=virtualGuestId)
		print (virtualGuestName + " powered off")
		return { "Status": "OK" }
		
	elif power == "on":
		try:
			virtualMachines = client['SoftLayer_Virtual_Guest'].powerOn(id=virtualGuestId)
			print (virtualGuestName + " powered off")
			return { "Status": "OK" }
		except SoftLayer.SoftLayerAPIError as e:
			print("Unable to power on/off the virtual guest")
