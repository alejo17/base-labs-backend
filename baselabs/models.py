from django.db import models


class Purchases(models.Model):
    inventoryid = models.CharField(max_length=50, blank=True, null=True)
    store = models.IntegerField(blank=True, null=True)
    brand = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=50, blank=True, null=True)
    size = models.CharField(db_column='Size', max_length=50, blank=True, null=True)
    vendornumber = models.IntegerField(blank=True, null=True)
    vendorname = models.CharField(max_length=50, blank=True, null=True)
    ponumber = models.IntegerField(blank=True, null=True)
    podate = models.CharField(max_length=50, blank=True, null=True)
    receivingdate = models.CharField(max_length=50, blank=True, null=True)
    invoicedate = models.CharField(max_length=50, blank=True, null=True)
    paydate = models.CharField(max_length=50, blank=True, null=True)
    purchaseprice = models.FloatField(blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    dollars = models.FloatField(blank=True, null=True)
    classification = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'purchases'


class Sales(models.Model):
    inventoryid = models.CharField(max_length=50, blank=True, null=True)
    store = models.IntegerField(blank=True, null=True)
    brand = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=50, blank=True, null=True)
    size = models.CharField(db_column='Size', max_length=50, blank=True, null=True)
    salesquantity = models.IntegerField(blank=True, null=True)
    salesdollars = models.FloatField(blank=True, null=True)
    salesprice = models.FloatField(blank=True, null=True)
    salesdate = models.CharField(max_length=50, blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    classification = models.IntegerField(blank=True, null=True)
    excisetax = models.FloatField(blank=True, null=True)
    vendorno = models.IntegerField(blank=True, null=True)
    vendorname = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sales'


class BeginInventory(models.Model):
    inventoryid = models.CharField(max_length=50, blank=True, null=True)
    store = models.IntegerField(blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    brand = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=50, blank=True, null=True)
    size = models.CharField(db_column='Size', max_length=50, blank=True, null=True)
    onhand = models.IntegerField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    startdate = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'begin_inventory'


class EndInventory(models.Model):
    inventoryid = models.CharField(max_length=50, blank=True, null=True)
    store = models.IntegerField(blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    brand = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=50, blank=True, null=True)
    size = models.CharField(db_column='Size', max_length=50, blank=True, null=True)
    onhand = models.IntegerField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    enddate = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'end_inventory'
