from .models import AnnouncedPuResults,Lga

def get_serialized_PuResult():
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
    data=Lga.objects.all().exclude(lga_name="")
    data_list=[l.serialized() for l in data]
    return data_list







