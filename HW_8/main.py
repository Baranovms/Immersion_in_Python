from lib_func import tools as tls

JSON_FILENAME = "relust_.json"
CSV_FILENAME = "relust_.csv"
PICK_FILENAME = "relust_.pcl"

if __name__ == '__main__':
    dir_info = tls.dir_info()
    print("Сохранение информации в файлы")
    tls.save_to_json(dir_info, JSON_FILENAME)
    tls.save_to_picle(dir_info, PICK_FILENAME)
    tls.save_to_csv(dir_info, CSV_FILENAME)

    print(f"Информация в файлах: {JSON_FILENAME}, {CSV_FILENAME}, {PICK_FILENAME}")