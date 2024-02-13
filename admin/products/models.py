from django.db import models

from .shared.validators import validate_image


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name="Nomi", max_length=128, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ['name', 'created_at']
        verbose_name = "Mamlakat"
        verbose_name_plural = "Mamlakatlar"


class SubCategory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name="Nomi", max_length=128, unique=True)
    photo1 = models.FileField(verbose_name="1 - Rasm", upload_to="subcategory", validators=[validate_image])
    photo2 = models.FileField(verbose_name="2 - Rasm", upload_to="subcategory", validators=[validate_image])
    photo3 = models.FileField(verbose_name="3 - Rasm", upload_to="subcategory", validators=[validate_image])
    photo4 = models.FileField(verbose_name="4 - Rasm", upload_to="subcategory", validators=[validate_image])
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Mamlakat")
    created_at = models.DateTimeField(auto_now=True)
    tola_turi = models.CharField(verbose_name="Tola turi", max_length=128)
    zichligi = models.FloatField(verbose_name="Zichligi")
    vorsi = models.FloatField(verbose_name="Vorsi balandligi")
    ranglari = models.CharField(verbose_name="Ranglari", max_length=255)
    narhi = models.FloatField(verbose_name="Narxi m2")

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ['name', 'created_at']
        verbose_name = "Kolleksiya"
        verbose_name_plural = "Kolleksiyalar"


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    photo = models.FileField(verbose_name="Rasm", upload_to="products", validators=[validate_image])
    country = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Davlati")
    style = models.CharField(verbose_name="Stili", max_length=128)
    forma = models.CharField(verbose_name="Formasi", max_length=128)
    boyi = models.FloatField(verbose_name="Bo'yi")
    eni = models.FloatField(verbose_name="Eni")
    sub_id = models.ForeignKey(SubCategory, on_delete=models.CASCADE, verbose_name="SubKategoria")
    created_at = models.DateTimeField(auto_now=True)
    nasiya = models.BooleanField(verbose_name="Nasiya savdo", default=False)

    def __str__(self) -> str:
        return self.sub_id.name

    class Meta:
        ordering = ['country', 'created_at']
        verbose_name = "Mahsulot"
        verbose_name_plural = "Mahsulotlar"
