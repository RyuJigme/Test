from queue import Queue
def main():    
    patient_queue = Queue()
    while True:
        print("\n1. Register Patient\n2. Remove Patient after Meeting Doctor\n3. Display Patient Queue\n4. Exit")
        choice = input("Enter your choice:")
        if choice == '1':
            name = input("Enter patient's name to register: ")            
            patient_queue.put(name)
            print(f"Patient {name} registered.")        
        elif choice == '2':
            if patient_queue.empty():                
                print("No patients in queue.")
            else:                
                name = patient_queue.get()
                print(f"Patient {name} has met the doctor and is now removed from the queue.")        
        elif choice == '3':
            if patient_queue.empty():                
                print("No patients in queue.")
            else:                
                print("Patients in queue:")
                for index, name in enumerate(list(patient_queue.queue)):                    
                    print(f"{index + 1}. {name}")
        elif choice == '4':            
            print("Exiting program.")
            break        
        else:
            print("Invalid input. Please enter a number between 1 and 4.")
if __name__== "__main__":    
    main()
