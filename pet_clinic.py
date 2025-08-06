# Required imports
from  sqlalchemy  import  Text, create_engine,  Integer,  String,  ForeignKey,  DateTime,  Table,  Column
from  sqlalchemy.orm  import  declarative_base,  relationship,  sessionmaker,  Mapped,  mapped_column
from  datetime  import  datetime

Base = declarative_base()

engine = create_engine('sqlite:///clinic.db')

Session = sessionmaker(bind=engine)
session = Session() #Create Sessions
class Owners(Base):
    '''
    Owner Model with:

    id (primary key)
    name (string, not null)
    phone (string, not null)
    email (string, unique)
    Relationship to pets
    '''
    __tablename__='owners'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    phone: Mapped[str] = mapped_column(String(255), nullable=False)
    email: Mapped[str] = mapped_column(String(255), unique=True)

class Pets(Base):
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
    __tablename__='pets'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    species: Mapped[str] = mapped_column(String(255), nullable=False)
    breed: Mapped[str] = mapped_column(String(255))
    age: Mapped[int] = mapped_column(Integer)

class Veterinarians(Base):
    '''
    Veterinarian Model with:

    id (primary key)
    name (string, not null)
    specialization (string) - e.g., "General", "Surgery", "Dermatology"
    email (string, unique)
    
    Relationships to pets and appointments (if you do the association model)
    '''
    __tablename__='veterinarians'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    specialization: Mapped[str] = mapped_column(String(255) # TODO )
    email: Mapped[str] = mapped_column(String(255), unique=True)
    
class Appointments(Base):
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
    __tablename__ = 'appointments'

    id: Mapped[int] = mapped_column(primary_key=True)
    pet_id: Mapped[int] = mapped_column(Integer, ForeignKey('pets.id'))
    veterinarian_id: Mapped[int] = mapped_column(Integer, ForeignKey("veterinarians.id"))
    appointment_date: Mapped[datetime] = mapped_column(DateTime, default=datetime.now(), nullable=False)
    notes: Mapped[str] =mapped_column(Text)
    status: Mapped[str] = mapped_column(String(255), default='Scheduled', #TODO )













Base.metadata.create_all(bind=engine) #Add to the bottom of page