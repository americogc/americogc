from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from datetime import date, datetime,timedelta

# Create your models here.
class Booking(models.Model):
    STATUS_CHOICES = (
        ('matrimonial', 'Matrimonial'),
        ('doble', 'Doble'),
        ('suite', 'Suite - Yacuzzi' ),
    )
    IMP_CHOICES = (
        (120, 'S/ 120.00'),
        (160, 'S/ 160.00'),
    )
    PAY_CHOICES = (
        ('reservacion', 'Solo reservar'),
        ('transferencia', 'Cta cci banco Interbank'),
        ('visa', 'Pago en línea' ),
    )
    ARRIVE_CHOICES = (
        ('0','12:00 a. m.'),
        ('1','1:00 a. m.'),
        ('2','2:00 a. m.'),
        ('3','3:00 a. m.'),
        ('4','4:00 a. m.'),
        ('5','5:00 a. m.'),
        ('6','6:00 a. m.'),
        ('7','7:00 a. m.'),
        ('8','8:00 a. m.'),
        ('9','9:00 a. m.'),
        ('10','10:00 a. m.'),
        ('11','11:00 a. m.'),
        ('12','12:00 p. m.'),
        ('13','1:00 p. m.'),
        ('14','2:00 p. m.'),
        ('15','3:00 p. m.'),
        ('16','4:00 p. m.'),
        ('17','5:00 p. m.'),
        ('18','6:00 p. m.'),
        ('19','7:00 p. m.'),
        ('20','8:00 p. m.'),
        ('21','9:00 p. m.'),
        ('22','10:00 p. m.'),
        ('23','11:00 p. m.'),
    )
    room_desc_type= models.CharField(max_length=100,choices=STATUS_CHOICES,
                                     default='matrimonial')
    lst_price = models.FloatField(default=160,choices=IMP_CHOICES,) #null=True)
    total = models.FloatField(null=True)
    check_in = models.DateField(default = timezone.localdate())
    check_out = models.DateField(default = timezone.localdate() + timedelta(days=1)) #timezone.now()) #default = date.today() ) # + timedelta(days=1) + datetime.timedelta(days=1)
    customer_name = models.CharField(max_length=100, null=True)
    #apellido
    customer_lastname = models.CharField(max_length=100, null=True)
    customer_email = models.CharField(max_length=100, null=True)
    #telefono
    customer_tel = models.CharField(max_length=15, null=True)
    customer_special_req = models.CharField(max_length=250, null=True)

    option_pay = models.CharField(max_length=25, choices=PAY_CHOICES,
                                     default='reservacion')
    hour_arrive = models.CharField(max_length=20,choices=ARRIVE_CHOICES, default = 1)
    estado = models.CharField(max_length=20, null = True)
    nro_personas = models.IntegerField(default=2)
    user = models.ForeignKey(User, related_name="bookings", on_delete=CASCADE, null=True)