saldo_awal = 5000
deposit = input('masukan jumlah deposit... ')
saldo_total = saldo_awal + int(deposit)
hutang = 50000

if saldo_total >= hutang:
    print('saldo anda cukup untuk membayar hutang, saldo anda akan terpotong secara otomatis untuk membayar hutang')
elif saldo_total <= hutang:
    print('saldo anda tidak cukup untuk membayar hutang... mohon melakukan deposit lagi')
