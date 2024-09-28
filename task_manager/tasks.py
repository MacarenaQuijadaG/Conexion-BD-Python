
import mysql.connector


class TaskManager: 
  
    def __init__(self, conn, cursor):
      
        self.conn = conn
        self.cursor = cursor
    
   
    def add_task(self, title):
        
        sql = "INSERT INTO tasks (title) VALUES (%s)"
        
        try:
           
            self.cursor.execute(sql, (title,))
            self.conn.commit()
            print(f"Tarea '{title}' agregada")
        
        except mysql.connector.Error as err:
            
            print(f"Error al agregar la tarea: {err}")
    
    def get_tasks(self):
        
        try:
            
            self.cursor.execute("SELECT * FROM tasks")
            tasks = self.cursor.fetchall()
            return tasks
        
        except mysql.connector.Error as err:
            
            print(f"Error al obtener las tareas: {err}")
            return []
    
    
    def complete_task(self, task_id):
        
        
        sql = "UPDATE tasks SET completed = TRUE WHERE id = %s"
        
        try:
            
            self.cursor.execute(sql, (task_id,))
            self.conn.commit()
            
            print(f"Tarea con ID {task_id} marcada como completada")
        
        except mysql.connector.Error as err:
            
            print(f"Error al completar la tarea: {err}")
    
    def delete_task(self, task_id):
        
     
        sql = "DELETE FORM tasks WHERE id = %s"
        
        try:
      
            self.cursor.execute(sql, (task_id,))
            self.conn.commit()
            
            print(f'Tarea con ID {task_id} eliminada')
        
        except mysql.connector.Error as err:
            
            print(f"Error al eliminar la tarea: {err}")
    

    def close(self):
        self.cursor.close()
        self.conn.close()
        print("Conexión a la base de datos cerrada")