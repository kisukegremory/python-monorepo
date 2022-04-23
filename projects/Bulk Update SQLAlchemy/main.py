from faker import Faker
from src.db import SampleTable 
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, update, bindparam
from datetime import datetime


fake = Faker()

uri = "sqlite:///example.db"
engine = create_engine(uri)
metadata = SampleTable.metadata
sync_session = sessionmaker(bind=engine)

with engine.begin() as conn:
    metadata.drop_all(bind=conn)
    metadata.create_all(bind=conn)


counter = 10000
orm_objs = [SampleTable(name=fake.name()) for _ in range(1,counter)]

with sync_session() as session:
    with session.begin():
        session.add_all(orm_objs)
    session.commit()

one_by_one_start = datetime.now()
## sync
with engine.begin() as conn:
    for _id in range(1,counter):
        stmt =(
            update(SampleTable).
            values(name="Tavinho").
            where(SampleTable.id == _id)
        )
        with sync_session() as session:
            session.execute(stmt)
        session.commit()
one_by_one_end = datetime.now()
one_by_one = one_by_one_end-one_by_one_start


bulk_start = datetime.now()
stmt_model = (
  update(SampleTable).
  where(SampleTable.id == bindparam('_id')).
  values(name=bindparam('name'))
)

with engine.begin() as conn:
  conn.execute(
      stmt_model,
      [{"_id":_id, "name": "Tavinho"} for _id in range(1,counter)]
  )
bulk_end = datetime.now()

bulk = bulk_end-bulk_start


print(f"with {counter} rows")
print(f"One by One: {one_by_one.total_seconds()}")
print(f"Bulk: {bulk.total_seconds()}")
coef = bulk.total_seconds()/one_by_one.total_seconds()
print(f"Bulk is {coef:.5f}*One by One")
print(f"One by One is {(1/coef):.5f}*Bulk")