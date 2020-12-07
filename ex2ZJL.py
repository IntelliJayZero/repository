import time
scale = 57
print('周杰伦：“今年一定会有新专辑”'.center(scale, '-'))
print('')
time.sleep(4)
start = time.perf_counter()
for i in range(scale+1):
    a = '_' * i
    b = '_' * (scale-i)
    c = (i/scale)
    d = time.perf_counter()-start
    print('\r{:.3%} [{}|周杰伦>{}]{:.0f}天--正在做新专辑'.format(c, a, b, d*23.7),end='')
    time.sleep(0.37)
print('\n已完成\n'+'结论：周杰伦是鸽中之鸽！'.center(scale, '-'))