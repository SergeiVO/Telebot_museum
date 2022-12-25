import peewee

sqlite_db = peewee.SqliteDatabase('app1.db', pragmas={
    'journal_mode': 'wal',
    'cache_size': -1024 * 64
})


class BaseModel(peewee.Model):
    class Meta:
        database = sqlite_db


class User(BaseModel):
    external_id = peewee.BigIntegerField(unique=True)
    chat_id = peewee.BigIntegerField(unique=True)



if __name__ == '__main__':
    sqlite_db.create_tables([User])
