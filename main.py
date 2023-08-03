#-------------------------------------------------------------------------------
# Name:         Main
# Purpose:      Script que permite imprimir documentos en impresora predetermindad en el equipo.
#
# Author:       Fredys Barrera Artiaga <fredys.barrera@arauco.com>
# Created:      27-07-2023
# Copyright:    (c) Arauco 2023
# Licence:      <your licence>
#-------------------------------------------------------------------------------

from datetime import datetime
import win32print
import traceback
import win32api
import sys
import os

script_dir = os.path.dirname(__file__)

def main():
    """Main function."""

    try:
    
        # Parámetros
        fileName = sys.argv[1] 
        copies = sys.argv[2] 

        print('param1=', fileName)
        print('param2=', copies)

        # fileName = "test1.pdf"
        # copies = 1 

        scriptDir = os.path.dirname(__file__)
        pdfFile = os.path.join(scriptDir, fileName)

        name = win32print.GetDefaultPrinter()
        print(name)
        
        #printdefaults = {"DesiredAccess": win32print.PRINTER_ACCESS_ADMINISTER}
        printDefaults = {"DesiredAccess": win32print.PRINTER_ACCESS_USE}
        handle = win32print.OpenPrinter(name, printDefaults)

        level = 2
        attributes = win32print.GetPrinter(handle, level)

        #attributes['pDevMode'].Duplex = 1    # no flip
        #attributes['pDevMode'].Duplex = 2    # flip up
        attributes['pDevMode'].Duplex = 3    # flip over
        attributes['pDevMode'].Copies = int(copies)

        ## 'SetPrinter' fails because of 'Access is denied.'
        ## But the attribute 'Duplex' is set correctly
        try:
            win32print.SetPrinter(handle, level, attributes, 0)
        except:
            print("Failed win32print.SetPrinter (%s)" % traceback.format_exc())
            error_log("Failed win32print.SetPrinter (%s)" % traceback.format_exc())

        win32api.ShellExecute(0, 'print', pdfFile, None, '.', 0)

        win32print.ClosePrinter(handle)
    
    except:
        print("Failed main (%s)" % traceback.format_exc())
        error_log("Failed main (%s)" % traceback.format_exc())


def error_log(text):
    """Registra un log de error. """
    try:
        log_file = os.path.join(script_dir, 'error-log.txt')
        f = open(log_file, "a")
        f.write(
            "{0} -- {1}\n".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), text))
        f.write("---------------------------------------------------------------- \n")
        f.close()
    except:
        print("Failed error_log (%s)" % traceback.format_exc())


if __name__ == '__main__':
    main()