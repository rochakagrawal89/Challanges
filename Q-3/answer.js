let str = `{"return":
                     {
                       "response": [{"$": 1234}],
                       "responseMessage": [{"$": "Success ABC"}],
                       "responseCode": [{"$": "CITY,India"}]
                     }
                    }`;
    
    
        let js_object = JSON.parse(str); // parse json string to javascript object
        let js_object_return = js_object.return;
        let formated_obj = {};
        let desired_obj = {};
        Object.keys(js_object_return).forEach(function(key) {
            formated_obj[key] = js_object_return[key][0]["$"];
        });
        desired_obj['return']=formated_obj;
        console.log(desired_obj.return.response);