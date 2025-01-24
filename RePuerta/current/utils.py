import csv
from django.conf import settings
import os


def search_in_csv(height, width):
    # Pfad zur CSV-Datei
    csv_file_path = os.path.join(settings.BASE_DIR, 'csv_match/products.csv')

    results = []

    # Öffnen und Lesen der CSV-Datei
    with open(csv_file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        # Durch die Zeilen der CSV-Datei iterieren und nach Höhe und Breite suchen
        for row in reader:
            # Vergleiche Höhe und Breite
            if int(row['height']) == height and int(row['width']) == width:
                results.append(row)

    return results
