
from task_manager import DB_CONFIG, create_connection, TaskManager

def mostrar_menu():
    print("\nOpciones:")
    print("1. Crear una tarea")
    print("2. Ver todas las tareas")
    print("3. Completar una tarea")
    print("4. Eliminar una tarea")
    print("5. Salir")


def main():
    

    conn, cursor = create_connection(**DB_CONFIG)
    task_manager = TaskManager(conn, cursor)
    
    while True:
        
      
        mostrar_menu()
        opcion = input("Seleccionar una opción (1-5): ")
        
     
        if opcion == '1':
            title = input("Ingresa el título de la tarea: ")
            task_manager.add_task(title)

        elif opcion == '2':
            print("Lista de tareas:")
            tasks = task_manager.get_tasks()
            if tasks:
                for task in tasks:
                    status = "Completada" if task[2] else "Pendiente"
                    print(f"ID: {task[0]}, Título: {task[1]}, Estado: {status}")
            else:
                print("No hay tareas.")

        elif opcion == '3':
            task_id = input("Ingresa el ID de la tarea a completar: ")
            task_manager.complete_task(task_id)

        elif opcion == '4':
            task_id = input("Ingresa el ID de la tarea a eliminar: ")
            task_manager.delete_task(task_id)

        elif opcion == '5':
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")
   
    task_manager.close()
main()