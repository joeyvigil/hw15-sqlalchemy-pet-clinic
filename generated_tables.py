#GENERATED USING sqlacodegen, but I still had to fix a few errors (datetime and primary keys)
# Required imports
from typing import Any, List, Optional

from sqlalchemy import ForeignKey, Integer, String, text, create_engine,  Integer,  String,  ForeignKey,  DateTime,  Table,  Column
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, declarative_base, sessionmaker
from sqlalchemy.sql.sqltypes import NullType
from  datetime  import  datetime

Base = declarative_base()
engine = create_engine('sqlite:///clinic.db')


class Owners(Base):
    __tablename__ = 'owners'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    phone: Mapped[str] = mapped_column(String(255), nullable= False)
    email: Mapped[str] = mapped_column(String(255), unique=True)

    pets: Mapped[List['Pets']] = relationship('Pets', back_populates='owner')


class Veterinarians(Base):
    __tablename__ = 'veterinarians'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    specialization: Mapped[str] = mapped_column(String(255))
    email: Mapped[str] = mapped_column(String(255), unique=True)

    appointments: Mapped[List['Appointments']] = relationship('Appointments', back_populates='veterinarian')


class Pets(Base):
    __tablename__ = 'pets'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    species: Mapped[str] = mapped_column(String(255), nullable=False)
    breed: Mapped[str] = mapped_column(String(255))
    age: Mapped[int] = mapped_column(Integer)
    owner_id: Mapped[int] = mapped_column(ForeignKey('owners.id', ondelete='CASCADE'))

    owner: Mapped[Optional['Owners']] = relationship('Owners', back_populates='pets')
    appointments: Mapped[List['Appointments']] = relationship('Appointments', back_populates='pet')


class Appointments(Base):
    __tablename__ = 'appointments'

    id: Mapped[int] = mapped_column(primary_key=True)
    pet_id: Mapped[Optional[int]] = mapped_column(ForeignKey('pets.id', ondelete='CASCADE'))
    veterinarian_id: Mapped[Optional[int]] = mapped_column(ForeignKey('veterinarians.id', ondelete='CASCADE'))
    appointment_date: Mapped[Any] = mapped_column(DateTime, default=datetime.now())
    notes: Mapped[str] = mapped_column(String(255))
    status: Mapped[str] = mapped_column(String(255), default='Scheduled')

    pet: Mapped['Pets'] = relationship('Pets', back_populates='appointments')
    veterinarian: Mapped['Veterinarians'] = relationship('Veterinarians', back_populates='appointments')
    
    
    
Base.metadata.create_all(bind=engine) #Add to the bottom of page
  
  
# # ======= CREATE DATA ======  
Session = sessionmaker(bind=engine)
session = Session() #Create Sessions

new_owners = [
    Owners(name= 'Joseph Vigil', phone = '(719) 420-6969', email ='jv@email.com'),
    Owners(name= 'Sly Clayton', phone = '(719) 123-6969', email ='sly@email.com'),
    Owners(name= 'Silver Fox', phone = '(719) 240-1234', email ='foxy@email.com')
]

new_pets = [
    Pets(name= 'Beans', species = 'Dog', breed ='Cream Retriever', age = 5 , owner_id= 1),
    Pets(name= 'Mr. Bingleworth', species = 'Cat', breed ='Hairless', age = 3 , owner_id= 1),
    Pets(name= 'Spiderman', species = 'Dog', breed ='Husky', age = 8 , owner_id= 2),
    Pets(name= 'Thing 1', species = 'Fish', breed ='Clown Fish', age = 1 , owner_id= 3),
    Pets(name= 'Thing 2', species = 'Fish', breed ='Clown Fish', age = 1 , owner_id= 3),
    Pets(name= 'Thing 3', species = 'Fish', breed ='Clown Fish', age = 1 , owner_id= 3)
]

new_vets = [
    Veterinarians(name= 'Dr. Jaksic', specialization = 'Surgery', email ='drjaksic@gmail.com'),Veterinarians(name= 'Dr. Barnet', specialization = 'MD', email ='drbarnet@gmail.com')
]

new_apps = [
    Appointments(pet_id= '1', veterinarian_id = '1', notes ='Tummy Ache'),
    Appointments(pet_id= '1', veterinarian_id = '2', notes ='Medication'),
    Appointments(pet_id= '2', veterinarian_id = '2', notes ='Hair Plugs'),
    Appointments(pet_id= '3', veterinarian_id = '1', notes ='Eye Surgery'),
    Appointments(pet_id= '3', veterinarian_id = '2', notes ='Medication'),
    Appointments(pet_id= '4', veterinarian_id = '2', notes ='Anxiety Meds'),
    Appointments(pet_id= '5', veterinarian_id = '2', notes ='Anxiety Meds'),
    Appointments(pet_id= '6', veterinarian_id = '2', notes ='Anxiety Meds')
]
session.add_all(new_owners)
session.add_all(new_pets)
session.add_all(new_vets)
session.add_all(new_apps)
session.commit()


#get  all user data
all_owners = session.query(Owners).all() # SELECT * FROM users
print('\n---------- Owners, Pets & Appointments ----------')
for user in all_owners:
    print(f"\n{user.id}. {user.name}: {user.email}")
    pets = user.pets
    for pet in pets:
        print(f'    *{pet.name}: {pet.species}, {pet.breed}')
        appoints = pet.appointments
        for appoint in appoints:
            print(f'        {appoint.appointment_date.date()}: {appoint.notes} :: {appoint.status} with {appoint.veterinarian.name}')
