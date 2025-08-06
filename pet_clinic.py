# Required imports
from  sqlalchemy  import  create_engine,  Integer,  String,  ForeignKey,  DateTime,  Table,  Column
from  sqlalchemy.orm  import  declarative_base,  relationship,  sessionmaker,  Mapped,  mapped_column
from  datetime  import  datetime

Base = declarative_base()

engine = create_engine('sqlite:///clinic.db')

Session = sessionmaker(bind=engine)
session = Session() #Create Sessions
class Owner(Base):
    '''
    Owner Model with:

    id (primary key)
    name (string, not null)
    phone (string, not null)
    email (string, unique)
    Relationship to pets
    '''
    

class Pet(Base):
    '''
    Pet Model with:

    id (primary key)
    name (string, not null)
    species (string, not null) - e.g., "Dog", "Cat", "Bird"
    breed (string)
    age (integer)
    owner_id (foreign key to owners)
    Relationships to owner, veterinarians, and appointments (if you do the association model)
    '''
class Veterinarian(Base):
    '''
    Veterinarian Model with:

    id (primary key)
    name (string, not null)
    specialization (string) - e.g., "General", "Surgery", "Dermatology"
    email (string, unique)
    Relationships to pets and appointments (if you do the association model)
    '''
class Appointment(Base):
    '''
    Appointment Junction Table :
    Either Simple Table object connecting Pet and Vet ids
    or Association Model with the following fields

    id (primary key)
    pet_id (foreign key to pets)
    veterinarian_id (foreign key to veterinarians)
    appointment_date (datetime, not null)
    notes (text)
    status (string, default "Scheduled") - "Scheduled", "Completed", "Cancelled"
    Relationships to pet and veterinarian
    '''














Base.metadata.create_all(bind=engine) #Add to the bottom of page