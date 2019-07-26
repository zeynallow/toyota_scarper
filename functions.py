import urllib.request, os
import ssl

def downloadUrl( url, filename = None ):
    if not filename:
        filename = os.path.basename( os.path.realpath(url) )

    req = urllib.request.Request( url, headers={'User-Agent': 'Mozilla/5.0'} )
    try:
        response = urllib.request.urlopen( req, context=ssl._create_unverified_context() )
    except urllib.error.URLError as e:
        if hasattr( e, 'reason' ):
            print( '====> FAIL SERVER -> ', e.reason )
            return False
        elif hasattr( e, 'code' ):
            print( '====> THE SERVER COULDN\'T FULFILL THE REQUEST -> ', e.code )
            return False
    else:
        with open( filename, 'wb' ) as fo:
            fo.write( response.read() )
            print( '====> FILE SAVED:  %s' % filename )
        return True