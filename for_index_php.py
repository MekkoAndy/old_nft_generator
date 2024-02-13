import numpy as np
import csv

path = "/Users/andrew/Coding_stuff/Python/#40_Anime_anim/Metadata/"
path_meta_2D = "/Users/andrew/Coding_stuff/Python/#40_Anime_anim/Metadata/items_log_#40_Anime_anim.csv"
tokens_amount = 5555
main_np = []


with open(path+'meta_for_php'+'.txt', 'w', newline='') as txt_file:
    fieldnames = [
        'items',
        'total_scores',
        'rarity_category',
        'name'
    ]
    writer = csv.DictWriter(txt_file, fieldnames=fieldnames)
    with open(path_meta_2D, 'r', newline='') as csv_file:
        csv_file_reader = csv.reader(csv_file)
        o_bot_2D_items = [row for row in csv_file_reader]
        for img_name in range(tokens_amount):
            if img_name in [0, 666, 2345, 4567, 5554]:
                rarity_category = '影-Kage'
                names_score = 2000
            elif img_name in range(1, 23):
                rarity_category = '上 忍-Jōnin'
                names_score = 600
            elif img_name in range(23, 5001):
                rarity_category = '下忍-Genin'
                names_score = 200
            elif img_name in range(5001, 5101):
                rarity_category = '特別 上 忍-Tokubetsu_Jōnin'
                names_score = 1400
            elif img_name in range(5101, 5501):
                rarity_category = '上 忍-Jōnin'
                names_score = 2000
            else:
                rarity_category = '中忍-Chūnin'
                names_score = 2500
            writer.writerow(
                {
                'items':o_bot_2D_items[img_name+1][-3],
                'total_scores': int(o_bot_2D_items[img_name+1][-1])+names_score,
                'rarity_category':rarity_category,
                'name': img_name
                }
            )

np.save(path+'meta_for_bpy.npy', main_np)
