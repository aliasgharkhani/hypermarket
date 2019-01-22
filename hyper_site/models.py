from django.db import models


# Create your models here.
class WareHouse(models.Model):
    WID = models.IntegerField(primary_key=True)
    capacity = models.IntegerField()
    general_type = models.CharField()
    address = models.CharField()


class Material(models.Model):
    MID = models.IntegerField(null=False),
    buyDate = models.DateTimeField(null=False),
    name = models.CharField(null=False),
    inCategory = models.IntegerField(null=False),
    producer = models.CharField(null=False),
    InWereHouse = models.IntegerField(null=False),
    color = models.IntegerField(),
    buyPrice = models.FloatField(null=False),
    sellPrice = models.FloatField(null=False),
    wight = models.FloatField(),
    type = models.CharField(null=False),

    class Meta:
        unique_together = (('MID', 'buyDate'),)


class Floor(models.Model):
    FN = models.IntegerField(null=False, primary_key=True),
    type = models.CharField(null=False),
    operatorNumber = models.IntegerField(null=False),


class equipment(models.Model):
    EK = models.IntegerField(null=False, primary_key=True),
    wellness = models.CharField(null=False),
    buyDate = models.DateField(null=False),
    available = models.CharField(null=False),
    name = models.CharField(null=False),


class customer(models.Model):
    CNumber = models.IntegerField(null=False, primary_key=True),
    name = models.CharField(null=False),
    familyName = models.CharField(null=False),
    joinDate = models.DateField()
    purchaseSum = models.PositiveIntegerField(null=False),


class transaction(models.Model):
    TN = models.IntegerField(null=False, primary_key=True),
    time = models.TimeField(null=False),
    date = models.DateField(null=False),
    amount = models.DecimalField(null=False, max_digits=19, decimal_places=4),
    CNumber = models.ForeignKey(customer, on_delete=models.CASCADE, null=False),


class telephone(models.Model):
    PNumber = models.IntegerField(null=False),
    CNumber = models.ForeignKey(customer, on_delete=models.CASCADE, null=False),

    class Meta:
        unique_together = (('PNumber', 'CNumber'),)


class spoiler(models.Model):
    MID = models.ForeignKey(Material, null=False, on_delete=models.CASCADE),
    buyDate = models.ForeignKey(Material, null=False, on_delete=models.CASCADE),
    produceDate = models.DateTimeField(null=False),
    expireDate = models.DateTimeField(null=False),

    class Meta:
        unique_together = (('MID', 'buyDate'),)


class material_wereHouse(models.Model):
    MID = models.ForeignKey(Material, null=False, on_delete=models.CASCADE),
    buyDate = models.ForeignKey(Material, null=False, on_delete=models.CASCADE),
    WID = models.ForeignKey(WareHouse, null=False, on_delete=models.CASCADE),
    wStartDay = models.DateTimeField(null=False),
    wEndDay = models.DateTimeField(null=False),

    class Meta:
        unique_together = (('MID', 'buyDate'),)


class floor_equipment(models.Model):
    FN = models.ForeignObject(Floor, null=False, on_delete=models.CASCADE),
    EK = models.ForeignKey(equipment, null=False, on_delete=models.CASCADE),
    From = models.DateField(null=False),
    to = models.DateField(null=False),

    class Meta:
        unique_together = (('FN', 'EK'),)


class employee(models.Model):
    ENumber = models.IntegerField(null=False, primary_key=True),
    birthdate = models.DateField(null=False),
    NC = models.PositiveIntegerField(null=False, unique=True),
    accessLevel = models.PositiveIntegerField(null=False),
    liability = models.CharField(null=False),
    workingHours = models.PositiveIntegerField(null=False),
    salary = models.PositiveIntegerField(null=False),
    insuranceNumber = models.PositiveIntegerField(null=False),
    joinDate = models.DateField(null=False),
    joinType = models.CharField(null=False),
    splitDate = models.DateField(null=False),
    splitType = models.CharField(null=False),
    post = models.CharField(null=False),
    sex = models.CharField(null=False),
    FN = models.ForeignKey(Floor, null=False, on_delete=models.CASCADE),


class category(models.Model):
    CID = models.IntegerField(null=False, primary_key=True),
    capacity = models.IntegerField(null=False),
    color = models.CharField(null=False),
    MID = models.ForeignKey(Material, null=False, on_delete=models.CASCADE),
    buyDate = models.ForeignKey(Material, null=False, on_delete=models.CASCADE),
    downloader = models.CharField(null=False),
    lastDownloadDate = models.DateTimeField(null=False),
    FN = models.ForeignKey(Floor, null=False, on_delete=models.CASCADE),


class uncash(models.Model):
    TN = models.ForeignKey(transaction, null=False, primary_key=True, on_delete=models.CASCADE),
    accountNumber = models.CharField(null=False),


class traffic(models.Model):
    date = models.DateField(null=False),
    time = models.TimeField(null=False),
    type = models.CharField(null=False),
    ENumber = models.ForeignKey(employee, null=False, on_delete=models.CASCADE),

    class Meta:
        unique_together = (('date', 'time'),)


class employee_wereHouse(models.Model):
    ENumber = models.ForeignKey(employee, null=False, primary_key=True, on_delete=models.CASCADE),
    WID = models.ForeignKey(WareHouse, null=False, on_delete=models.CASCADE),
    From = models.DateTimeField(null=False),
    to = models.DateTimeField(null=False),


class employee_transaction(models.Model):
    TN = models.ForeignKey(transaction, null=False, on_delete=models.CASCADE),
    ENumber = models.ForeignKey(employee, null=False, on_delete=models.CASCADE),

    class Meta:
        unique_together = (('TN', 'ENumber'),)


class employee_equipment(models.Model):
    ENumber = models.ForeignKey(employee, null=False, on_delete=models.CASCADE),
    EK = models.ForeignKey(equipment, null=False, on_delete=models.CASCADE),
    take = models.DateField(null=False),
    give = models.DateField(null=False),

    class Meta:
        unique_together = (('EK', 'ENumber'),)


class net(models.Model):
    TN = models.ForeignKey(uncash, null=False, primary_key=True, on_delete=models.CASCADE),
    trackingCode = models.CharField(null=False),


class check(models.Model):
    TN = models.ForeignKey(uncash, null=False, primary_key=True, on_delete=models.CASCADE),
    receiptDate = models.DateField(null=False),
    number = models.IntegerField(null=False),


class card(models.Model):
    TN = models.ForeignKey(uncash, null=False, primary_key=True, on_delete=models.CASCADE),
    trackingCode = models.CharField(null=False),
