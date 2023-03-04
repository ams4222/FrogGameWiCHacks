import ctypes
import time

#basically what happens in keys get pressed instead
SendInput = ctypes.wind11.user32.SendInput

space_pressed = 0x39

PUL = ctypes.POINTER(ctypes.c_ulong)
#class KeyBdInput(ctypes.Structure):

#class HardwareInput(ctypes.Structure):

#class MouseInput(ctypes.Structure):

#def ReleaseKey(hexKeyCode):

#if __name__ == "__main__":