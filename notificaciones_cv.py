#!/usr/bin/env python3

'''
Bot que muestra una notificación cada vez que se realiza un cambio en el campus virtual de la USC en las URLs indicadas

Instrucciones para un correcto funcionamiento del bot en 


© 2022 Toi1000, Santiago de Compostela, España © 
'''



# -----------------------------------------------------------------------------
# ------------------ MODIFICA ESTO CON TUS DATOS Y URLs -----------------------

URLs = ['https://cv.usc.es/course/view.php?id=27310',
        'https://cv.usc.es/course/view.php?id=27665',
        'https://cv.usc.es/course/view.php?id=27310',
        'https://cv.usc.es/course/view.php?id=27312',
        'https://cv.usc.es/course/view.php?id=27664',
        'https://cv.usc.es/course/view.php?id=28917']

# nombres de las asignaturas
subjectNames = ['COGA', 'ARQCOMP', 'BDII', 'DISEÑO', 'SOII', 'XEFE']

# imagen con el logotipo del icono
img = "logo.png"    

# completa con tu username, password y execution (disponible en github como obtener esta información)
payload = {
    'username': 'oscar.toimil@rai.usc.es',
    'password': '0sc4r$T01m1l',
    'execution': '784f636f-a7f7-4dba-b53b-4b05bb7ae115_ZXlKaGJHY2lPaUpJVXpVeE1pSXNJblI1Y0NJNklrcFhWQ0o5LjNBdUY0b0h2MkZpWUNhVXFUYjFIazR0TGdpU1M5aVFRQ3V3aUJRd1lLQ252NmVfcjNoRDFQMHdiX0RYS2pCeTJ5VjlNejZKSlk0V0E0dXpUTG5RZDZTRFZVUUd6a1VGQmVwV2pBbEJ3NmVuUTliSnBmQi0tTDZoX2hHU0tSQlM3WjZVZHZQbjNmSmpMS1Z4T1p2eldPQVQ2dEpaSFc4bWp6dHhQWXZvMl82MGllS2dNNk5nVVVnWVE5MEMzYlZQR0syeVZmRUUtR2thdGZfZjJibXNoY0szdGFUYXN4V0lTX2ZVUlJZbnB5M1BNNndKQ2EycWVhU2xEUlM1cEM4RElxcDJPYkZHOE9fenFiTV9TVmVOdGV0N0tsUXY5V1BxZVpEdmhNUWRfVjdocThFSXV4TjJMalRrYVJJVmhWaGxvM05veFRXQ3llTGRRLV9MNHFnT2VMRERpemVINl9ZaVZZREpXRmZWbktBWjdhTlBIa21Cdm1uTWR5RVFaM3ZfS0kzdVdpbllSdWIwd0dFdV8yWUZ5cDBvZC1va0huMGI4Tm9MTW9oeFVHQTNLU2M1bkM5N1Zyc0tVb05ZN0NLMzR4U3F1cnQ1eXFncnlveWNQdi03dDY1R2EtYzU3bDRybVRhaDBfVXN0NEx5QXBpYm9VczJRbDJBMjhybVZrN3Y3dlcteTNVc1hocWhkcGV0OVJLTDBjWURNRkpXdFl3SnZqUGpGU0NZYU1KTmQ3ME54YWd1b2toSkFrUVlqSHlZaGVkVUp5WEVYaE41NEswLUlnaTBtd3dqTXBJQS1UNnNYVmpPSGRlYUxrTm94Sm9VWFJtdzFXbHZta1N6Z3ZRUkdJUmFpVE9Kclp2YzBsNVBPN0RCMUp3b1Vub2M2cVYzTGhwRmVmOGZKTVVDODhnZ0ZQR2ZRUmtvSFdDU2xRbkpNOEttaEZBUWd6S0hTMlFCc05VUGN1M25ubzFvMFU5ZC05VmJreUhHeFJhWjdpakowTWlHUFYwdHZlMDdIS0ZkNnplSW1wdi1tOFNSQ1dpSTV4U0JDOE1oUDRTVFRFSnJXZmNxMFFJTElycU9wUmtEamtsQjBKT3cxM1dpYkV1WFV1aFV4TERnTmViS1YwTXVTcWpRb19JYXprV2xxZ1FWbUlIY1BZc3QxUlJIVlJfeXJxVzJ0RmExVXZhWWNQbjVSTVl2TndQeFpHS2RVWVlYNHMtUExxWEcweXFKVHpGQXdQdGJiUmVmY0paV3dBVjBFVjBmS2RGRDVXTnByU1NsUmVOcno2S1ZOZjRpdk1yMHQ2N0tjTDlTVURpd3d4QVV6dzY2Uk96LWpIanYzZ2RCZUljUHpFcmhjU0ZScVFsVXQwTXI3VVVjV0FRLUozYktLdnhVWDlLSW9ueHNsNDI3TFU3WnNUZHBkXzlSVi14OTRMOU9ndmExUkJOTXdmM0xuTDJ4WGRqVFZaWGxTd29yOHRzQjFLYmZQc1RqV2tGN0RKc0VybE12UEdlYTI5Y3VPNTh0YlZ1eVhuLWVkaTdRMG03Q1daS295LVgwV09JMTIyU0NqX2NpNWM4S0NWeV8yLXJBaTVKaGZ1ejdxSXhnU3EyekJFbzlvV1lzZ0RHQUxHYTB3LU5XbFc5SC1mUmhKM2hEbmo1aGxjcEZFeFhQMVlQanp0Y3BkaDh3RGxKNWVTdFcxUzNKSXlaU0RZN0lCNU1ZVk40dXc1a2pxajNDWEFkcUJYbWxZMzZPd3VNTXR5MFZhUjhKYnJqak52WHBqaWlIRUpvU1k3OXZSelZCNmdTb3JXeThmMUZ6QmhXXzgyQlhTQVhHNjZEQkNlU3hCQTdwdzlPMUNKWk1yWGg4MmtTMTNmYjB4ZktNOFZsU0EwYWRJUzE1Slp5a1RPeVBvQjg5TlNHcGw1UDdIV09QbHg0ajJpb2FSLTc1UkNPZFZfSVpCYzQxLUF0dm42UHA3S1laZWEtUi04QXdHSmE4SExxSi1YczB4dWU2eVhzUnhjM0Zpc1RscHg1dWFETTlxMTJXVjkxdU9id1hqSFRCdFRZWW9GWFhadWpTMXA3dE5DQnB6M0JyVmtRWE9mRHZjLUlJeHdOZU5SQng5by02LVk3NzdhS25fSnNaVUJ3OFllaWFzN1lWMDlxZ2xmUlB0Z3ZQdnZDLVBsZE45TElHd1NacDNZeEs1ZmNzVnhqMm5HMjZJMGExaUtjc091UTFtdzhKZDlzUFNuOHdqMGt3amd5UFNfelZTZ2pOWHNXM2t2RHFxOUYtRmNmWTRHZ0Jsdkxud3N1X09MdUhtQ1JLUExEUENsdW9QY0hVRm5LUllQU3piZ2x4TFZqX04wODZ4cFB0VFRkQnV0bzZLU1ltelpVUzYtNVUydFdsT0RtSUhmRG9xdXJBa3dnbTNMVDBlc0MwdmhVTFp2TzN3MVJiWGU3b0tYSl8wR1ZiQWNDOWV4Y1AzVXVzRGMyVjQ0ZTk3SHRseGlpN1J2S2p4ZUFEQlhOb3VUUkE2SWlYT1EtODZXaksxMUJtM0hpUFlwMFI0NnRlYVNKbVoxdTVSOS04UzAzX2c2SkpEemdTbHZWQkRGZ3FIaDB2eVVxRHpCaVF2WVUwYmJsdkY3MzRCTk1fdWF6SmQwd3pReTk3ejBKZGxhNTNuVmo3TUtsbEVqNHlLZGtoRGl2Ri1TSUVRSDBLZExwQUc5Tnd6NVNGWnUxa01ta2ctczJpTkoxQTdFX2ZlQVByVTJJY3JYb0hlU0dnZHQwX2p1R3BVN2lNbkp0dGhWRHh6bmNSM2RPdXkycE44QjZyXy1WekJHU3JFQ25UZWJvMFIzc1UzVktTN0JrVUpiMnpKanRuLWlndEgwVWx2OVg0N1ZqWmUwaVo3U1Y3VFZwNUZZNXN5MXBmaGJDRVJGbl9nSmVRaFBmWTVuMUlvSW1FX3dSckNqMnpEWWpUYnlBajdqY3FrcFc2dlRmbW9xN3B3eUo3RzQ3b280dmMteHRCWlpfZU1iWEJ2MEM3Qk1XWk5rR181LV9Qd1ZaVmlRcWFxaTdyQUZ1UGhHeGYxdzRMTGY2U05hVFR6YWtzZTRTNjBiTGJWU28xMWxhczNPZFpudFppNXczVE5HV0xoVkJJZ0FtLVpZRVFHLUlqZXIzX0NScTE4eXJiRGY5MnVXV0pQNDQ1MktfOEpZRFBIdFZUNzlvM0tQcFhtS2JVaS1NeGZLX044dFhadUVkMER4dGdURFhtcTFNNjJ3NURKUXVfUTc4b1UyMUtkdFdBRmR3MDhaZXZDa3FvTWI5NHQ0dXlfc3I4NDZfRzQ4Sk13SnJpUUpwcXE2OW54ZjRBWGNvRUVtUERTWjZOa2JOcFlNdWVpYVpZdmVJNWszQjZ4N1g3UGMyci1DOWt1ZUxEd2VOZDdCZWJQSDNuUmVHMjU1VzRDbWJ3YjdYNE56elRVYlNCRW1HRUZJRHp4c0Vab0VQZGU2ajM1eHlPQzN2LTlrQXlTU3lXYVBlVmx4cjBKbjc4dGEtOFBDcDZxb2Zmb2Z3NnFMb2kzcW5SdnpSZjFTdWhuRVRqVkZLSTI2Xy0tY1MzOEtXRUFwMngyMnlXYWNraVVBbUJIbXRzazlpZjNEZkFROWF0V1BVUWMzNWlQaGlQZDU2bTJPV2piX3NGc3NFWE1nVFlDRm1zTnlVSWpfYmMyLTl1eU1NdFFuZHpXZzN5cnJvTUF1TVJKY1JEZjlvM19acy14OWpKOFJGUU1ZMEs4ZG11N1Z4M0NZZ2NLMEJTdlU2a3NpUVZ6QmUwcWlsR2xiN2xlSnFaWER6a1lMb2pfblVyWWZmQjFTSk41UFhRa2FZZ0FWVWhDNzRIb0RPSDdnZURtQk1zZnB0VGNackt3N3YzUmY4ZVBBTW1nLXA4dHFJd1k2clBjNDBKYlRadkdVYlU5bUREandac010UzZrb1JIY1U4VklsZDlINWpfSERoZ3YwRTBHc012NHdpR2NBeWtKeHU4clFfX0oxV21qeWV3N1BqZ0w4YW9hc0dJODN2NE8wTEluNXltazd0b1BVMjZOS0xydENpOEtudDVxVFRzRWZ0VmZRalFHR1Vpcm9EczFQY0pZMkNienBOYnBtbmFTcmZZTHZpU01HNzVxc2hZVWttUjZDUUFqR216c0RDZXFVaTV4cXFWLUY5MTdiQl9NUVpMMmM0NlB3WjlQV3RwVXFCOUt2aG5MOFBQb0U1SnhtYVJDZU1QNGZkcjYxbnlZN1BSVy02aEdOMHhHS2RuNjNESUN3NHczaWVGeUJnM3pNUWlJTEg0U1JYMHN5WFVTa0RYY0VtazJXaVhMTmI0OEhsQ0s1Q1hKQkg5Q0taOWtlcloyNmNvcjE1RDBHZmNlNnB2TTlXbHhiSU1xS0EtSmtfaDlTSDZuVDFlZnY5aThOOG5ycHdHN21DUnJLZnA2VGdiVWIxSEJrVVU2SkFlNThrQlZkQWlxZWV5NUV4UE9paGZoWE55Vzk5RklOM19xZDRON2JIUlQzRm9oRjVUM0Y3eFVZWkk0Um9RbGpTTGVhb0lRMFRtLW9MR3otdm9zcExtNkRZY1JNUFBqWTN2eTYtWFY4RzFubzhWNVhJSGZ5c2Vsd1dEMk10OUxJLTE5ckFWaTk3eHhXM01RRWduRWJMSjBJMzE5MGxBQm9BNHVkN1hSOEpDenY2Sms2OG1HZjBQQzYyaUM1UWFqWWhCc3JVTHhsQThuSHpCUURlNW43R1AzZExUNTdqcWFfLS1zaWpLQlZFNEVYMmh1V1FjTXY0NzJIMlk1RklieGJxbnZfY1BrWi1YV2VwTTQ3SWtfbnAzYi0wd1BnMEEyTVRmM240UWd6RzZ3SmFxakx6Uk9EY253RThWSnVwVDdmMVhfazZ2U1lJS3lUVnVXR0xFZ2JaWnJiek9mT0RBQ1BVcm9MS0ZmaEoxQ3FyakFTS2VFNjQtNG8wdE1aNFZJV0U1UU5sNXF2ZlBEQUN4X3NMaHhQaWV4UTdfNHNrTHphYUdDQ3pUeFFzMFNPWURQNXRFWkxyQnhzUmFOR1E4MEY5bmFLOGowVmNqbGZ1TW5MTnBaWHA5bmlkWGxqdDBvTC14OFNwelZPMXktQXJ2cXNuSDFnN25pQVEtTnBxcUVGX21fcVZlMkFFQ2lFYlhEbXRNcEhQb0h3VmFVeEVpZE5wVk9GUkRLT0pzRnE2dTZyNk5BaFdFWnlEbjdwSnZFeU9oOWlqTXNpNVRLeW1Ianhza0tRWlNXRHdYcFBtU21ZQUwtN0RLZE8xei05bGNaWlQ5Vk84eC01enRhU2FucExzbW9KbW16NGF4RnA1OS1yZ0J1QURsQ090RHpKVkpWeWtuek1zMnVxQUFfVHYxVE16TnZuNWJFckJlZ1FiS3I5NWpFc0ZCdjBZa1dhQnEtQkhoY3ltdHY0U0dwLVB6RE5HS0ZJdkVZZGc0dHRDWGlPMEFCTzVKMlZDemlBZDVLUWdJNEY5b3VQRGI2VjF4N3kxb19PYy1ibGVRX0otZ2tGbF84VlhVRXBrQVFEWVl0OTg5VFBnbFZfX3M0NlpYMTZEbkh6NmVRSEduaHN3aEdwOVp6M1d5WFlhMWdCRWtZc283R3FoV0Z1cm9Tb0FEM2hXZUtaNnhBRlM0bkU5bnhVR05rakVrTzFNWUg3bjdMU2pxaHZTam16RTRDQlVIN0lyYlRwb2UtaEN1VTg0b0pBZkNaRHpyWEc4LVl1RTFLRzBYWHo5NERfVzM1RmcxVkpMcnkzRFFuV2xTTDRMR2pUY1RBbGhMbnBRMUp1akpTeW4zdnp2dk9EQklhRklQbC03RnE1ejJtbUhYSVlZaUw3NFNKbUpmbkFQUnZjcXdTRVdQTTgyLW5UWU55c2VuNWpGSHBUU2Z4ZDF1a3dZY3NNTkNUMjdvQjExZFc3NVNlY3h4OW1reDdHd1ZpbEU1cHpBMW0yelIwVmNSWld2R21laWpHTEFqRWhwWHR4MTlpeFExRy43dmlJUW5QRHVhUHloQWYyMlpDZllLVlg1ejJjbmtQY1Fxb2NRZG9ad3BVcWxadWMzWmtrdnRtREROMkhCZEh4NVhOb2Q4MXRLTl9uMzNhS0tkQTVYQQ==',
    '_eventId': 'submit',
    'geolocation': '', 
    'submit': 'Login3'
}
# -----------------------------------------------------------------------------





