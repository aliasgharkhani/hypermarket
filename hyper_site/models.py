from django.db import models


# Create your models here.


class WareHouse(models.Model):
    WID = models.IntegerField(primary_key=True)
    capacity = models.IntegerField()
    general_type = models.CharField(max_length=20)
    address = models.CharField(max_length=100)


class Material(models.Model):
    MID = models.IntegerField()
    buyDate = models.DateTimeField()
    name = models.CharField(max_length=100)
    inCategory = models.IntegerField()
    producer = models.CharField(max_length=100)
    InWereHouse = models.IntegerField()
    color = models.IntegerField()
    buyPrice = models.FloatField()
    sellPrice = models.FloatField()
    wight = models.FloatField()
    type = models.CharField(max_length=100)
    WID = models.ForeignKey(WareHouse, on_delete=models.CASCADE)
    wStartDay = models.DateTimeField()
    wEndDay = models.DateTimeField()


class Floor(models.Model):
    FN = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=100)
    operatorNumber = models.IntegerField()


class Equipment(models.Model):
    EK = models.IntegerField(primary_key=True)
    wellness = models.CharField(max_length=100)
    buyDate = models.DateField()
    available = models.CharField(max_length=100)
    name = models.CharField(max_length=100)


class Customer(models.Model):
    CNumber = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    familyName = models.CharField(max_length=100)
    joinDate = models.DateField()
    purchaseSum = models.PositiveIntegerField()


class Transaction(models.Model):
    TN = models.IntegerField(primary_key=True)
    time = models.TimeField()
    date = models.DateField()
    amount = models.DecimalField(max_digits=19, decimal_places=4)
    CNumber = models.ForeignKey(Customer, on_delete=models.CASCADE )


class Telephone(models.Model):
    PNumber = models.IntegerField()
    CNumber = models.ForeignKey(Customer, on_delete=models.CASCADE, )


class Spoiler(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    produceDate = models.DateTimeField()
    expireDate = models.DateTimeField()


#
# class material_wereHouse(models.Model):
#     MID = models.ForeignKey(Material,  on_delete=models.CASCADE)
#     buyDate = models.ForeignKey(Material,  on_delete=models.CASCADE)
#     WID = models.ForeignKey(WareHouse,  on_delete=models.CASCADE)
#     wStartDay = models.DateTimeField()
#     wEndDay = models.DateTimeField()
#
#     class Meta:
#         unique_together = ('MID', 'buyDate')


class FloorEquipment(models.Model):
    FN = models.ForeignKey(Floor, on_delete=models.CASCADE)
    EK = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    From = models.DateField()
    to = models.DateField()


class Employee(models.Model):
    ENumber = models.IntegerField(primary_key=True)
    birth_date = models.DateField()
    NC = models.PositiveIntegerField(unique=True)
    accessLevel = models.PositiveIntegerField()
    liability = models.CharField(max_length=100)
    workingHours = models.PositiveIntegerField()
    salary = models.PositiveIntegerField()
    insuranceNumber = models.PositiveIntegerField()
    joinDate = models.DateField()
    joinType = models.CharField(max_length=100)
    splitDate = models.DateField()
    splitType = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    sex = models.CharField(max_length=100)
    FN = models.ForeignKey(Floor, on_delete=models.CASCADE)


class EmployeeEquipment(models.Model):
    ENumber = models.ForeignKey(Employee, on_delete=models.CASCADE)
    EK = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    take = models.DateField()
    give = models.DateField()


class Category(models.Model):
    CID = models.IntegerField(primary_key=True)
    capacity = models.IntegerField()
    color = models.CharField(max_length=100)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    downloader = models.CharField(max_length=100)
    lastDownloadDate = models.DateTimeField()
    FN = models.ForeignKey(Floor, on_delete=models.CASCADE)


class Uncash(Transaction):
    accountNumber = models.CharField(max_length=100)


class Cash(Transaction):
    pass


class Traffic(models.Model):
    date = models.DateField()
    time = models.TimeField()
    type = models.CharField(max_length=100)
    ENumber = models.ForeignKey(Employee, on_delete=models.CASCADE)


class EmployeeWereHouse(models.Model):
    ENumber = models.OneToOneField(Employee,  on_delete=models.CASCADE)
    WID = models.ForeignKey(WareHouse, on_delete=models.CASCADE)
    From = models.DateTimeField()
    to = models.DateTimeField()


class EmployeeTransaction(models.Model):
    TN = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    ENumber = models.ForeignKey(Employee, on_delete=models.CASCADE)


class Net(Uncash):
    trackingCode = models.CharField(max_length=100)


class BankCheck(Uncash):
    receiptDate = models.DateField()
    number = models.IntegerField()


class Card(Uncash):
    trackingCode = models.CharField(max_length=100)
