import json

print('Loading function')


def lambda_handler(event, context):
    
    body = json.loads(event['body'])
    
    op = body["op"]
    a = body["a"]
    b = body["b"]

    ans = '0.00'
    if( op == '+'):
        ans = float(a) + float(b) 
    elif(op == '-'):
        ans = float(a) - float(b) 
    elif(op == '*'):
        ans = float(a) * float(b) 
    elif(op == '/'):
        try:
            ans = float(a) / float(b) 
        except:
            ans = 'can not devide by 0'
    else:
        ans = op + ' is not an operation'
    
    return {
         'statusCode': 200,
         'body': json.dumps({'result':str(ans)})
    }
    

