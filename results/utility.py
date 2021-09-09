from .models import AnnouncedPuResults,Lga, Party
'''
The utility module contain helper functions
'''

def get_serialized_PuResult():
    #returns the serialized Polling Unit results

    data=AnnouncedPuResults.objects.all()
    data_set=set([i.polling_unit_uniqueid for i in data])
    data_list= sorted(list(data_set))

    serialized_data=[]
    for i in data_list:
        d=AnnouncedPuResults.objects.filter(polling_unit_uniqueid=i)
        serial={}
        for b in d:
            serial.update(b.serialized())
        serial["id"]=i
        serialized_data.append(serial)
    return serialized_data

def get_serialized_Pu():
    # returns the serialized polling unit
    data=Lga.objects.all().exclude(lga_name="")
    data_list=[l.serialized() for l in data]
    return data_list

def get_serialized_party():
    # returns the serialized party data
    
    data=[p.serialized() for p in Party.objects.all().exclude(partyname='')]
    return data






