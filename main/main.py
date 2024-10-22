import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
 
import model.clientes  as cl
import ui.ui as ui

def main():
    ui.menu()