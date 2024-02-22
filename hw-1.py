#Write a function draw_grid(m=2, n=3) that draws a similar grid with m rows and n columns.

def draw_grid(row, col):
  #定義ziqi為首行邊界線
  ziqi = '\n' + '+ - - '* col + '+\n'
  return ziqi + ('/     '* col + '/\n' + '/     '* col + '/' + ziqi)*row

print(draw_grid(2,3))