import csv
from datetime import datetime
from models import Session, Message, Priority  # Assuming 'models.py' contains your Session setup

def import_messages_from_csv(csv_file_path):
    session = Session()  # Create session from updated Session factory
    
    with open(csv_file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            try:
                # Parse CSV fields - adjust these field names to match your CSV
                customer_id = int(row['User ID'])
                message_text = row['Message Body']  # Updated field name
                timestamp = datetime.strptime(row['Timestamp (UTC)'], "%m/%d/%Y %H:%M")  # New timestamp parsing
                
                # Create a new Message instance
                new_message = Message(
                    customer_id=customer_id,
                    message_text=message_text,
                    timestamp=timestamp  # Added timestamp
                )
                
                # Add to the session
                session.add(new_message)
                
            except Exception as e:
                print(f"Error processing row: {row}")
                print(f"Error: {str(e)}")
                continue
        
        try:
            # Commit all changes to the database
            session.commit()
            print("Messages imported successfully.")
        except Exception as e:
            print(f"Error committing to database: {str(e)}")
            session.rollback()

if __name__ == "__main__":
    csv_file_path = 'messages.csv'  # Update with your CSV file path
    import_messages_from_csv(csv_file_path)
