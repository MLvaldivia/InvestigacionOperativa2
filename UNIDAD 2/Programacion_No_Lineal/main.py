import subprocess

def main_menu():
    while True:
        print("\n--- Menú Principal de Problemas de Optimización ---")
        print("1. Problema Convexa")
        print("2. Problema Cuadrática")
        print("3. Problema Fraccional")
        print("4. Problema Geométrica")
        print("5. Problema No Convexa")
        print("6. Optimización por Bisección")
        print("7. Problema Separable")
        print("8. Salir")
        
        # Pedir al usuario una opción
        try:
            choice = int(input("Selecciona una opción: "))
            
            if choice == 1:
                print("\nEjecutando Problema Convexa...")
                subprocess.run(["python", "p_convexa.py"])
                
            elif choice == 2:
                print("\nEjecutando Problema Cuadrática...")
                subprocess.run(["python", "p_cuadratica.py"])
                
            elif choice == 3:
                print("\nEjecutando Problema Fraccional...")
                subprocess.run(["python", "p_fracional.py"])
                
            elif choice == 4:
                print("\nEjecutando Problema Geométrica...")
                subprocess.run(["python", "p_geométrica.py"])
                
            elif choice == 5:
                print("\nEjecutando Problema No Convexa...")
                subprocess.run(["python", "p_no_convexa.py"])
                
            elif choice == 6:
                print("\nEjecutando Optimización por Bisección...")
                subprocess.run(["python", "p_optimización_bisección.py"])
                
            elif choice == 7:
                print("\nEjecutando Problema Separable...")
                subprocess.run(["python", "p_separable.py"])
                
            elif choice == 8:
                print("\nSaliendo del programa...")
                break  # Salir del menú
                
            else:
                print("Opción no válida. Inténtalo de nuevo.")
        
        except ValueError:
            print("Por favor, ingresa un número válido.")

if __name__ == "__main__":
    main_menu()
