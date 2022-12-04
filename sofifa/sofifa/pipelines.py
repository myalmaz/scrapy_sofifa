# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class SofifaPipeline:
    def process_item(self, item, spider):
        return item


 get_pos_reg(pos):
    return {
        'GK': 0,
        'CB': 3,
        'LB': 4,
        'RB': 4,
        'CDM': 5,
        'LWB': 6,
        'RWB': 6,
        'CM': 7,
        'LM': 8,
        'RM': 8,
        'CAM': 9,
        'LW': 10,
        'RW': 10,
        'LF': 11,
        'RF': 11,
        'CF': 11,
        'ST': 12
    }.get(pos, 0)    # si no encontramos la posicion devolvemos 0 que es GK


def get_pos(posicion,posiciones):
    equivalencias= {
        0: 0,
        2: 1,
        3: 2,
        4: 3,
        5: 4,
        6: 5,
        7: 6,
        8: 7,
        9: 8,
        10: 9,
        11: 10,
        12: 11