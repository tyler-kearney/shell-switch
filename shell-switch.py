import tkinter as tk
import subprocess as sp

def install_shell(shell, package_manager):
   try:
        sp.run([package_manager, shell], capture_output=True, check=True)
   except sp.CalledProcessError as e:
       print(f"Error installing shell: {e}")
       
def switch_shell(shell):
    try:
        sp.run(["chsh", "-s", f"usr/bin/{shell}"], capture_output=True, check=True)
    except sp.CalledProcessError as e:
        print(f"Error switching shell: {e}")
        
def shell_switch_btn_click():
    selected_shell = shell_var.get()
    package_manager = txt_package_man.get()
    install_shell(selected_shell, package_manager)
    switch_shell(selected_shell)
    
root = tk.Tk()
root.title("Shell Switch")

shell_var = tk.StringVar(value="bash")

bash_rdo = tk.Radiobutton(root, text="Bash", variable=shell_var, value="bash")
bash_rdo.pack()

zsh_rdo = tk.Radiobutton(root, text="Zsh", variable=shell_var, value="zsh")
zsh_rdo.pack()

fish_rdo = tk.Radiobutton(root, text="Fish", variable=shell_var, value="fish")
fish_rdo.pack()

package_man_lbl = tk.Label(root, text="Package Manager: ")
package_man_lbl.pack()

txt_package_man = tk.Entry(root)
txt_package_man.pack()

shell_switch_btn = tk.Button(root, text="Switch Shell", command=shell_switch_btn_click)
shell_switch_btn.pack()

root.mainloop()