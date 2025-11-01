import tkinter as tk
import random


class ConwaysGameOfLife:
    
    def __init__(self,rows,columns,sizeofcell,speed):
        self.check=0
        self.immortalcell=[]
        self.deadcells=[]
        self.buttons=[]
        self.array_cord=[]
        self.rows=rows
        self.columns=columns
        self.sizeofcell=sizeofcell
        self.speed=speed
        self.new=0
        self.grid=[]
        self.key_pressed = False
        self.generation=0
        self.programm=tk.Tk()
        self.canvas = tk.Canvas(self.programm, width=self.columns*self.sizeofcell,
                                height=self.rows*self.sizeofcell,  bg='white')
        self.canvas.pack()
        self.programm.resizable(False, False)
        self.programm.title('Game of Life')
        self.programm.config(bg='lightblue')
        self.create_label()
        self.create_buttons()
        self.programm.mainloop()
        self.array=[]
    
    def create_buttons(self):
        button_frame = tk.Frame(self.programm, bg='lightblue', bd=2, relief=tk.SOLID)
        button_frame.pack(pady=10)

        button_style = {'font': ('Arial', 12), 'width': 15, 'height': 2, 'bg': 'lightblue', 'fg': 'black', 'bd': 0, 'activebackground': 'lightgreen', 'activeforeground': 'white'}

        self.start_button = tk.Button(button_frame, text='Random Generate', command=self.run1, **button_style)
        self.pause_button = tk.Button(button_frame, text='Pause', command=self.pause, **button_style)
        self.continue_button = tk.Button(button_frame, text='Start/Continue', command=self.bcontinue, **button_style)
        self.stop_button = tk.Button(button_frame, text='Exit', command=self.programm.destroy, **button_style)
        self.steady_button = tk.Button(button_frame, text='Set Immortal Cells', command=self.immortal, **button_style)
        self.dead_button = tk.Button(button_frame, text='Set dead Cells', command=self.dead, **button_style)
        self.reset_button = tk.Button(button_frame, text='Random reset', command=self.reset, **button_style)
        self.clear_button = tk.Button(button_frame, text='Clear', command=self.clear, **button_style)
        self.speed_slider = tk.Scale(self.programm, from_=1, to=100, orient=tk.HORIZONTAL, label='Speed', command=self.change_speed, bg='lightblue', troughcolor='lightblue', highlightbackground='lightblue', sliderlength=20, width=10)
        self.speed_slider.set(self.speed)
        self.user_button = tk.Button(button_frame, text='Initialize', command=self.run2, **button_style)
        self.start_button.pack(side='left', padx=10)
        self.user_button.pack(side='left', padx=10)
        self.steady_button.pack(side='left', padx=10)
        self.dead_button.pack(side='left', padx=10)
        self.pause_button.pack(side='left', padx=10)
        self.continue_button.pack(side='left', padx=10)
        self.stop_button.pack(side='left', padx=10)
        self.reset_button.pack(side='left', padx=10)
        self.clear_button.pack(side='left', padx=10)
        self.speed_slider.pack(pady=10)

        
    def make_array_users(self):
        
        self.array_cord=[]
        self.array=[]
        self.new=tk.Toplevel(self.programm)
        res=str(self.columns*self.sizeofcell+self.columns*3)+"x"+str(self.rows*self.sizeofcell+50)
        
        self.new.title("Choose the buttons and press 'b' to continue")
        
        self.key_pressed = False
        
        def on_key_press(event):
            if event.char == 'b':
                self.new.destroy()
            
        
        self.new.bind('<KeyPress>', on_key_press)   
        self.buttons=[]
        for i in range(self.rows):
            row=[]
            for j in range(self.columns):
                if self.immortalcell!=[] and self.immortalcell[i][j]==1:
                    button=tk.Button(self.new,bg='red',width=1,height=1)
                elif self.deadcells!=[] and self.deadcells[i][j]==1:
                    button=tk.Button(self.new,bg='black',width=1,height=1)
                else:
                    button=tk.Button(self.new,command=lambda r=i,c=j:self.user_selection(r ,c),width=1,height=1)
                button.grid(row=i,column=j,sticky='nsew')
                row.append(button)
                self.buttons.append(row)
            
        self.new.wait_window()
        
        for i in range(self.rows):
            self.array.append([])
            for j in range(self.columns):
                
                if [i,j] in self.array_cord:
                    self.array[i].append(1)
                else:
                    self.array[i].append(0)
        
        
        return self.array
    
    def immortal(self):
        self.immortalcell=self.make_array_users()
    
    def dead(self):
        self.deadcells=self.make_array_users()
    
    
    def make_array_random(self):
        array=[]
        for i in range(self.rows):
            array.append([])
            for j in range(self.columns):
                array[i].append(random.randint(0,1))
        
        return array
        
                
    def user_selection(self,i,j):
        for widget in self.new.winfo_children():
            if (i==widget.grid_info()['row'] and j==widget.grid_info()['column']):
                widget.config(bg="green")
                self.array_cord.append([i,j])
        
    def clear(self):
        self.pause()
        self.programm.destroy()
        ConwaysGameOfLife(self.rows,self.columns,self.sizeofcell,self.speed)

    
    def create_label(self):
        self.generation = 0
        self.label = tk.Label(
            self.programm, text=f'Generation: {self.generation}')
        self.label.pack()
    
    def update_generation(self):
        self.label.config(text=f'Generation: {self.generation}')

    def draw_grid(self):
        
        for row in range(self.rows):  
            for col in range(self.columns):  
                x1 = col * self.sizeofcell
                y1 = row * self.sizeofcell
                x2 = x1 + self.sizeofcell
                y2 = y1 + self.sizeofcell
            
                if self.immortalcell==[] and self.deadcells==[]: 
                    if self.grid[row][col] == 1:
                        self.canvas.create_rectangle(
                            x1, y1, x2, y2, fill='green', outline='black')
                    else:
                        self.canvas.create_rectangle(
                            x1, y1, x2, y2, fill='white', outline='black')
                else:
                    if self.immortalcell!=[] and self.immortalcell[row][col]==1:
                        self.canvas.create_rectangle(
                            x1, y1, x2, y2, fill='red', outline='black')
                    elif self.deadcells!=[] and self.deadcells[row][col]==1:
                        self.canvas.create_rectangle(
                            x1, y1, x2, y2, fill='black', outline='black')
                    elif self.grid[row][col] == 1:
                        self.canvas.create_rectangle(
                            x1, y1, x2, y2, fill='green', outline='black')
                    else:
                        self.canvas.create_rectangle(
                            x1, y1, x2, y2, fill='white', outline='black')
                 
    def update(self):
        if self.check>0:
            self.check=0
            return 0
        new_grid = []
        for row in range(self.rows):
            new_grid.append([])
            for col in range(self.columns):
                
                if self.immortalcell==[] and self.deadcells==[]:
                    new_grid[row].append(self.get_new_cell_state(row, col))
                
                elif self.immortalcell!=[] and self.immortalcell[row][col]==1 :
                    new_grid[row].append(1)
                elif self.deadcells!=[] and self.deadcells[row][col]==1:
                    new_grid[row].append(0)                    
                else:
                    new_grid[row].append(self.get_new_cell_state(row, col))


        self.grid = new_grid
        
        self.canvas.delete('all')
        
        self.draw_grid()
        self.programm.after(500//self.speed, self.update)
        
        self.generation += 1
        self.update_generation()
    
    def get_new_cell_state(self, row, col):
        
       
        num_neighbours = self.get_num_neighbours(
            row, col)
       
        if self.grid[row][col] == 1:
            
            if num_neighbours < 2:
                
                return 0
            
            elif num_neighbours == 2 or num_neighbours == 3:
                
                return 1
            elif num_neighbours > 3:
               
                return 0

        else:
            
            if num_neighbours == 3:
                
                return 1
            
            else:
                
                return 0

    def get_num_neighbours(self, row, col):
    
        num_neighbours = 0
        for i in range(-1, 2): 
            for j in range(-1, 2):  
                if i == 0 and j == 0:
                    
                    continue
                
                neighbour_row = row + i
                
                neighbour_col = col + j
                
                if neighbour_row < 0 or neighbour_row >= self.rows or neighbour_col < 0 or neighbour_col >= self.columns:
                    
                    continue
                num_neighbours += self.grid[neighbour_row][neighbour_col]
        return num_neighbours

    def run1(self):
        self.grid=self.make_array_random()
        self.update()

    def reset(self):
        
        self.grid = self.make_array_random()
        self.canvas.delete('all')
        self.draw_grid()
        # Reset the generation
        self.generation = 0
        self.update_generation()

    def change_speed(self, speed):
        self.speed = int(speed)

    def run2(self):
        self.grid=self.make_array_users()
        self.generation = 0
        self.update_generation()
        if self.grid!=[]:
            self.update()
        
    def wait(self):
        if self.new==1:
            return 1
        else:
            return 0
    def pause(self):
        self.check=1
    def bcontinue(self):
        if self.grid==[]:
            for i in range(self.rows):
                self.grid.append([])
                for j in range(self.columns):
                    self.grid[i].append(0)
        self.update()
    

class MainWindow:
    def __init__(self,root):
        self.root=root    
        self.root.config(bg='lightblue')
        self.x=10
        self.y=10
        self.cellsize = 4
        
        self.frame1=tk.Frame(self.root,bg='lightblue')
        self.frame2=tk.Frame(self.root,bg='lightblue')
        self.label=tk.Label(self.frame1, text="Conway's Game of Life", font=("Arial", 18), bg='lightblue')
        self.sliderX=tk.Scale(self.frame2,from_=20,to=40,orient=tk.HORIZONTAL,label='Width',font=("Arial", 12),
                                command=self.updateX)
        self.sliderY=tk.Scale(self.frame2,from_=20,to=40,orient=tk.HORIZONTAL, label='Height',font=("Arial", 12),
                                command=self.updateY)    
        self.sliderCell=tk.Scale(self.frame2, from_=10, to=20, orient=tk.HORIZONTAL, label='Cell Size',
                                   font=("Arial", 12), command=self.updateCellSize) 
        self.startButton=tk.Button(self.frame2,text="Start Simulation",font=("Arial", 14),bg='lightgreen',
                                    command=self.startProgram)
        
        self.sliderX.set(self.x)
        self.sliderY.set(self.y)
        self.sliderCell.set(self.cellsize)
        
        self.frame1.pack(fill='both', pady=20)
        self.label.pack()
        self.frame2.pack(fill='both', side='bottom', padx=50, pady=20)
        self.startButton.pack(pady=10)
        self.sliderX.pack(pady=10)
        self.sliderY.pack(pady=10)
        self.sliderCell.pack(pady=10)
        
        self.root.mainloop()

    def updateX(self, x):
        self.x = int(x)
        
    def updateY(self, y):
        self.y = int(y)
        
    def updateCellSize(self, cellsize):
        self.cellsize = int(cellsize)
         
    def startProgram(self):
        game = ConwaysGameOfLife(self.x, self.y, self.cellsize, 1)
    

if __name__ == '__main__':
    root=tk.Tk()
    root.geometry("700x500+540+200")
    main=MainWindow(root)
    
