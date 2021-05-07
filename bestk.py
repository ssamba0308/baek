import pybithumb
import numpy  as  np


def  get_ror ( k = 0.5 ) :
    df  =  pybithumb . get_ohlcv ( "KRW-BTC", count=7 )
    df [ 'range' ] = ( df [ 'high' ] -  df [ 'low' ]) *  K
    df [ 'target' ] =  df [ 'open' ] +  df [ 'range' ]. shift ( 1 )

    df [ 'ror' ] =  np . where( df [ 'high' ] >  df [ 'target' ],
                         df [ 'close' ] /  df [ 'target' ],
                         1 )

    ror  =  df[ 'ror' ].cumprod()[-2 ]
    return  ror


for  K  in np . arange( 0.1 , 1.0 , 0.1 ) :
    ror  =  get_ror ( k )
    print ( "% .1f % f"  % ( k , ror ))