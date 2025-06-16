import random
import tkinter as tk
from tkinter import messagebox, Canvas, PhotoImage
import time

class AWSPokemonQuiz:
    def __init__(self, root):
        self.root = root
        self.root.title("AWS Pokémon Quiz")
        self.root.geometry("400x600")
        self.root.configure(bg="#3B4CCA")  # Pokémon blue
        
        # Store references to images to prevent garbage collection
        self.images = {}
        
        self.questions = [
            {
                "question": "Which AWS service is used for object storage?",
                "options": ["EC2", "S3", "RDS", "Lambda"],
                "answer": "S3",
                "pokemon": "S3saur",
                "color": "#3CB371"  # Green like Bulbasaur
            },
            {
                "question": "Which AWS service runs code without provisioning servers?",
                "options": ["EC2", "EBS", "Lambda", "RDS"],
                "answer": "Lambda",
                "pokemon": "Lambachu",
                "color": "#FFD700"  # Yellow like Pikachu
            },
            {
                "question": "Which AWS service provides virtual servers in the cloud?",
                "options": ["EC2", "S3", "DynamoDB", "CloudFront"],
                "answer": "EC2",
                "pokemon": "EC2kachu",
                "color": "#FF8C00"  # Orange like Charmander
            },
            {
                "question": "Which AWS service is a managed NoSQL database?",
                "options": ["RDS", "Redshift", "DynamoDB", "Aurora"],
                "answer": "DynamoDB",
                "pokemon": "DynamoMew",
                "color": "#9370DB"  # Purple like Mewtwo
            },
            {
                "question": "Which AWS service is used for content delivery?",
                "options": ["Route 53", "CloudFront", "ELB", "VPC"],
                "answer": "CloudFront",
                "pokemon": "CloudFairy",
                "color": "#FF69B4"  # Pink like Jigglypuff
            }
        ]
        
        self.current_question = 0
        self.score = 0
        self.caught_pokemon = []
        
        self.create_widgets()
    
    def create_widgets(self):
        # Clear previous widgets
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Title
        title_label = tk.Label(
            self.root, 
            text="AWS Pokémon Quiz", 
            font=("Arial", 24, "bold"),
            bg="#3B4CCA",
            fg="#FFDE00"  # Pokémon yellow
        )
        title_label.pack(pady=20)
        
        if self.current_question < len(self.questions):
            self.display_question()
        else:
            self.show_pokedex()
    
    def display_question(self):
        question_data = self.questions[self.current_question]
        
        # Question frame
        question_frame = tk.Frame(self.root, bg="#FFFFFF", padx=20, pady=20, bd=5, relief=tk.RAISED)
        question_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Question number
        question_num = tk.Label(
            question_frame,
            text=f"Question {self.current_question + 1}/{len(self.questions)}",
            font=("Arial", 12),
            bg="#FFFFFF"
        )
        question_num.pack(anchor=tk.W)
        
        # Question text
        question_label = tk.Label(
            question_frame,
            text=question_data["question"],
            font=("Arial", 14, "bold"),
            wraplength=300,
            bg="#FFFFFF"
        )
        question_label.pack(pady=10)
        
        # Options
        option_var = tk.StringVar()
        for option in question_data["options"]:
            option_btn = tk.Radiobutton(
                question_frame,
                text=option,
                variable=option_var,
                value=option,
                font=("Arial", 12),
                bg="#FFFFFF",
                selectcolor="#FFDE00"
            )
            option_btn.pack(anchor=tk.W, pady=5)
        
        # Submit button
        submit_btn = tk.Button(
            question_frame,
            text="Submit Answer",
            font=("Arial", 12, "bold"),
            bg="#FF0000",  # Pokémon red
            fg="#FFFFFF",
            command=lambda: self.check_answer(option_var.get(), question_data["answer"], question_data["pokemon"])
        )
        submit_btn.pack(pady=15)
        
        # Score
        score_label = tk.Label(
            self.root,
            text=f"Score: {self.score}",
            font=("Arial", 12),
            bg="#3B4CCA",
            fg="#FFFFFF"
        )
        score_label.pack(pady=10)
    
    def check_answer(self, selected, correct, pokemon):
        if not selected:
            messagebox.showinfo("Select an option", "Please select an answer!")
            return
            
        if selected == correct:
            self.score += 1
            self.caught_pokemon.append(pokemon)
            self.show_scratch_card(pokemon)
        else:
            messagebox.showinfo("Incorrect", f"Wrong answer! The correct answer is {correct}.")
            self.current_question += 1
            self.create_widgets()
    
    def show_scratch_card(self, pokemon):
        # Clear previous widgets
        for widget in self.root.winfo_children():
            widget.destroy()
            
        # Scratch card frame
        scratch_frame = tk.Frame(self.root, bg="#FFFFFF", padx=20, pady=20, bd=5, relief=tk.RAISED)
        scratch_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Correct answer label
        correct_label = tk.Label(
            scratch_frame,
            text="Correct Answer!",
            font=("Arial", 18, "bold"),
            fg="#00AA00",
            bg="#FFFFFF"
        )
        correct_label.pack(pady=10)
        
        # Scratch card effect
        scratch_label = tk.Label(
            scratch_frame,
            text="Scratching to reveal Pokémon...",
            font=("Arial", 14),
            bg="#FFFFFF"
        )
        scratch_label.pack(pady=10)
        
        # Simulate scratching
        self.root.update()
        time.sleep(1)
        
        # Reveal Pokémon
        pokemon_label = tk.Label(
            scratch_frame,
            text=f"You caught {pokemon}!",
            font=("Arial", 20, "bold"),
            fg="#FF0000",
            bg="#FFFFFF"
        )
        pokemon_label.pack(pady=10)
        
        # Get pokemon color
        pokemon_color = "#FFD700"  # Default yellow
        for q in self.questions:
            if q["pokemon"] == pokemon:
                pokemon_color = q["color"]
                break
        
        # Create a canvas for the Pokémon image
        canvas_width, canvas_height = 150, 150
        canvas = tk.Canvas(
            scratch_frame, 
            width=canvas_width, 
            height=canvas_height, 
            bg="#FFFFFF",
            highlightthickness=0
        )
        canvas.pack(pady=10)
        
        # Draw a Pokémon-like character
        self.draw_pokemon(canvas, pokemon, pokemon_color)
        
        # Continue button
        continue_btn = tk.Button(
            scratch_frame,
            text="Continue",
            font=("Arial", 12, "bold"),
            bg="#3B4CCA",
            fg="#FFFFFF",
            command=self.next_question
        )
        continue_btn.pack(pady=15)
    
    def draw_pokemon(self, canvas, pokemon, color):
        # Draw a colorful Pokémon-like character based on the name
        w, h = 150, 150
        
        # Body
        canvas.create_oval(30, 30, w-30, h-30, fill=color, outline="black", width=2)
        
        # Eyes
        canvas.create_oval(50, 60, 70, 80, fill="white", outline="black", width=2)
        canvas.create_oval(w-70, 60, w-50, 80, fill="white", outline="black", width=2)
        canvas.create_oval(55, 65, 65, 75, fill="black")
        canvas.create_oval(w-65, 65, w-55, 75, fill="black")
        
        # Mouth
        if "saur" in pokemon:
            # Bulbasaur-like mouth
            canvas.create_line(60, 100, 90, 110, w-60, 100, smooth=True, width=2)
        elif "chu" in pokemon:
            # Pikachu-like mouth
            canvas.create_arc(60, 90, w-60, 120, start=0, extent=-180, style="arc", width=2)
        elif "Mew" in pokemon:
            # Mewtwo-like mouth
            canvas.create_line(75, 100, w-75, 100, width=2)
        else:
            # Default smile
            canvas.create_arc(50, 80, w-50, 120, start=0, extent=-180, style="arc", width=2)
        
        # Special features based on Pokémon type
        if pokemon == "S3saur":
            # Bulbasaur-like bulb
            canvas.create_oval(w//2-25, 15, w//2+25, 45, fill="#2E8B57", outline="black", width=2)
        elif pokemon == "Lambachu":
            # Pikachu-like ears
            canvas.create_polygon(40, 40, 30, 5, 60, 30, fill=color, outline="black", width=2)
            canvas.create_polygon(w-40, 40, w-30, 5, w-60, 30, fill=color, outline="black", width=2)
            # Lightning bolt
            canvas.create_polygon(65, 90, 75, 105, 65, 110, 85, 130, fill="yellow", outline="black")
        elif pokemon == "EC2kachu":
            # Charmander-like flame
            canvas.create_oval(w//2-10, 10, w//2+10, 40, fill="#FF4500", outline="black", width=2)
        elif pokemon == "DynamoMew":
            # Mewtwo-like head shape
            canvas.create_polygon(w//2-30, 40, w//2, 10, w//2+30, 40, fill=color, outline="black", width=2)
        elif pokemon == "CloudFairy":
            # Jigglypuff-like curl
            canvas.create_arc(w//2-20, 20, w//2+20, 40, start=0, extent=180, style="arc", width=2)
        
        # Name
        canvas.create_text(w//2, h-15, text=pokemon, font=("Arial", 12, "bold"))
    
    def next_question(self):
        self.current_question += 1
        self.create_widgets()
    
    def show_pokedex(self):
        # Pokédex frame
        pokedex_frame = tk.Frame(self.root, bg="#FF0000", padx=20, pady=20, bd=5, relief=tk.RAISED)
        pokedex_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Pokédex title
        pokedex_title = tk.Label(
            pokedex_frame,
            text="AWS Pokédex",
            font=("Arial", 20, "bold"),
            bg="#FF0000",
            fg="#FFFFFF"
        )
        pokedex_title.pack(pady=10)
        
        # Final score
        score_label = tk.Label(
            pokedex_frame,
            text=f"Final Score: {self.score}/{len(self.questions)}",
            font=("Arial", 16),
            bg="#FF0000",
            fg="#FFFFFF"
        )
        score_label.pack(pady=10)
        
        # Caught Pokémon list
        caught_label = tk.Label(
            pokedex_frame,
            text="Caught AWS Pokémon:",
            font=("Arial", 14, "bold"),
            bg="#FF0000",
            fg="#FFFFFF"
        )
        caught_label.pack(pady=10, anchor=tk.W)
        
        # Create a white inner frame for the Pokémon list
        pokemon_list_frame = tk.Frame(pokedex_frame, bg="#FFFFFF", padx=10, pady=10)
        pokemon_list_frame.pack(fill=tk.BOTH, expand=True)
        
        if not self.caught_pokemon:
            no_pokemon = tk.Label(
                pokemon_list_frame,
                text="You didn't catch any AWS Pokémon!",
                font=("Arial", 12),
                bg="#FFFFFF"
            )
            no_pokemon.pack(pady=10)
        else:
            # Create a canvas for each caught Pokémon
            for i, pokemon in enumerate(self.caught_pokemon):
                # Container frame for each Pokémon
                pokemon_container = tk.Frame(pokemon_list_frame, bg="#FFFFFF")
                pokemon_container.pack(fill=tk.X, pady=10)
                
                # Get pokemon color
                pokemon_color = "#FFD700"  # Default yellow
                for q in self.questions:
                    if q["pokemon"] == pokemon:
                        pokemon_color = q["color"]
                        break
                
                # Create a small canvas for the Pokémon image
                canvas_width, canvas_height = 80, 80
                canvas = tk.Canvas(
                    pokemon_container, 
                    width=canvas_width, 
                    height=canvas_height, 
                    bg="#FFFFFF",
                    highlightthickness=0
                )
                canvas.pack(side=tk.LEFT, padx=5)
                
                # Draw a smaller Pokémon
                self.draw_small_pokemon(canvas, pokemon, pokemon_color)
                
                # Info frame
                info_frame = tk.Frame(pokemon_container, bg="#FFFFFF")
                info_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
                
                # Pokémon name
                pokemon_name = tk.Label(
                    info_frame,
                    text=pokemon,
                    font=("Arial", 12, "bold"),
                    bg="#FFFFFF",
                    fg="#000000"
                )
                pokemon_name.pack(anchor=tk.W)
                
                # Description
                description = tk.Label(
                    info_frame,
                    text=self.get_pokemon_description(pokemon),
                    font=("Arial", 10),
                    wraplength=250,
                    bg="#FFFFFF",
                    fg="#555555",
                    justify=tk.LEFT
                )
                description.pack(anchor=tk.W)
        
        # Play again button
        play_again_btn = tk.Button(
            self.root,
            text="Play Again",
            font=("Arial", 12, "bold"),
            bg="#3B4CCA",
            fg="#FFFFFF",
            command=self.restart_game
        )
        play_again_btn.pack(pady=15)
    
    def draw_small_pokemon(self, canvas, pokemon, color):
        # Draw a smaller version of the Pokémon for the Pokédex
        w, h = 80, 80
        
        # Body
        canvas.create_oval(15, 15, w-15, h-15, fill=color, outline="black", width=2)
        
        # Eyes
        canvas.create_oval(25, 30, 35, 40, fill="white", outline="black", width=1)
        canvas.create_oval(w-35, 30, w-25, 40, fill="white", outline="black", width=1)
        canvas.create_oval(28, 33, 32, 37, fill="black")
        canvas.create_oval(w-32, 33, w-28, 37, fill="black")
        
        # Mouth - simplified for small size
        canvas.create_line(30, 50, w-30, 50, width=1)
        
        # Special features based on Pokémon type - simplified for small size
        if pokemon == "S3saur":
            canvas.create_oval(w//2-10, 10, w//2+10, 25, fill="#2E8B57", outline="black", width=1)
        elif pokemon == "Lambachu":
            canvas.create_polygon(25, 20, 20, 5, 35, 15, fill=color, outline="black", width=1)
            canvas.create_polygon(w-25, 20, w-20, 5, w-35, 15, fill=color, outline="black", width=1)
        elif pokemon == "EC2kachu":
            canvas.create_oval(w//2-5, 10, w//2+5, 20, fill="#FF4500", outline="black", width=1)
        elif pokemon == "DynamoMew":
            canvas.create_polygon(w//2-15, 20, w//2, 5, w//2+15, 20, fill=color, outline="black", width=1)
    
    def restart_game(self):
        self.current_question = 0
        self.score = 0
        self.caught_pokemon = []
        self.create_widgets()
    
    def get_pokemon_description(self, pokemon):
        descriptions = {
            "S3saur": "A storage-type AWS Pokémon that can hold unlimited objects and has 99.999999999% durability.",
            "Lambachu": "A serverless AWS Pokémon that executes code in response to events without provisioning servers.",
            "EC2kachu": "A compute-type AWS Pokémon that can scale up and down based on demand.",
            "DynamoMew": "A database-type AWS Pokémon with single-digit millisecond response times at any scale.",
            "CloudFairy": "A networking-type AWS Pokémon that delivers content globally with low latency."
        }
        return descriptions.get(pokemon, "")

if __name__ == "__main__":
    root = tk.Tk()
    app = AWSPokemonQuiz(root)
    root.mainloop()