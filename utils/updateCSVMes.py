

from sqlalchemy import (Column, Integer, Float, String, DateTime)
import datetime

from app import db

class Measurement(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    air_quality = Column(Float, nullable=False)
    humidity = Column(Float, nullable=False)
    temperature = Column(Float, nullable=False)
    timestamp = Column(DateTime(timezone=True), nullable=False, default=datetime.datetime.utcnow)


def update():
    msr_data = db.session.query(Measurement).all()
    with open('CSVMes.txt', 'w') as f:
        f.write(','.join(Measurement.__dict__.keys())+"\n")
        for msr in msr_data:
            f.write(','.join([msr.id,msr.air_quality,msr.humidity,msr.temperature,msr.timestamp]) + "\n")

if __name__ == '__main__':
    update()
