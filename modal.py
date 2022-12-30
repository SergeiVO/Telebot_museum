import telebot
import peewee
import datetime
import datetime
from config import TOKEN_API
import logging

connect = peewee.SqliteDatabase("telek.db")


class User(peewee.Model):
    id = peewee.PrimaryKeyField(unique=True)
    user_id = peewee.IntegerField()
    name = peewee.CharField()

    class Meta:
        database = connect


connect.create_tables([User])

