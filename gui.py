import customtkinter
from modCalculator import modCalculator

class ModulusCalculatorGUI:
    def __init__(self):
        self.app = customtkinter.CTk()
        self.app.geometry("400x250")
        self.app.title("Modulus Calculator")

        self.a = customtkinter.CTkEntry(self.app, placeholder_text="Enter a", width=150)
        self.a.grid(row=0,column=0,padx=20,pady=10)

        self.b = customtkinter.CTkEntry(self.app, placeholder_text="Enter b", width=150)
        self.b.grid(row=1,column=0,padx=20,pady=10)

        self.equation = customtkinter.CTkLabel(self.app, text="a mod b =", font=customtkinter.CTkFont(size=15, weight="normal"))
        self.equation.grid(row=2,column=0,padx=20,pady=10)
        
        #Add action to calculate button
        buttonCalc = customtkinter.CTkButton(self.app, text = "Calculate", command = self.buttonCalcAction) 
        buttonCalc.grid(row=3,column=0,padx=20,pady=12,sticky="ew")

        buttonReset = customtkinter.CTkButton(self.app, text = "Reset", command = self.buttonResetAction)
        buttonReset.grid(row=4,column=0,padx=20,pady=12,sticky="ew")

        self.app.grid_columnconfigure(0, weight=1)


    def buttonCalcAction(self):
        try:
            aInteger = int(self.a.get())
            bInteger = int(self.b.get())
            result = modCalculator(aInteger,bInteger)
        except ValueError:
            self.equation.configure(text="Error: Please enter valid integers.")
            return
        except ZeroDivisionError:
            self.equation.configure(text="Error: Divisor b cannot be zero.")
            return
        self.equation.configure(text=f"a mod b = {result}")

    def buttonResetAction(self):
        self.a.delete(0, 'end'), 
        self.b.delete(0, 'end')
        self.equation.configure(text="a mod b =")

    def run(self):
        self.app.mainloop()

if __name__ == "__main__":
    gui = ModulusCalculatorGUI()
    gui.run()

        

        

       
       
        

        