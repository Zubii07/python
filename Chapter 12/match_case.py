# Similar to switch statement

def http_status(status):
    match status:
        case 200:
            return 'OK'        
        
        case 404:
            return 'Not Found'
        
        case 500:
            return 'Internal server error'
        
        case _:
            return 'Unknown Status'
        


print(http_status(200))        