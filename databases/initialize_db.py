from databases.models import Base, engine

def initialize_database():
    Base.metadata.create_all(engine)

if __name__ == "__main__":
    print("Initializing database...")
    initialize_database()
    print("Database initialized successfully!")

