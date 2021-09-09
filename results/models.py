from django.db import models

# Create your models here.
class Agentname(models.Model):
    name_id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=13)
    pollingunit_uniqueid = models.IntegerField()

    class Meta:
        db_table = 'agentname'
    
    def __str__(self):
        return "%s %s"% (self.firstname, self.lastname)


class AnnouncedLgaResults(models.Model):
    result_id = models.AutoField(primary_key=True)
    lga_name = models.CharField(max_length=50)
    party_abbreviation = models.CharField(max_length=4)
    party_score = models.IntegerField()
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.DateTimeField()
    user_ip_address = models.CharField(max_length=50)

    class Meta:
        db_table = 'announced_lga_results'
        ordering=("party_abbreviation",)
        verbose_name_plural="AnnounceLgaResults"
    
    
    def __str__(self):
        return "%s %d" % (self.party_abbreviation, self.party_score)


class AnnouncedPuResults(models.Model):
    result_id = models.AutoField(primary_key=True)
    polling_unit_uniqueid = models.CharField(max_length=50)
    party_abbreviation = models.CharField(max_length=4)
    party_score = models.IntegerField()
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.DateTimeField()
    user_ip_address = models.CharField(max_length=50)

    class Meta:
        db_table = 'announced_pu_results'
        ordering=("polling_unit_uniqueid",)
        verbose_name_plural= "AnnouncedPuResults"
    
    def __str__(self):
        return "%s %d" % (self.party_abbreviation,self.party_score)
    
    def serialized(self):
        data={
            f"{self.party_abbreviation}": self.party_abbreviation,
            f"{self.party_abbreviation}_score":self.party_score
        }
        return data


class AnnouncedStateResults(models.Model):
    result_id = models.AutoField(primary_key=True)
    state_name = models.CharField(max_length=50)
    party_abbreviation = models.CharField(max_length=4)
    party_score = models.IntegerField()
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.DateTimeField()
    user_ip_address = models.CharField(max_length=50)

    class Meta:
        db_table = 'announced_state_results'
        ordering=("party_abbreviation",)
    
    def __str__(self):
        return "%s %d" % (self.party_abbreviation,self.party_score)


class AnnouncedWardResults(models.Model):
    result_id = models.AutoField(primary_key=True)
    ward_name = models.CharField(max_length=50)
    party_abbreviation = models.CharField(max_length=4)
    party_score = models.IntegerField()
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.DateTimeField()
    user_ip_address = models.CharField(max_length=50)

    class Meta:
        db_table = 'announced_ward_results'
        ordering=("party_abbreviation",)
    
    def __str__(self):
        return "%s %d" % (self.party_abbreviation,self.party_score)

class Lga(models.Model):
    uniqueid = models.AutoField(primary_key=True)
    lga_id = models.IntegerField()
    lga_name = models.CharField(max_length=50)
    state_id = models.IntegerField()
    lga_description = models.TextField(blank=True, null=True)
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.DateTimeField()
    user_ip_address = models.CharField(max_length=50)

    class Meta:
        db_table = 'lga'
        ordering=("lga_name",)
    
    def __str__(self):
        return "%s" % (self.lga_name)

    def serialized(self):
        data={
            "lga_name":self.lga_name,
            "lga_id": self.lga_id
        }
        return data


class Party(models.Model):
    partyid = models.CharField(max_length=11)
    partyname = models.CharField(max_length=11)

    class Meta:
        db_table = 'party'
    
    def __str__(self):
        return "%s" % (self.partyname)
    
    def serialized(self):
        data={
            'party_id':self.partyid,
            'party_name':self.partyname
        }
        return data

class PollingUnit(models.Model):
    uniqueid = models.AutoField(primary_key=True)
    polling_unit_id = models.IntegerField()
    ward_id = models.IntegerField()
    lga_id = models.IntegerField()
    uniquewardid = models.IntegerField(blank=True, null=True)
    polling_unit_number = models.CharField(max_length=50, blank=True, null=True)
    polling_unit_name = models.CharField(max_length=50, blank=True, null=True)
    polling_unit_description = models.TextField(blank=True, null=True)
    lat = models.CharField(max_length=255, blank=True, null=True)
    long = models.CharField(max_length=255, blank=True, null=True)
    entered_by_user = models.CharField(max_length=50, blank=True, null=True)
    date_entered = models.DateTimeField(blank=True, null=True)
    user_ip_address = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'polling_unit'

    def __str__(self):
        name=""
        if self.polling_unit_name=="":
            name="Nil"
        return "%s: %d" % (name,self.polling_unit_id)
    


class States(models.Model):
    state_id = models.IntegerField(primary_key=True)
    state_name = models.CharField(max_length=50)

    class Meta:
        db_table = 'states'
    
    def __str__(self):
        return "%s : %d" % (self.state_name,self.state_id)


class Ward(models.Model):
    uniqueid = models.AutoField(primary_key=True)
    ward_id = models.IntegerField()
    ward_name = models.CharField(max_length=50)
    lga_id = models.IntegerField()
    ward_description = models.TextField(blank=True, null=True)
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.DateTimeField()
    user_ip_address = models.CharField(max_length=50)

    class Meta:
        db_table = 'ward'
    def __str__(self):
        return "%s : %d" % (self.ward_name, self.ward_id)

