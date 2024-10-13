import os, platform, zipfile
from datetime import datetime
if (platform.platform().startswith("macOS") or platform.platform().startswith("Linux")):
    os.system('clear')
else:
    os.system('cls')

""" * EJERCICIO:
 * ¿Has visto la camiseta.rar?
 * https://x.com/MoureDev/status/1841531938961592740
 *
 * Crea un programa capaz de comprimir un archivo 
 * en formato .zip (o el que tú quieras).
 * - No subas el archivo o el zip."""


# for i in range(5):
#     with open(f"#41 - ZIP/files/file{i+1}.txt", "w") as file:#Abriéndolo con with el archivo se cierra automáticamente 
#         file.write(f"Este es el fichero nº {i+1}")# cuando termine el bloque de código tabulado.

current_datetime = datetime.today().strftime("%Y_%m_%d_%H_%M_%S")
backup = "#41 - ZIP/files"
zip_path = f"#41 - ZIP/files/python_zip{current_datetime}.zip"
os.chdir(backup)
files_folder = os.listdir("./")
zip_file = zipfile.ZipFile(zip_path, "w")

for file in files_folder:
    zip_file.write(backup+file, compress_type=zipfile.ZIP_DEFLATED)
zip_file.close()