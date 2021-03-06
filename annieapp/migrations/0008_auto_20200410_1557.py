# Generated by Django 3.0.5 on 2020-04-10 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annieapp', '0007_brand_brand_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_detali',
        ),
        migrations.AddField(
            model_name='product',
            name='product_detail',
            field=models.ImageField(blank=True, help_text='Ảnh và chữ được tạo trong photoshop, chiều ngang 1000, không giới hạn chiều dài', null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='is_best_product',
            field=models.BooleanField(default=False, help_text='Sản phẩm bán chạy'),
        ),
        migrations.AlterField(
            model_name='product',
            name='is_new_product',
            field=models.BooleanField(default=False, help_text='Sản phẩm mới'),
        ),
        migrations.AlterField(
            model_name='product',
            name='is_on_sale',
            field=models.BooleanField(default=False, help_text='Sản phẩm sale'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(help_text='Tên sản phẩm', max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_img1',
            field=models.ImageField(help_text='Chiều cao và rộng bằng nhau VD:1000x1000', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_img2',
            field=models.ImageField(help_text='Chiều cao và rộng bằng nhau VD:1000x1000', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_img3',
            field=models.ImageField(help_text='Chiều cao và rộng bằng nhau VD:1000x1000', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='sale_off',
            field=models.IntegerField(default=0, help_text='Chữ số, không có dấu %'),
        ),
        migrations.AlterField(
            model_name='product',
            name='stock_price',
            field=models.IntegerField(default=0, help_text='Giá gốc'),
        ),
    ]
