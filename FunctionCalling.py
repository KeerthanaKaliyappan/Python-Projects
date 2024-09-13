# Function calling with GPT

#Function calling is when a model cannot fetch some real time data.
#We provide list of function descriptions to the model, it returns the custom function or API with required params
#We can make the call to the returned function description.

#Note: Models don't make call to custom functions, they return the matching function to call.

from openai import OpenAI

client=OpenAI(
    api_key="Your OpenAI API KEY"
)

def get_stock_price_XYZ(price):
    price_info={
        "name": "X",
        "price": price
    }
    return json.dumps(price_info)

functions=[
    {
        "name": "get_stock_price_XYZ",
        "description": "Get the stock price of XYZ Company",
        "parameter": {
            "type": "object",
            "properties": {
                "price": {
                    "type": "float",
                    "description": "The stock price in INR"
                }
            },
            "required": ["price"],
        }
    }
]

response=client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "What is the stock price of XYZ Company"}],
    functions=functions
    function_call="auto"
)
#If we are calling a single known functions, we can replace "auto" with {"name": "function_name"}

response_message=response.data[0].message
if response_message.function_call:
    args=json.loads(response_message.function_call.arguments)
    print(get_stock_price_XYZ(args.get('price')))