# realizamos los imports necesarios
import requests
import time
from win10toast import ToastNotifier
import pystray
import PIL.Image
import os


# comprobaciones
if (len(URLs) != len(subjectNames)):
    print("Error al introducir las URLs o los nombres de las asignaturas")
    print("Deben existir tantas URLs como nombres de asignaturas")
    os._exit(1)



def check_string(a):
    """Comprueba si existen las palabras 'Sen actividade recente' en el archivo pasado como parámetro
    return boolean true si esas palabras se encuentran en el archivo o false en caso contrario    
    """
    with open(a, encoding="utf-8") as temp_f:
        datafile = temp_f.readlines()
    for line in datafile:
        if 'Sen actividade recente' in line:
            return True
    return False


def on_clicked(icon, item):
    """Cuando se pulse en el item del icono se terminará el programa
    """
    icon.stop()
    os._exit(1)



toaster=ToastNotifier()   # notificacion
image=PIL.Image.open(img)  # abrimos la imagen
# creamos el icono con un item que será salir
icon = pystray.Icon("ToiBot", image, menu=pystray.Menu(
    pystray.MenuItem("Salir", on_clicked)
))
tam = len(URLs) # número de URLs



def cv(icon):
    """Realizamos el login en el campus virtual de la USC y comprobamos si se realizaron cambios en las URLs indicadas previamente
            en el caso de que se haya hecho un cambio, mostramos una notificación por pantalla
    """
    icon.visible = True
    with requests.Session() as s:
        while(1):

            p = s.post('https://login.usc.es/cas/login', data=payload) # logeamos en el campus virtual


            for i in range(tam):
                r = s.get(URLs[i])
                file = open(subjectNames[i] + ".txt", "w", encoding="utf-8")
                file.write(r.text) 
                if not check_string(subjectNames[i] + ".txt"):
                    toaster.show_toast("Campus Virtual", subjectNames[i], duration=30)
           
            time.sleep(60.0) # cada minuto comprobamos si se realizó algún cambio
        
icon.run(cv)
