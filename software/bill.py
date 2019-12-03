# -*- coding: utf-8 -*-
"""
Created on Tue Jan  1 09:55:21 2019

@author: Hamza Khalid
"""
import numpy as np
import xlrd
import pygame
import pymysql.cursors

pygame.init()
display_width = 250
display_height = 150
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Energy Meter')
clock = pygame.time.Clock()
white = (255,255,255)


loc = ("os.xls")
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
sheet.cell_value(0, 0)
rows = sheet.nrows - 1
cols = sheet.ncols
array_length = rows * cols
temp_line =  [ '' ] * array_length

def meterloop(temp_line):
    gameExit = False
    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
        gameDisplay.fill(white)

        size = [display_width, display_height]
        screen = pygame.display.set_mode(size)
        basicfont = pygame.font.SysFont(None, 24)
        text = basicfont.render('Software Reading Bill File...', True, (0, 0,0))
        textrect = text.get_rect()
        textrect.centerx = screen.get_rect().centerx
        textrect.centery = screen.get_rect().centery

        screen.fill((255, 255, 255))
        screen.blit(text, textrect)



        lines = []
        try:
            # Give the location of the file
            loc = ("os.xls")
            wb = xlrd.open_workbook(loc)
            sheet = wb.sheet_by_index(0)

            sheet.cell_value(0, 0)

            rows = sheet.nrows

            for count in range(1, rows):
                f = sheet.row_values(count)
                for line in f:
                    lines.append(line)
            a = len(lines)

            if a > 1:
                    if np.array_equal(lines, temp_line) == False:
                        print("Data changed")

                        for x in range(0,array_length-1):
                            temp_line[x] = lines[x]
                        print(lines)
                        print(temp_line)

                        for i in range (0,array_length-1,cols):
                            unit = temp_line[i+0]
                            charges = temp_line[i+1]
                            meter_number=temp_line[i+2]
                            location=temp_line[i+3]
                            past_unit=temp_line[i+4]
                            current_unit=temp_line[i+5]
                            consumed_unit=temp_line[i+6]
                            charges_per_unit=temp_line[i+7]
                            total_charges=temp_line[i+8]
                            tax=temp_line[i+9]
                            bill=temp_line[i+10]

                            try:
                                # Connect to the database
                                connection = pymysql.connect(host='127.0.0.1',
                                                             port=3306,
                                                             user='root',
                                                             password='',
                                                             db='energymeter',
                                                             charset='utf8mb4',
                                                             autocommit=True,
                                                             cursorclass=pymysql.cursors.DictCursor)

                                with connection.cursor() as cursor:
                                    if i == 0:
                                        sql1 = "TRUNCATE TABLE bill"
                                        cursor.execute(sql1)
                                    sql2 = "INSERT INTO `bill` (`unit`, `charges`,`meter_number`, `location`, `past_unit`, `current_unit`, `consumed_unit`, `charges_per_unit`, `total_charges`, `tax`, `bill`) VALUES (%s, %s, %s, %s,  %s, %s, %s, %s, %s, %s,%s)"
                                    cursor.execute(sql2, (unit,charges,meter_number, location, past_unit, current_unit, consumed_unit, charges_per_unit, total_charges, tax, bill))
                                    connection.close()
                                    cursor.close()

                            except Exception as e:
                                print(e)

        except Exception as e:
            print(e)

        pygame.display.flip()
        clock.tick(120)

meterloop(temp_line)

pygame.quit()
quit()
