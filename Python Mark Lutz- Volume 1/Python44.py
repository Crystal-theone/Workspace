import decimal
with decimal.localcontext() as ctsx:
    ctsx.prec=4;
    ans=decimal.Decimal('1.00')/decimal.Decimal('3.00')
    print(ans)
