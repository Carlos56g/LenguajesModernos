from sqlalchemy import create_engine, text
from sqlalchemy import insert

engine = create_engine('mssql+pyodbc://@SIRIUS-S40\\SQLEXPRESS/Agenda_db?trusted_connection=yes&driver=ODBC+Driver+17+for+SQL+Server')


def getEvents():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT * From Event_tb"))
        events_list = [row for row in result]
        return events_list
    
def postEvent(eventDatetime,eventTitle,eventDescription):
    with engine.connect() as connection:
        # Use a parameterized query
        query = text("INSERT INTO Event_tb (EventDate, EventTitle, EventDescription) VALUES (:event_datetime, :event_title, :event_description)")

        parameters = {
            'event_datetime': eventDatetime,
            'event_title': eventTitle,
            'event_description': eventDescription
            }
        
        # Execute the query with the provided parameters
        result=connection.execute(query,parameters)
        connection.commit()
        print(result)

    return 0
